from operator import pos
import requests
import json
import xlwt
import xlrd
import time
import os
import dh
from xlutils.copy import copy
path = "C:\\Users\\QWERT\\Desktop\\每日离线统计\\维修记录\\梨花广场.xlsx";
result = [];
ip = "34.33.8.25";
url_login = "http://"+ip+"/RPC2_Login";
url_camera = "http://"+ip+"/RPC2";
device_info = {};
notExists = ["007074砀山梨花广场西入口停车场1",
"007066砀山梨花广场银杏路北2",
"007164砀山梨花广场西北入口球机",
"91007033砀山梨花广场北入口3",
"007035砀山梨花广场香樟路东入口枪机",
"007154砀山梨花广场西停车场西北角",
"007099砀山梨花广场东卫生间",
"007157砀山梨花广场西卫生间",
"007169砀山梨花广场梅林凉亭",
"007171砀山梨花广场梅林凉亭西假山",
"007161砀山梨花广场假山桥东",
"007151砀山梨花广场听涛路南3",
"007098砀山梨花广场九曲桥东1",
"007083砀山梨花广场环湖路东入口1",
"007081砀山梨花广场环湖路东入口球机",
"007104砀山梨花广场香樟大道东入口2",
"007124砀山梨花广场网球场西4",
"007110砀山梨花广场东南入口1",
"007117砀山梨花广场东南入口2",
"007118砀山梨花广场东南入口3",
"007111砀山梨花广场健身路东1",
"007135砀山梨花广场健身路西",
"007132砀山梨花广场南入口东1",
"007066砀山梨花广场银杏路北2",
"007064砀山梨花广场银杏路北1",
"007065砀山梨花广场樱花路北"]
# 统计离线
def camera_status(urlLogin,urlCamera,currentTime):
	print("camera_status执行");
	# 登录
	response =dh.before_login(urlLogin);
	session = dh.dealResponse(response)["session"];
	response = dh.login(urlLogin,session);

	# 查询相机详情
	response = dh.camera_info(urlCamera,session);
	camera_json = dh.dealResponse(response);
	camera_list = camera_json["params"]["camera"];
	for camera in camera_list:
		if "DeviceID" in camera.keys():
			uuid = camera["DeviceID"];
			device = camera["DeviceInfo"];
			channels = device["VideoInputs"];
			if channels[0] != None :
				name = channels[0]["Name"];
			else :
				name = "";
			device_info[uuid] = name;
			# print(uuid,":",address);
	# 查询相机在离线状态
	response = dh.camera_onOffLine(urlCamera,session);
	camera_json = dh.dealResponse(response);
	camera_onLine_list = camera_json["params"]["status"];
	for camera_status in camera_onLine_list:
		uuid = camera_status["Device"];
		status = camera_status["Online"];
		info = device_info[uuid];
		if status != True and info not in notExists:
			result.append(info);
	if len(result):
		excel_append(result,currentTime);

def excel_append(result,currentTime):
	print("离线数据:",result);
	
	# 读取文件
	rb = xlrd.open_workbook(path,formatting_info = True);
	rows = rb.sheet_by_name("square").nrows;
	# 复制 write对象
	wb = copy(rb);
	# 获取第三个sheet
	sheet = wb.get_sheet(0);
	for i in range(len(result)):
		sheet.write(i+rows,0,currentTime);
		sheet.write(i+rows,1,result[i]);
	sheet.write_merge(rows,rows+len(result)-1,0,0,currentTime,excel_style());
	wb.save(path);
# 设置excel格式
def excel_style():
	style = xlwt.XFStyle();
	font = xlwt.Font();
	# 单元格对其方式
	alignment = xlwt.Alignment();
	# 0x01 左对齐 0x02 居中对齐 0x03 右对齐
	alignment.horz = 0x02;
	# 0x00 上对齐 0x01 居中对齐 0x02 底对齐
	alignment.vert = 0x01;
	style.alignment = alignment;
	return style;
if __name__ == "__main__":
	while True:
		currentTime = time.strftime("%Y%m%d%H%M%S",time.localtime());
		print(currentTime,"定时任务执行");
		camera_status(url_login,url_camera,currentTime);
		time.sleep(10*60*3);