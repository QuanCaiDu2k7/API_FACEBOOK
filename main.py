from typing import Optional
from fastapi import FastAPI
import requests
import random
def random_id(length):
    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    id = ''
    for i in range(0,length,2):
        id += random.choice(number)
        id += random.choice(alpha)
    return id

def generateImei() :
        return str(str(str(str(str(str(str(str(generateRandomString(8)) + '-') + str(generateRandomString(4))) + '-') + str(generateRandomString(4))) + '-') + str(generateRandomString(4))) + '-') + str(generateRandomString(12));  

def generateRandomString(length = 20) :
    characters = '0123456789abcdef'
    charactersLength = len(characters)
    randomString = ''
    i = 0
    while ( i < length ) :
        randomString += characters[random.randint(0, charactersLength - 1)]
        i+=1
    return randomString
app = FastAPI()

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
}

def tiki(phone):
    if phone == "0395524153" or phone == "84395524153":
        return "Spam Số Tao Làm Lồn À!"
    else:
        try:
            return "Mua Soucre Api Liên Hệ: Nguyễn Minh Quân" 
        except:
            return "Lỗi Không Xác Định!"

def grab_food(phone):
    if phone == "0395524153" or phone == "84395524153":
        return "Spam Số Tao Làm Lồn À!"
    else:
        try:
            return "Mua Soucre Api Liên Hệ: Nguyễn Minh Quân" 
        except:
            return "Lỗi Không Xác Định!"
    
def bach_hoa_xanh(phone):
    if phone == "0395524153" or phone == "84395524153":
        return "Spam Số Tao Làm Lồn À!"
    else:
        try:
            return "Mua Soucre Api Liên Hệ: Nguyễn Minh Quân" 
        except:
            return "Lỗi Không Xác Định!" 
    
def meta_vn(phone):
    if phone == "0395524153" or phone == "84395524153":
        return "Spam Số Tao Làm Lồn À!"
    else:
        try:
            return "Mua Soucre Api Liên Hệ: Nguyễn Minh Quân" 
        except:
            return "Lỗi Không Xác Định!"    

def elines(phone):
    if phone == "0395524153" or phone == "84395524153":
        return "Spam Số Tao Làm Lồn À!"
    else:
        try:
            return "Mua Soucre Api Liên Hệ: Nguyễn Minh Quân" 
        except:
            return "Lỗi Không Xác Định!"  
        
def gojoy(phone):
    if phone == "0395524153" or phone == "84395524153":
        return "Spam Số Tao Làm Lồn À!"
    else:
        try:
            return "Mua Soucre Api Liên Hệ: Nguyễn Minh Quân" 
        except:
            return "Lỗi Không Xác Định!" 
        
def vntrip(phone):
    if phone == "0395524153" or phone == "84395524153":
        return "Spam Số Tao Làm Lồn À!"
    else:
        try:
            return "Mua Soucre Api Liên Hệ: Nguyễn Minh Quân" 
        except:
            return "Lỗi Không Xác Định!" 

def nhaphang247(phone):
    if phone == "0395524153" or phone == "84395524153":
        return "Spam Số Tao Làm Lồn À!"
    else:
        try:
            return "Mua Soucre Api Liên Hệ: Nguyễn Minh Quân" 
        except:
            return "Lỗi Không Xác Định!" 
        
@app.post("/tiki")
def read_item(phone: Optional[str] = None):
    done = tiki(phone)
    return done

@app.post("/grab-food")
def read_item(phone: Optional[str] = None):
    done = grab_food(phone)
    return done

@app.post("/bach-hoa-xanh")
def read_item(phone: Optional[str] = None):
    done = bach_hoa_xanh(phone)
    return done

@app.post("/meta-vn")
def read_item(phone: Optional[str] = None):
    done = meta_vn(phone)
    return done

@app.post("/elines")
def read_item(phone: Optional[str] = None):
    done = elines(phone)
    return done

@app.post("/gojoy")
def read_item(phone: Optional[str] = None):
    done = gojoy(phone)
    return done

@app.post("/vntrip")
def read_item(phone: Optional[str] = None):
    done = vntrip(phone)
    return done

@app.post("/nhap-hang-247")
def read_item(phone: Optional[str] = None):
    done = nhaphang247(phone)
    return done


