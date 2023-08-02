import requests
import json
from tinydb import TinyDB, Query
from tinydb.table import Document
import datetime

class DB:
    def __init__(self, path) -> None:
        self.db = TinyDB(path)
        self.query = Query()
        self.base_url = "http://127.0.0.1:8000/"

    def get_category_list(self):
        request = requests.get(self.base_url+"category/list/")
        if request.status_code == 200:
            data = request.json()
        else:
            data = {"error":"request not fount"}
        return data
    
    def get_category_detail(self, pk:int):
        request = requests.get(self.base_url+f"category/detail/{pk}/")
        if request.status_code == 200:
            data = request.json()
        else:
            data = {'error':'request not fount'}
        return data
    
    def get_subcategory_list(self, pk:int):
        request = requests.get(self.base_url+f"subcategory/list/{pk}/")
        if request.status_code == 200:
            data = request.json()
        else:
            data = {'error':'request not fount'}
        return data
    
    def get_subcategory_detail(self, pk:int):
        request = requests.get(self.base_url+f"subcategory/detail/{pk}/")
        if request.status_code == 200:
            data = request.json()
        else:
            data = {'error':'request not fount'}
        return data

    def get_product_list(self, pk:int):
        request = requests.get(self.base_url+f"product/list/{pk}/")
        if request.status_code == 200:
            data = request.json()
        else:
            data = {'error':'request not fount'}
        return data
    
    def get_product_detail(self, pk:int):
        request = requests.get(self.base_url+f"product/detail/{pk}/")
        if request.status_code == 200:
            data = request.json()
        else:
            data = {'error':'request not fount'}
        return data

    def create_order(self, data:dict):
        now = datetime.datetime.now()
        hour = now.hour + 1
        minute = now.minute
        new_time = datetime.datetime(now.year, now.month, now.day, hour, minute)
        data['hour'] = new_time
        request = requests.post(self.base_url+"order/create/", data=data)
        if request.status_code == 201:
            data = request.json()
        else:
            data = {'error':'request not fount'}
        return data
        
    

db = DB('db.json')
# data = {
#     "name":"test",
#     "phone":"123456789",
#     "address":"test",
#     "product":1,
#     'count':1,
# }


# print(db.create_order(data))
# # print(db.create_order(data))
