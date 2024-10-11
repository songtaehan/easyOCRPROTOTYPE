import requests
import json

# API URL 및 키 설정
api_url = 'https://clova.ai/apis/ocr/nmap/'
api_key = 'YOUR_API_KEY'  # 네이버 클로바에서 받은 API 키

# 이미지 파일 경로 설정
image_file_path = 'your_image_file.jpg'
output_file_path = 'ocr_results.txt'  # 결과를 저장할 파일 경로

# 헤더 설정
headers = {
    'X-OCR-SECRET': api_key,
    'Content-Type': 'application/json'
}

# 요청 페이로드 설정
payload = {
    'version': 'V1',
    'requestId': 'string',
    'timestamp': 0,
    'images': [
        {
            'name': 'string',
            'format': 'jpg',
            'data': None
        }
    ]
}

# 이미지 파일을 바이너리로 읽어오기
with open(image_file_path, 'rb') as f:
    image_data = f.read()
    payload['images'][0]['data'] = image_data

# JSON으로 변환
json_payload = json.dumps(payload)

# 요청 보내기
response = requests.post(api_url, headers=headers, data=json_payload)

# 응답 확인 및 저장
if response.status_code == 200:
    print('OCR Success')
    ocr_result = response.json()
    
    # 결과를 파일에 저장
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(ocr_result, f, ensure_ascii=False, indent=4)
    
    print(f'Results saved to {output_file_path}')
else:
    print('OCR Failed')
    print(response.status_code)

# 저장된 결과를 파일에서 읽고 출력
with open(output_file_path, 'r', encoding='utf-8') as f:
    saved_results = json.load(f)
    print('Saved OCR Results:')
    print(json.dumps(saved_results, ensure_ascii=False, indent=4))
