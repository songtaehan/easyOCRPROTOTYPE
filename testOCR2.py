import easyocr
import cv2
import numpy as np

print(dir(easyocr))
image_file = cv2.imread('cocoa.jpg')

if image_file is None:
    print("Error loading image")
else:
    resized_img = cv2.resize(image_file, dsize=(3000, 2500), interpolation=cv2.INTER_LINEAR)
    print("Image resized successfully")


reader = easyocr.Reader(['ko','en'],gpu = True)
result = reader.readtext(resized_img, detail = 0)
print(result)

new_result = [i.replace(' ','') for i in result]
print(new_result)

split_result = [i.split() for i in result]
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

info1 = [go for go in split_result if 'kcal' in go ]
info2 = [go for go in split_result if '나트륨' in go ]
info3 = [go for go in split_result if '탄수화물' in go ]
info4 = [go for go in split_result if '당류' in go ]
info5 = [go for go in split_result if '지방' in go ]
info6 = [go for go in split_result if '포화지방' in go ]
info7 = [go for go in split_result if '콜레스테롤' in go ]
info8 = [go for go in split_result if '단백질' in go ]
print(info1)
print(info2)
print(info3)
print(info4)
print(info5)
print(info6)
print(info7)
print(info8)


totalinfo = list()
totalinfo = info1 + info2 + info3 + info4 + info5 + info6 + info7 + info8  
print(totalinfo)


print(totalinfo[0][0])
print(totalinfo[1][1])
print(totalinfo[2][1])
print(totalinfo[3][1])
print(totalinfo[4][1])
print(totalinfo[5][1])


data0 = totalinfo[0][0]
data1 = totalinfo[1][1]
data2 = totalinfo[2][1]
data3 = totalinfo[3][1]
data4 = totalinfo[4][1]
data5 = totalinfo[5][1]


data1 = data1[:-1]
data2 = data2[:-1]
data3 = data3[:-1]
data4 = data4[:-1]
data5 = data5[:-1]

print("----------------------")
print("데이터 추출 완료")
print(data0) #kcal
print(data1) #탄수화물
print(data2) #당류
print(data3) #지방
print(data4) #포화지방
print(data5) #단백질
