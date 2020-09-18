import xlrd

sheetNames = [11,12,13,14,15,17,18,19,20,21,24]
path = "C:\\Users\\QWERT\\Desktop\\temp\\砀山设备表.xlsx";
repeat = {};
def excel_read(path):
	wb = xlrd.open_workbook(path)
	data = {};
	# 根据sheet名获取工作表
	for index in sheetNames:
		name = "EVS"+str(index);
		print(name);
		sheet = wb.sheet_by_name(name)
		for a in range(sheet.nrows):
			# print('当前行数：',a)
			if a != 0:
				row = sheet.row_values(a);
				ip = row[4];
				if ip in data.keys() and ip != '':
					evs = data[ip];
					data[ip] = evs + ',' +name;
					repeat[ip] = data[ip];
				else:
					data[ip] = name;
	return data;

excel_read(path);

for temp in repeat.keys():
	print(temp,":",repeat[temp]);