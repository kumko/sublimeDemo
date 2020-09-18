# key-value 键值对，键唯一必须是不可变类型 如数字 字符串 元组
dict = {'name':'klj','age':10,'address':'安徽省苏鄂州市砀山县'}
if('name' in dict.keys()){
	print(123);
}
print(dict)
# 根据key获取value
print(dict['name'])
print(dict['address'])
# print(dict['12'])  当key不存在时，会报错
# 修改值
dict['name'] = '孔丽娟'
print(dict)
print(type(dict))

del dict['name']
print(dict)
print('keys =',dict.keys())
dict.clear()
print(dict)

print('keys =',dict.keys())




