# 函数的参数类型
	# 必备参数
	# 关键字参数
	# 默认参数
	# 可变参数 实际传递的是一个元组
# 必备参数
def necessary_param(param):
	print(param)

#关键字参数
def key_word_param(name,age):
	print('name=',name,',age=',age)
	return
# 默认参数 不传递参数时使用默认值的参数
def default_param(name,age=18):
	print('name=',name,',age=',age)
	return
# 可变参数 参数数量不一定的函数
def var_params(name,*varparams):
	print (name)
	print('不定长参数：',varparams)
	return

# 下面开始依次调用这些函数
necessary_param('你好')
key_word_param(age = 50,name = '孔丽娟')
default_param(name='孔丽娟')
var_params('孔丽娟',12,'你好哦','我是你的朋友')




# 匿名函数 lambda表达式创建匿名函数
# lambda [arg,[arg1,arg2......argn]]:expression
sum = lambda param1,param2:param1+param2
print(sum(10,10))