import requests
import json
from tinydb import TinyDB, Query
from tinydb.table import Document
import datetime

class DB:
    def __init__(self, path) -> None:
        self.db = TinyDB(path, indent=4, separators=(',', ': '))
        self.query = Query()
        self.product = self.db.table('products')
        self.base_url = "https://fastfoodbackend.pythonanywhere.com/"

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
    
    def add_product_to_db(self, pk:int, user_id:int):
        request = requests.get(self.base_url+f"product/list/{pk}/")
        if request.status_code == 200:
            if self.product.get(doc_id=int(user_id)):
                self.product.remove(doc_ids=[int(user_id)])
            data = request.json()
            products = data['products']
            n = 1
            for product in products:
                add_product = {
                    'id':product['id'],
                    'name':product['name'],
                    'price':product['price'],
                    'img':product['img'],
                }
                self.product.upsert(Document({n:add_product}, doc_id=user_id))
                n += 1
            data = {'OK':'request'}
        else:
            data = {'error':'request not fount'}
        return data
    
    def get_product_detail(self, user_id:int):
        products = self.product.get(doc_id=int(user_id))
        return products['1'],1
        
    def next_product(self, user_id:int, n:int):
        products = self.product.get(doc_id=int(user_id))
        if products.get(str(n+1)):
            return products[str(n+1)],n+1
        else:
            return products['1'],1
        
    def back_product(self, user_id:int, n:int):
        products = self.product.get(doc_id=int(user_id))
        if products.get(str(n-1)):
            return products[str(n-1)],n-1
        else:
            max_n = len(products)
            return products[str(max_n)],max_n


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
        
    

# db = DB('db.json')
# data = {
#     "name":"test",
#     "phone":"123456789",
#     "address":"test",
#     "product":1,
#     'count':1,
# }
# print(db.back_product(2019100, 1))


# print(db.create_order(data))
# # print(db.create_order(data))
