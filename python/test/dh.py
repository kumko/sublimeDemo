# 相机状态监测
# 
# 
from operator import pos
import requests
import json
import xlwt
import time
import os
offLine = {};
ips = ["34.33.8.11","34.33.8.12","34.33.8.13","34.33.8.14","34.33.8.15","34.33.8.17","34.33.8.18","34.33.8.19","34.33.8.20","34.33.8.21","34.33.8.24"]
headers = {};
headers["Content-Type"] = "application/json";
cookie = "DHLangCookie30=%2Fweb_lang%2FSimpChinese.txt;DhWebClientSessionID=";
# 1.beforeLogin 
def before_login(url):
	data = {
    "method": "global.login",
    "params": {
        "userName": "admin",
        "password": "",
        "clientType": "Dahua3.0-Web3.0"
    },
    "id": 10000
 	}
	result = requests.post(url=url,headers = headers,data = json.dumps(data));
	return result;
#2.login
def login(url,session):
	data = {
    "method": "global.login",
    "session": session,
    "params": {
        "userName": "admin",
        "password": "6QNMIQGe",
        "clientType": "Dahua3.0-Web3.0",
        "authorityType": "OldDigest"
    },
    "id": 10000
	}
	headers["Cookie"] = cookie + str(session);
	result = requests.post(url=url,headers = headers,data = json.dumps(data));
	return result;

# 3.查询相机信息
def camera_info(url,session):
	data ={
    "method": "LogicDeviceManager.getCameraAll",
    "params": "",
    "session": session,
    "id": 79
	} 
	headers["Cookie"] = cookie + str(session);
	result = requests.post(url=url,headers = headers,data = json.dumps(data));
	return result;
# 4.相机在离线状态
def camera_onOffLine(url,session):
	data = {
    "method": "netApp.getRemoteDeviceStatus",
    "params": "",
    "session": session,
    "id": 89
	}
	headers["Cookie"] = cookie + str(session);
	result = requests.post(url=url,headers = headers,data = json.dumps(data));
	return result;
#处理返回结果
def dealResponse(response):
	# print("请求状态码:",response.status_code);
	# print(response.text);
	json_str = response.json();
	return json_str;
result = [];

def camera():
	for ip in ips:
		url_login = "http://"+ip+"/RPC2_Login";
		url_camera = "http://"+ip+"/RPC2";
		device_info = {};
		device_camera = {}
		# 登录
		print("请求的URL=",url_login);
		response = before_login(url_login);
		session = dealResponse(response)["session"];
		login(url_login,session);
		# 查询相机详情
		response = camera_info(url_camera,session);
		camera_json = dealResponse(response);
		camera_list = camera_json["params"]["camera"];
		for camera in camera_list:
			if "DeviceID" in camera.keys():
				uuid = camera["DeviceID"];
				device = camera["DeviceInfo"];
				address = device["Address"];
				channels = device["VideoInputs"];
				if channels[0] != None :
					name = channels[0]["Name"];
				else :
					name = "";
				device_info[uuid] = address + "-" + name;
				# print(uuid,":",address);
		# 查询相机在离线状态
		response = camera_onOffLine(url_camera,session);
		camera_json = dealResponse(response);
		camera_onLine_list = camera_json["params"]["status"];
		for camera_status in camera_onLine_list:
			uuid = camera_status["Device"];
			status = camera_status["Online"];
			# print(camera_status);
			if status != True :
				result.append(device_info[uuid]); 

# 创建目录
def mkdir(path):
	isExists = os.path.exists(path);
	if not isExists:
		# 如果不存在目录，则创建
		os.makedirs(path);
	else:
		print("目录已存在");
# 导出excel表格
def excel_write(result):
	wb = xlwt.Workbook();
	ws = wb.add_sheet("离线");
	# 添加数据
	ws.write(0,0,"名称");
	ws.write(0,1,"IP");
	i = 1;
	for camera in result:
		content = camera.split("-");
		ws.write(i,0,content[1]);
		ws.write(i,1,content[0]);
		i = i + 1;
	# date = 
	
	currentTime = time.localtime();
	fileName = time.strftime("%Y%m%d%H%M%S",currentTime);
	month = time.strftime("%m",currentTime);
	day = time.strftime("%d",currentTime);
	path = "C:\\Users\\QWERT\\Desktop\\每日离线统计\\" + month + "\\" + month + day + "\\";
	mkdir(path);
	wb.save(path + fileName +".xlsx");
	print("离线统计已导出");


# 离线相机
if __name__ == "__main__" :
	print(__name__);
	camera();
	excel_write(result);

