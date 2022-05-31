from typing import Optional
from fastapi import FastAPI
import requests
app = FastAPI()

def get_token(cookies):
    headers = {
        'authority': 'www.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cookie': cookies,
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }
    try:
        get = requests.get('https://www.facebook.com/dialog/oauth?client_id=124024574287414&redirect_uri=https://www.instagram.com/accounts/signup/&&scope=email&response_type=token', headers=headers).url
        access_ = get.split('#access_token=')[1].split('&data_access')[0]
        return access_
    except:
        return 'Không Thể Get Token!'

def like_ig(id_post, cookies):
    try:
        token=cookies.split('csrftoken=')[1].split(';')[0]
        get_id = requests.post('https://www.instagram.com/p/'+id_post+'/',headers={'Authority': 'www.instagram.com','Content-Length': '0','Sec-Ch-Ua': '\"Google Chrome\";v=\"93\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"93\"','X-Ig-App-Id': '1217981644879628','Sec-Ch-Ua-Mobile': '?1','X-Instagram-Ajax': 'd26a8ffbcd2b','Content-Type': 'application/x-www-form-urlencoded','Accept': '*/*','X-Requested-With': 'XMLHttpRequest','X-Asbd-Id': '198387','X-Csrftoken': token,'Sec-Ch-Ua-Platform': '\"Android\"','Origin': 'https://www.instagram.com','Sec-Fetch-Site': 'same-origin','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://www.instagram.com/','Accept-Language': 'en-US,en;q=0.9,vi;q=0.8','Cookie': cookies}).text
        id_lam = get_id.split('content="instagram://media?id=')[1].split('"/>\n<meta')[0]
        like = requests.post('https://www.instagram.com/web/likes/'+str(id_lam)+'/like/',headers={'Authority': 'www.instagram.com','Content-Length': '0','Sec-Ch-Ua': '\"Google Chrome\";v=\"93\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"93\"','X-Ig-App-Id': '1217981644879628','Sec-Ch-Ua-Mobile': '?1','X-Instagram-Ajax': 'd26a8ffbcd2b','Content-Type': 'application/x-www-form-urlencoded','Accept': '*/*','X-Requested-With': 'XMLHttpRequest','X-Asbd-Id': '198387','X-Csrftoken': token,'Sec-Ch-Ua-Platform': '\"Android\"','Origin': 'https://www.instagram.com','Sec-Fetch-Site': 'same-origin','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://www.instagram.com/','Accept-Language': 'en-US,en;q=0.9,vi;q=0.8','Cookie': cookies,}).json()
        return {'id': id_lam, 'msg': like}
    except:
        return {id_post: 'Thất Bại'}
@app.get("/get_token")
def read_item(cookies: Optional[str] = None):
    access_token = get_token(cookies)
    return {"access_token": access_token}

@app.post("/like_ig/{id_post}")
def read_item(id_post: str, cookies: Optional[str] = None):
    like = like_ig(id_post, cookies)
    return like
