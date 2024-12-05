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