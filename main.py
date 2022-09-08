from features import Instagram
import secrets


def main():
    ig_user = "jyusaka"
    ig_pwd = secrets.password

    bot = Instagram()
    bot.login(ig_user, ig_pwd)


if __name__ == "__main__":
    main()
