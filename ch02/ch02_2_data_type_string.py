'This is a string in Python' # 單引號括起來的字串
"This is a string in Python" # 雙引號括起來的字串
'''This is a string in Python''' # 三個單引號括起來的字串
"""This is a string in Python""" # 三個雙引號括起來的字串

# 文字賦值給變數
str1 = 'This is a string in Python' 
print(str1)

str2 = "This is a string in Python" 
print(str2)


# 三個單引號或三個雙引號
str1 = '''This is 
the first
Multi-line string.
'''
print(str1)

str2 = """This is
the second
Multi-line
string."""
print(str2)

# 單/雙引號作為字串的一部分
str1 = 'Welcome to "Python Tutorial" on TutorialsTeacher'
print(str1)

str2 = "Welcome to 'Python Tutorial' on TutorialsTeacher"
print(str2)

# 字串[索引]
str1 = "零壹貳叄"
# 提取索引 2 的字元。
print(str1[2])  # 貳

# 提取索引 -1 的字元。
print(str1[-1]) # 叄

str1 = "零壹貳叄"
# 提取索引 1 到 2 的字串，不含索引 3。
print(str1[1:3])     # 壹貳

# 提取索引 0 到 2 的字串。
print(str1[0:3])     # 零壹貳
# 若從第一個字元開始，則起始值可以省略不寫。
print(str1[:3])      # 零壹貳

# 提取索引 1 到最後的字串。
print(str1[1:4])     # 壹貳叄
print(str1[1:])      # 壹貳叄

str2 = "零壹貳叄肆伍陸柒捌玖拾"
# 提取索引 3 到 -3 的字串。
print(str2[3:-3])    # 叄肆伍陸柒

#提取索引 -5 到最後的字串。
print(str2[-5:])     # 陸柒捌玖拾

# 提取索引是偶數的字串。
print(str2[::2])     # 零貳肆陸捌拾
# 提取索引是奇數的字串。
print(str2[1::2])    # 壹叄伍柒玖

# 將字串倒過來
print(str2[::-1])    # 拾玖捌柒陸伍肆叄貳壹零


# 字串是一個不可變的物件
str3 = "Hello"
str3[0] = "A"   # TypeError: 'str' object does not support item assignment

""" 跳脫字元 """
# 單引號「'」
str1 = "這是\'單引號"
print(str1)

# 雙引號「"」
str1 = "這是\"雙引號"
print(str1)

# 反斜線
str1 = "這是\\反斜線"
print(str1)

# 換行
str1 = "這是\n換行"
print(str1)

# 游標移到列首
str1 = "這是\r游標移到列首"
print(str1)

# Tab
str1 = "這是\tTab"
print(str1)

# 倒退鍵(BackSpace)
str1 = "這是\b倒退鍵(BackSpace)"
print(str1)

# 以十六進位表示字元
str1 = "\x48\x69"
print(str1)

# 以八進位表示字元
str1 = "\110\151"
print(str1)

""" 字串運算子(Operator) """
# +
a = 'Hello,'
b = 'Python'
print(a + b)  # Hello,Python

# *
a = 'Python,'
print(a * 3)  # Python,Python,Python,

# []
a = 'Python'
print(a[2])  # t

# [:]
a = 'Python'
print(a[2:4])  # th

# in
a = 'Python'
print('x' in a)  # False
print('y' in a)  # True
print('p' in a)  # False

# not in
a = 'Python'
print('x' not in a)  # True
print('y' not in a)  # False


""" 字串函數 """
# str()
a = 3.0
b = "輸入的數值是："
print(b + str(a))

# lower()
a = "PYTHON"
print(a.lower())  # python

# upper()
a = "python"
print(a.upper())  # PYTHON

# capitalize()
a = "python"
print(a.capitalize())  # Python

# find()
a = "hello world"
print(a.find("world"))  # 6

# index()
a = "hello world"
print(a.index("o"))  # 4

# replace()
a = "hello world"
print(a.replace("world", "Python"))  # hello Python

# split()
a = "1,2,a,b"
b = a.split(",")  # ['1', '2', 'a', 'b']

# join()
a = [1, 2, 'a', 'b']
print("-".join(b))  # 1-2-a-b

# strip()
a = "  hello  "
print(a.strip())  # hello
print(a.lstrip())
print(a.rstrip())

""" 隨堂測驗 """
# Q1
print(7 + "13")

# Q2
a = "這是資料型別-字串的隨堂測驗"
print(a[2:-5])

# Q3
# \b 是倒退鍵

# Q4
# round() 是數值函數

# Q5
student = "    林小宇武技安   "
math1 = 100     # 林小宇的數學成績
math2 = 87      # 武技安的數學成續
english1 = 99   # 林小宇的英文成績
english2 = 78   # 武技安的英文成績

student1 = student.strip()[0:3]
student2 = student.strip()[3:6]

print("\\"+student1+"\\")
print("數學：" + str(math1) + " 分")
print("英文：" + str(english1) + " 分")
print("總成績：" + str(math1 + english1) + " 分")
print("總成績：" + str(round((math1 + english1)/2,1)) + " 分")
print("\\"+student2+"\\")
print("數學：" + str(math2) + " 分")
print("英文：" + str(english2) + " 分")
print("總成績：" + str(math2 + english2) + " 分")
print("總成績：" + str(round((math2 + english2)/2,1)) + " 分")