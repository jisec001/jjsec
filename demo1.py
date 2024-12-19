import requests
from lxml import etree

''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=--------ok4o88lom'
}
for i in range(0,225,25):
    url = f'https://movie.douban.com/top250?start={i}&filter='
    response = requests.get(url,headers=headers)
    tree = etree.HTML(response.text)
    movies = tree.xpath('//div[@class="article"]/ol/li/div')
    for i in movies:
        image = i.xpath('./div/a/img/@src')
        title = i.xpath('./div[2]/div/a/span[1]/text()')
        p = i.xpath('./div[2]/div[2]/div/span[4]/text()')
        print(image,title,p)
        url = ''.join(image)
        response1 = requests.get(url,headers=headers).content
        filename = f"{''.join(title)}.png"
        with open(filename,'wb') as f:
            f.write(response1)


