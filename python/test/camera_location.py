from operator import pos
import requests
import json
import xlrd
import time
import os

path = "C:\\Users\\QWERT\\Desktop\\大华经纬度-开发区.xlsx";
url = "http://34.33.8.8/emap/device_saveDevsLocation.action?systime=1600410994436&";

def camera_location():
	# 读取文件
	rb = xlrd.open_workbook(path,formatting_info = True);
	sheet = rb.sheet_by_name('经纬度');

	for i in range(sheet.nrows):
		if i != 0:
			row = sheet.row_values(i)
			deviceCode = row[1];
			channelNum = row[2];
			lon = row[3];
			lan = row[4];
			jsonStr = "jsonStr=%5B%7B%22mapId%22%3Anull%2C%22type%22%3A%220%22%2C%22channelClass%22%3Anull%2C%22deviceCode%22%3A%22"+str(deviceCode)+"%22%2C%22channelNum%22%3A"+str(channelNum)+"%2C%22mapX%22%3A"+str(lon)+"%2C%22mapY%22%3A"+str(lan)+"%7D%5D&userId=1";
			result = requests.get(url + jsonStr);
			print(result);
camera_location();