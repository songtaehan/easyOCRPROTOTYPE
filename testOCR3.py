import cv2
import base64
import json
import requests
import re

# API URL 및 키 설정
api_url =''
api_key = ''  # 네이버 클로바에서 받은 API 키

# 이미지 파일 경로 설정
image_file_path = r'C:\Users\user\Desktop\easyOCR\36.jpg'
output_file_path = r'C:\Users\user\Desktop\easyOCR\ocr_results.txt'  # 결과를 저장할 파일 경로

# 헤더 설정
headers = {
    'X-OCR-SECRET': api_key,
    'Content-Type': 'application/json'
}

# 이미지 파일 읽기 및 크기 조정
image = cv2.imread(image_file_path)

# 이미지 리사이즈
image_resized = cv2.resize(image, (1024, 1024), interpolation=cv2.INTER_AREA)

# 리사이즈된 이미지 저장
cv2.imwrite(image_file_path, image_resized)

# 리사이즈된 이미지를 Base64로 인코딩
with open(image_file_path, 'rb') as f:
    image_data = f.read()
    image_data_base64 = base64.b64encode(image_data).decode('utf-8')

# 요청 페이로드 생성
payload = {
    'version': 'V1',
    'requestId': 'string',
    'timestamp': 0,
    'images': [
        {
            'name': 'string',
            'format': 'jpg',
            'data': image_data_base64
        }
    ]
}

# JSON 변환
json_payload = json.dumps(payload)

# 요청 보내기
response = requests.post(api_url, headers=headers, data=json_payload)

# 응답 확인 및 저장
if response.status_code == 200:
    print('OCR Success')
    ocr_result = response.json()
    
    if 'images' in ocr_result:
        # 추출된 텍스트 저장
        text_result = ""
        for image in ocr_result['images']:
            for field in image['fields']:
                text_result += field['inferText'] + "\n"
        
        # 문자열로 저장
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(text_result)
        print(f'Results saved to {output_file_path}')
    else:
        print('OCR result does not contain expected data.')
else:
    print('OCR Failed')
    print(response.status_code)
    print(response.text)

# 저장된 결과를 파일에서 읽고 출력
try:
    with open(output_file_path, 'r', encoding='utf-8') as f:
        saved_results = f.read()
        print('Saved OCR Results:')
        print(saved_results)
except FileNotFoundError:
    print(f'File not found: {output_file_path}')
except Exception as e:
    print(f'Error reading file: {e}')


ocr_text = text_result

# 추출할 키워드
keywords = ['kcal', '나트륨', '탄수화물', '당류', '지방', '트랜스지방', '포화지방', '콜레스테롤', '단백질']

# 데이터 추출을 위한 정규 표현식 패턴
pattern = re.compile(r'(\w+)\s*([\d\.]+)\s*(kcal|mg|g)')

# 결과 저장
results = {}

# OCR 텍스트에서 데이터 추출
for match in pattern.finditer(ocr_text):
    label, value, unit = match.groups()
    if label in keywords:
        results[label] = f"{value} {unit}"

# 결과 출력
for key, value in results.items():
    print(f"{key}: {value}")
