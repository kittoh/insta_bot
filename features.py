import json
import requests


class Instagram:
    def __init__(self):
        self.session = None

    def load(self, session):
        self.session = session

    def login(self, username: str, password: str) -> dict:
        from datetime import datetime
        import requests
        
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

        return login_response
        
    def check_profile(self, username: str):
        import requests

        profile_url = f"https://i.instagram.com:443/api/v1/users/web_profile_info/?username={username}"
        # cookies = {"mid": "YxVv1QALAAFwKuD67IYk4CLsx8I9", "ig_did": "83D675D0-7C1D-43AF-B67E-11190FB9C6B7", "ig_nrcb": "1", "datr": "3JEVY-p_EKDMzm3XICT4L3Tc", "csrftoken": "YBaqFCk5FhIOb3476tTeqKDxiNbPWbR8", "ds_user_id": "55121016812", "sessionid": "55121016812%3AHXzL1rFNs3s5Ho%3A24%3AAYdXGYya2Ml2ntc1v123dpSpUXPc1B64cOyyOWXXMg", "rur": "\"NCG\\05455121016812\\0541694239634:01f715097f48fa4251466c618753a8c0a749f7de1cc4ab746cc0a148c3c358ce0901f06c\""}
        headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"105\", \"Not)A;Brand\";v=\"8\"", "X-Ig-App-Id": "936619743392459", "X-Ig-Www-Claim": "hmac.AR0Cu34eswjcCnfO2ilC63PifoFwll46_XxBB3G4B2VCjwlB", "Sec-Ch-Ua-Mobile": "?0", "X-Instagram-Ajax": "1006170369", "Accept": "*/*", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.54 Safari/537.36", "X-Asbd-Id": "198387", "X-Csrftoken": "YBaqFCk5FhIOb3476tTeqKDxiNbPWbR8", "Sec-Ch-Ua-Platform": "\"Windows\"", "Origin": "https://www.instagram.com", "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://www.instagram.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
        
        profile_response = requests.get(profile_url, headers=headers)
        profile_response_json = profile_response.json()
        
        user_id = profile_response_json["data"]["user"]["id"]
        
        return user_id
        
        
    def get_followers(self, user_id: int, csrftoken, sessionid):
        import requests
        
        followers_url = f"https://i.instagram.com:443/api/v1/friendships/{user_id}/followers/?count=12&search_surface=follow_list_page"
        
        cookies = {
            "csrftoken": csrftoken, 
            "sessionid": sessionid,
        }
        headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"105\", \"Not)A;Brand\";v=\"8\"", "X-Ig-App-Id": "936619743392459", "X-Ig-Www-Claim": "hmac.AR0Cu34eswjcCnfO2ilC63PifoFwll46_XxBB3G4B2VCjwlB", "Sec-Ch-Ua-Mobile": "?0", "X-Instagram-Ajax": "1006170369", "Accept": "*/*", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.54 Safari/537.36", "X-Asbd-Id": "198387", "X-Csrftoken": "YBaqFCk5FhIOb3476tTeqKDxiNbPWbR8", "Sec-Ch-Ua-Platform": "\"Windows\"", "Origin": "https://www.instagram.com", "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://www.instagram.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
        
        followers_response = requests.get(followers_url, headers=headers, cookies=cookies)
        followers_response_json = followers_response.json()
        followers = json.dumps(followers_response_json, indent=4)
        
        return followers
        