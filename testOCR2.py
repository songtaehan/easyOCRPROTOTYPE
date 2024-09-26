import easyocr
print(dir(easyocr))
reader = easyocr.Reader(['ko','en'],gpu = True)
result = reader.readtext("cocoa.jpg", detail = 0)
print(result)
new_result = [i.replace(' ','') for i in result]
print(new_result)
split_result = [i.split() for i in result]
print(split_result)
go = list()
info = list()
info2 = list()
info3 = list()
info4 = list()
info5 = list()
info6 = list()
info7 = list()
info8 = list()
info9 = list()
info10 = list()
info = [go for go in split_result if 'kcal' in go ]
info2 = [go for go in split_result if '나트륨' in go ]
info3 = [go for go in split_result if '탄수화물' in go ]
info4 = [go for go in split_result if '당류' in go ]
info5 = [go for go in split_result if '지방' in go ]
info6 = [go for go in split_result if '트랜스지방' in go ]
info7 = [go for go in split_result if '포화지방' in go ]
info8 = [go for go in split_result if '콜레스테롤' in go ]
info9 = [go for go in split_result if '단백질' in go ]
print(info)
print(info2)
print(info3)
print(info4)
print(info5)
print(info6)
print(info7)
print(info8)
print(info9)

totalinfo = list()
totalinfo = info + info2 + info3 + info4 + info5 + info6 + info7 + info8 + info9
print(totalinfo)


totalinfo[1][1]
