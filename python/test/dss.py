from operator import pos
import requests
import json
import xlwt
import time
import os
path = "C:\\Users\\QWERT\\Desktop\\大华经纬度.xlsx";
url_info = "http://34.33.8.8/emap/proxyTree_linkGet.action?id=001001&type=01;00_1,00_7,00_6;01_1&uId=1&searchKey=&act=&curCount=";
url_location = "http://34.33.8.8/emap/device_findAllAreaDevices.action?systime=1600392326546&types=0,2&deviceCode=1000539,1000538,1000537,1000522,1000516,1000515,1000513,1000511,1000510,1000509,1000508&channelClass=0";
camera_details = {};
camera_noLocation = {};
#处理返回结果
def dealResponse(response):
	# print("请求状态码:",response.status_code);
	# print(response.text);
	json_str = response.json();
	return json_str;

def camera_no_lacation():
	index = 400;
	while index <= 600:
		result = requests.get(url_info + str(index));
		json_str = dealResponse(result);
		for camera in json_str:
			if "deviceType" in camera.keys():
				camera_details[camera["name"]] = camera["id"];
		index += 50;
	result = requests.get(url_location);
	cameras = dealResponse(result)["data"];
	for camera in cameras:
		if camera["name"]  in camera_details.keys():
			del camera_details[camera["name"]]
def camera_export():
	wb = xlwt.Workbook();
	ws = wb.add_sheet("经纬度");
	# 添加数据
	ws.write(0,0,"名称");
	ws.write(0,1,"设备编码");
	ws.write(0,2,"通道号");
	i = 1;
	for key,value in camera_details.items():
		channel_info = value;
		list = channel_info.split("$");
		ws.write(i,0,key);
		ws.write(i,1,list[0]);
		ws.write(i,2,list[3]);
		i = i+1;
	wb.save(path);
camera_no_lacation();
# camera_export();
for key,value in camera_details.items():
	print(key,":",value);