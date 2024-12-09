# Ch02-2. 資料型別 - 數值
""" 整數 """
num1 = 10      # 正整數 
print(num1)

num2 = -10     # 負整數
print(num2)
print(type(num2))

x=1234567890
print(type(x))

y=5000000000000000000000000000000000000000000000000000000
print(type(y))

# 不允許非零整數前導零
x=001234567890    
# SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
z = 0000
print(z) # 0

""" 浮點數 """
num3 = 1.23    # 浮點數
print(num3)
print(type(num3)) # <class 'float'>

f = 1e3
print(f) # 1000.0

f = 1e5
print(f) # 100000.0

f = 3.4556789e2
print(f) # 345.56789
print(type(f)) # <class 'float'>

# 浮點數間運算存在不確定尾數
print(0.1 + 0.3)    # 0.4
print(0.1 + 0.2)    # 0.30000000000000004

print(0.1 + 0.2 == 0.3)            # False
print(round(0.1 + 0.2,1))          # 0.3
print(round(0.1 + 0.2,1) == 0.3)   # True


""" 布林值 """
isNum = True   # 布林值
print(isNum)
print(type(isNum)) #

num5 = num1 + isNum    # 值為 11
print(num5)
print(type(num5)) #

num6 = num3 + isNum    # 值為 2.23
print(num6)
print(type(num6)) #


""" 空型別 """
num4 = None    # 空物件
print(type(num4)) # <class 'NoneType'>
num7 = num4 + num3 # TypeError: unsupported operand type(s) for +: 'NoneType' and 'float'

""" 二進制 """
b = 0b010   # 二進制
print(b)    # 值為 2

B = -0B101  # 二進制
print(B)    # 值為 -5
print(type(B)) # <class 'int'>

""" 八進制 """
o = 0o123   # 八進制
print(o)    # 值為 83

O = -0O45   # 八進制
print(O)    # 值為 -37
print(type(O)) # 

""" 十六進制 """
h = 0x9a   # 十六進制
print(o)    # 值為 83

H = -0X89   # 十六進制
print(O)    # 值為 -37
print(type(H)) # <class 'int'>

""" 算術運算子 """
# 加
a, b = 10, 20
print(a + b)  # 30

# 減
a, b = 10, 20
print(a - b)  # -10

# 乘
a, b = 10, 20
print(a * b)  # 200

# 除
a, b = 10, 20
print(b / a)  # 2.0

# 整除數
a, b = 9, 2
print(a // b)  # 4

# 餘數
a, b = 10, 3
print(a % b)  # 2

# 次方
a, b = 3, 2
print(a ** b)  # 9

# 開根號
a = 10 ** 0.5
print(a)

x = 1
# 複合運算子
x += 1  # 就是 x = x + 1
print(x)

x = 5
x += 2 
print( x )  # 7

x -= 2
print( x )  # 3

x *= 2
print( x )  # 10

x /= 2
print( x )  # 2.5

x //= 2
print( x )  # 2

x %= 2
print( x )  # 1

x **= 2
print( x )  # 25

""" int() """
x = 2.5  # 浮點數 
y = int(x)  # 2 整數
print(y) 
print(type(y))

""" float() """
x = "2.5"  # 字串
y = float(x)  # 2.5
print(y)  # 2.5

""" abs() """
x = -10.01
print(abs(x))  # 10.01 

""" round() """
x = round(3.14159, 2)
print(x)  # 3.14

""" divmod() """
x = divmod(7, 3)
print(x)  # (2, 1)

""" pow() """
x = pow(3, 7)
print(x)  # 2187

""" bin() """
x = bin(128)
print(x) # '0b10000000'

""" oct() """
x = oct(128)
print(x) # '0o200'

""" hex() """
x = hex(128)
print(x) # '0x80'

""" Lab 1 """
dayup = 1.01 ** 365
print(dayup)  # 37.78343433288728

dayup = pow(1.01, 365)
print(dayup)  # 37.78343433288728

""" Lab 2 """
daydown = 0.99 ** 365
print(daydown)  # 0.025517964452291125

daydown = pow(0.99, 365)
print(daydown)  # 0.025517964452291125

""" Lab 3 """
ans = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20 + 21 + 22 + 23 + 24 + 25 + 26 + 27 + 28 + 29 + 30 + 31 + 32 + 33 + 34 + 35 + 36 + 37 + 38 + 39 + 40 + 41 + 42 + 43 + 44 + 45 + 46 + 47 + 48 + 49 + 50 + 51 + 52 + 53 + 54 + 55 + 56 + 57 + 58 + 59 + 60 + 61 + 62 + 63 + 64 + 65 + 66 + 67 + 68 + 69 + 70 + 71 + 72 + 73 + 74 + 75 + 76 + 77 + 78 + 79 + 80 + 81 + 82 + 83 + 84 + 85 + 86 + 87 + 88 + 89 + 90 + 91 + 92 + 93 + 94 + 95 + 96 + 97 + 98 + 99 + 100
print(ans)

ans = 101 * 50
print(ans)


""" 隨堂測驗 """
# Q1
A = 10000000 * 30
B = pow(2,29) # 或者 2 ** 30
print(A)
print(B)

# Q2
num = 10 + True
print(num)

# Q3
print(type(8.2+1.8))

# Q4
num = 19 % 5
print(num)

# Q5
bin(12)