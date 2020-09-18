# 字符串 String
# 使用 '' 或者 "" 来创建字符串
str = "hello everyone"
print(str)

# 字符串截取 
# 从前往后 下标从 0 开始 0，1，2，3
# 从后往前 下标从 -1 开始 -4，-3，-2，-1

# 遵循左闭右开 原则，不包含最后的元素
print(str[0:])
print(str[0:2])
print(str[0:-1])

# 转义字符 \
print('hello\nnihao')
# 不转义前缀 r 或 R 直接输出原始字符
print(r'hello\nnihao')
# 格式化字符串 %
# 常用 %s-格式化字符串 %d-格式化整数 %f-格式化浮点数


# 三引号 ，允许一个字符串跨多行，可以包含换行符 制表符以及其他特殊字符
str_param = '''我是三引号,可以包含制表符\t,换行符 \n和其他字符'''
print(str_param)

# f-string 新的格式化字符串的语法
# 替换变量 f'hello {name-变量名}' 
# 使用表达式 f '{1+1}'

name = 'konglj'
print(f'你好，{name}')


x = 1
print(f'{10+1}')
# Python3.8print(f'{x+1=}')