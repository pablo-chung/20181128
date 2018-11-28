'''
x=1;y=20;z='grace'
print(x,y,z, sep='/')
print(x,y,z, sep='z')
print(x,y,z, end='')
print()
print(x,y,z, end='\n')
print("x*y=", x*y)
file_path =r"C:\Documents and Settings\ericsk\test.dat"
print (file_path)

#ch0103
import time
name=input('你的名字:')
print('hi', name,'現在時間是:', time.ctime())

print('hello pablo')

#ch1學習評量
import time #匯入時間模組
name = input('你的名字-> ')
print('Hi', name, '現在時間')
print()
print(time.ctime())
print( ) #輸入空白行
#print(time.clock())

print(78+56)
print(125-41)
print(" ----- ")
print("/Hello\\")
print("|Mary!|")
print("\     /")
print(" ----- ")
print(">>> |  ")
'''
'''
x=['100000']
print(id(x))
print(type(x))
number=147
print(id(number))
print(type(number))
y=24.7789
print(id(y))
print(type(y))
'''
'''
a = b = 55.8
c , d = "marry" , 22+45*333*457*9999999
print(a,b,c,d)
print(type(a), type(b), type(c), type(d))
print(id(a), id(b), id(c), id(d))
'''
'''
#CH0201.py
num1, num2, num3=eval(input('請輸入3個值,以逗號隔開:'))
#total = num1+num2+num3
print('數值合計=',num1+num2+num3)
'''

#CH0202.py
number=int(input('輸入一個數值-->'))
print('型別:', type(number))
print('二進位:', bin(number))
print('八進位:', oct(number))
print('十六進位:', hex(number))
print('10進位:', number)
print('二進位:', format(number, 'b'))
print('八進位:', format(number, 'o'))
print('十六進位:', format(number, 'x'))

'''
#CH0203.py
import math
a=1E309
print('a=1E309, 輸出', a)
#輸出True, 表示它是 NaN
print('為NaN?', math.isnan(float(a/a)))
b=-1E309
print('b=-1E309, 輸出', b)
#輸出True, 表示它是Inf
print('為Inf?', math.isinf(float(-1E309)))
'''