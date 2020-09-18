# list 使用方括号定义[]
list0 = [1,2,6,5]
print(list0)
# 通过索引获取值，索引从0开始
print('list[0]=',list0[0])
print('list[2]=',list0[2])
print('list[1:2]',list0[1:3])

# del 删除元素
del list0[2]
print(list0)
# 修改元素
list0[2] = 10
print(list0)

# 获取长度
print(len(list0))


list1 = ['k','k','l','4']
list2 = [list0,list1]
print(list2)
print(len(list2))

# 常用函数 
# len(list) 列表元素个数
# max(list) 列表最大值
# min(list) 列表最小值
# list(seq) 元组转列表
print('max = ',max(list0))
print('min = ',min(list0))


tup = (1,2,'45')
print(tup)
print(list(tup))