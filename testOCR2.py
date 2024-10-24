import easyocr
import cv2
import numpy as np

#print(dir(easyocr))
image_file = cv2.imread('cocoa.jpg')

if image_file is None:
    print("Error loading image")
else:
    resized_img = cv2.resize(image_file, dsize=(3000, 2500), interpolation=cv2.INTER_LINEAR)
    print("Image resized successfully")


reader = easyocr.Reader(['ko','en'],gpu = False)
result = reader.readtext(resized_img, detail = 0)
print("-----------result")
print(result)

#new_result = [i.replace(' ','') for i in result]
#print("----------new_result")
#print(new_result)

split_result = [i.split() for i in result]
print("----------split_result")
print(split_result)

go = list()
info1 = list()
info2 = list()
info3 = list()
info4 = list()
info5 = list()
info6 = list()
info7 = list()
info8 = list()
info9 = list()
info10 = list()

info1 = [go for go in split_result if 'kcal' in go ]
info2 = [go for go in split_result if '나트륨' in go ]
info3 = [go for go in split_result if '탄수화물' in go ]
info4 = [go for go in split_result if '당류' in go ]
info5 = [go for go in split_result if '지방' in go ]
info6 = [go for go in split_result if '포화지방' in go ]
info7 = [go for go in split_result if '콜레스테롤' in go ]
info8 = [go for go in split_result if '단백질' in go]
info9 = [go for go in split_result if '탄백질' in go]
info10 = [go for go in split_result if '프화지방' in go]
print("-------------1")
print(info1)
print(info2)
print(info3)
print(info4)
print(info5)
print(info6)
print(info7)
print(info8)
print(info9)
print(info10)
data = list()
totalinfo = list()
totalinfo = info1 + info2 + info3 + info4 + info5 + info6 + info7 + info8 + info9 + info10
print("------------------2")
print(totalinfo)

print("------------------3")
print("데이터 추출 완료")
for i in range(len(totalinfo)):
    if totalinfo is None:
        pass
    elif totalinfo[i][0] == '탄수화물':
        print(totalinfo[i][1] + "_탄수화물")
    elif totalinfo[i][0] == '당류':
        print(totalinfo[i][1] + "_당류")
    elif totalinfo[i][0] == '지방':
        print(totalinfo[i][1] + "_지방")
    elif totalinfo[i][0] == '포화지방':
        print(totalinfo[i][1] + "_포화지방")
    elif totalinfo[i][0] == '프화지방':
        print(totalinfo[i][1] + "_포화지방")
    elif totalinfo[i][0] == '단백질':
        print(totalinfo[i][1] + "_단백질")
    elif totalinfo[i][0] == '탄백질':
        print(totalinfo[i][1] + "_단백질")
    elif totalinfo[i][1] == 'kcal':
        print(totalinfo[i][0] + "_kcal")
    elif totalinfo[i][2] == 'kcal':
        print(totalinfo[i][1] + "_kcal")
    else:
        pass   
    



