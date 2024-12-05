# Ch02-1. 變數

""" 註解 """
# 單行註解
# 將 3 賦值給變數 A
A = 3
hero.say(A) # 命令英雄說出"變數A"的數值

# 多行註解
'''
向寶石進發。
小心撞牆！
在下面輸入你的代碼。
'''

""" 變數 (Variables) """
變數名稱 = "變數值"

# Python變數
# 將 3 賦值給變數 A
A = 3
hero.say(A) # 命令英雄說出"變數A"的數值

num = 10 #integer variable
amount = 78.50 #float variable
greet='Hello World' #string variable
isActive = True #boolean variable

""" 物件（Objects） """
# 型別
num = 10
print(type(num))  #<class 'int'>

amount = 78.50
print(type(amount))  #<class 'float'>

greet='Hello World'
print(type(greet))   #<class 'str'>

isActive = True
print(type(isActive))  #<class 'bool'>

# 物件的ID
x = 100
print(id(x))

greet='Hello'
print(id(greet))


""" 多變數賦值 """ 
A = B = C = 3
x, y, z = 10, 'Hello', True
print(x, y, z)  #10 Hello True
x = 10, y = 'Hello', z = True  # SyntaxError: cannot assign to literal

""" 刪除變數 """
del 變數名稱

""" 變數命名規則 """
7eleven = 11  # 第一個字母不可以是數字
H&M = 1       # 不能有特殊字元
H M = 1       # 不能有空白
for = 1       # 不能是系統保留字
If = 1        # 可以，大寫的 If 不是系統保留字