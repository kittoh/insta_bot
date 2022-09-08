import json
import requests


class Instagram:
    def __init__(self):
        self.session = None

    def load(self, session):
        self.session = session

    def login(self, username: str, password: str) -> dict:
        from datetime import datetime

        url = "https://www.instagram.com/accounts/login/"
        login_url = "https://www.instagram.com:443/accounts/login/ajax/"

        time = int(datetime.now().timestamp())

        response = requests.get(url)
        csrf = response.cookies['csrftoken']

        data = {
            "username": username,
            "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{time}:{password}",
            "queryParams": "{}",
            "optIntoOneTap": "false",
            "stopDeletionNonce": '',
            "trustedDeviceRecords": "{}"
        }

        headers = {
            "Sec-Ch-Ua": "\"Chromium\";v=\"105\", \"Not)A;Brand\";v=\"8\"",
            "X-Ig-App-Id": "936619743392459",
            "X-Ig-Www-Claim": "0",
            "Sec-Ch-Ua-Mobile": "?0",
            "X-Instagram-Ajax": "2c4a166c736d",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "X-Requested-With": "XMLHttpRequest",
            "X-Asbd-Id": "198387",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.54 Safari/537.36",
            "X-Csrftoken": csrf,
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Origin": "https://www.instagram.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://www.instagram.com/",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9"
        }

        login_response = requests.post(login_url, headers=headers, data=data)

        login_response_json = json.loads(login_response.text)
        print(json.dumps(login_response_json))

        if login_response_json["authenticated"]:
            print("login successful")
            cookies = login_response.cookies
            cookie_jar = cookies.get_dict()
            csrf_token = cookie_jar['csrftoken']
            print("csrf_token: ", csrf_token)
            session_id = cookie_jar['sessionid']
            print("session_id: ", session_id)

        else:
            print("login failed ", response)
