import os,time
import colorama
from get_token import get_yourtoken

class check_token():
    def check_yourtoken(self):
        if not os.path.isfile("access_token.txt"):
            print(colorama.Fore.RED + "[-] 检测不到access_token.txt上的token，正在登陆")
            getyourToken = get_yourtoken()
            getyourToken.login("https://api.zoomeye.org/user/login")
            time.sleep(2)
            if not os.path.isfile('access_token.txt'):
                print(colorama.Fore.RED + "[-] 登陆超时，请确定你的账号密码是否有用")
            else:
                with open("access_token.txt",'r') as fp:
                    token = fp.readline()
                    return token


        else:
            try:
                with open("access_token.txt", 'r') as fp:
                    token = fp.readline()
                    return token
            except Exception as e:
                print(colorama.Fore.RED + "[-] api失效，正在重新登陆")
                os.remove("access_token.txt")
                getyourToken = get_yourtoken()
                getyourToken.login("https://api.zoomeye.org/user/login")
                time.sleep(2)
                if not os.path.isfile('access_token.txt'):
                    print(colorama.Fore.RED + "[-] 登陆超时，请确定你的账号密码是否有用")
                else:
                    with open("access_token.txt", 'r') as fp:
                        token = fp.readline()
                        return token