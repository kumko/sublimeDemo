import xlrd
from xlutils.copy import copy
def excel_read(path):
	wb = xlrd.open_workbook(path)
	# 根据sheet名获取工作表
	sheet = wb.sheet_by_name('test2')
	data = []
	for a in range(sheet.nrows):
		# print('当前行数：',a)
		if a != 0:
			row = sheet.row_values(a)
			data.append(row[1])
	return data;
# 循环结果集
# result = excel_read('C:\\Users\\QWERT\\Desktop\\每日离线统计\\08\\0831\\08-31.xls')

def excel_read_dict(path):
	wb = xlrd.open_workbook(path)
	# 根据sheet名获取工作表
	sheet = wb.sheet_by_name('test2')
	data = dict()
	for a in range(sheet.nrows):
		# print('当前行数：',a)
		if a != 0:
			row = sheet.row_values(a)
			data[int(row[0])] = row[1] + ',' + '116.63' + ',' + '34.336'
	return data;
result = excel_read_dict('C:\\Users\\QWERT\\Desktop\\每日离线统计\\08\\0831\\08-31.xls')
print(result)
for cell in result:
	if cell != '':
		print (cell)
	