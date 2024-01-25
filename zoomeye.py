#/usr/bin/python
# Env: python3
# Author: 月金剑客

from colorama import *

import colorama
from check_token import check_token
from get_token import get_yourtoken
init(autoreset=True)
import requests
import json
import argparse

def title():
    print('\n')
    print(colorama.Fore.GREEN + '+-------------------------------------------------------------+')
    print(colorama.Fore.GREEN + '+                         zoomeye爬取                         +')
    print(colorama.Fore.GREEN + '+-------------------------------------------------------------+')
    print(colorama.Fore.GREEN + '+-------------------------------------------------------------+')
    print(colorama.Fore.BLUE + '+ writer:                 yuejinjianke                        +')
    print('\n')
    print('\n')
    print('\n')

class zoomeye_query():
    def query(self, query, page, num, facet, file):
        gettoken = check_token()
        random_token = get_yourtoken()
        headers={
            'Authorization': "JWT " + gettoken.check_yourtoken(),
            'User-Agent': random_token.random_useragent()
        }
        api = "https://api.zoomeye.org/host/search"
        index = 0

        while True:
            try:
                if index == num:
                    break
                print(colorama.Fore.YELLOW + f"正在爬取第{page}页数据：")
                resp = requests.get(url=api,headers=headers,verify=False,params={"query": query,'page': page,'facet': facet}).text
                json_res = json.loads(resp)["matches"]
                count = 1
                for i in json_res:
                    print(f"[{count}] "+ i['ip'] + ":" + str(i['portinfo']['port']))
                    record = i['ip'] + ":" + str(i['portinfo']['port'])
                    with open(file,'a') as fp:
                        fp.writelines(record+"\n")
                        count += 1



            except Exception as e:
                print(colorama.Fore.RED + "请看看是不是到达最大限度数目了")




if __name__ == '__main__':
    title()
    parser = argparse.ArgumentParser("zoomeyetool made by yuejinjianke")

    parser.add_argument(
        '-q','--query',
        metavar='',required=True,type=str,
        help='please input query string. eg: shiro'
    )

    parser.add_argument(
        '-p','--page',
        metavar='',required=False,type=int,default=1,
        help='please input start page. eg: 2'
    )

    parser.add_argument(
        '-n','--num',
        metavar='',required=False,type=int,default=1,
        help='please input max page.eg: 98'
    )

    parser.add_argument(
        '-f','--facet',
        metavar='',required=False,type=str,
        help='Please input covariance item. eg: server'
    )

    parser.add_argument(
        '-o', '--file', required=False,
        metavar='', type=str, default='output.txt',
        help='Please input output file path. eg: output.txt'
    )

    args = parser.parse_args()
    zoomeye_running = zoomeye_query()
    zoomeye_running.query(args.query, args.page, args.num, args.facet, args.file)
    pass