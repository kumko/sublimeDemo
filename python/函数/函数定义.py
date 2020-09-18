# 函数定义 def function_name(参数列表):

def myself(str):
	print(str)

myself('传递的参数')

# 不可变对象参数  string number tuple 相当于值传递
temp = 1
def value_transfer(value):
	value = 10
	print('函数内改变参数值后',value)
value_transfer(temp)
print('函数调用后，函数外的参数值',temp)


# 可变对象参数 list dict set 相当于址传递
temp1 = [1,2,32]
def address_transfer(value):
	value.append([123,45])
	print('函数内改变参数值后',value)
address_transfer(temp1)
print('函数调用后，函数外的参数值',temp1)