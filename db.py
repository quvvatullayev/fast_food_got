import requests
import json
from tinydb import TinyDB, Query
from tinydb.table import Document

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
    

db = DB('db.json')
print(db.get_category_detail(1))
