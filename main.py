from features import Instagram
import secrets


def main():
    ig_user = "jyusaka"
    ig_pwd = secrets.password

    bot = Instagram()
    
    # bot login to get cookies
    response_json = bot.login(ig_user, ig_pwd)
    cookies = response_json.cookies
    cookie_jar = cookies.get_dict()
    csrftoken = cookie_jar['csrftoken']
    sessionid = cookie_jar['sessionid']
    
    # gets user id via user profile
    check_user = "kxttxh"
    user_id = bot.check_profile(check_user)
    
    # get followers using user_id
    followers = bot.get_followers(user_id, csrftoken,sessionid)
    print(followers)


if __name__ == "__main__":
    main()
