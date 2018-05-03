import requests

url1 = "https://wechatapp.cdifs.cn/wechat/ifs/coupons"
url2 = "http://172.28.6.234:8088/wechat/ifs/coupons"


def post(url):
    headers = {'Content-Type': 'application/json', 'authorization': 'token 0HVL2FwLGRMAro4rPutvNbH63y7qkcZVYtstTMq4kDEAPchCpJpY6Rgk7VoaDxWlvdfDb3HgXJd2hUug2L2p0lFSQnDcoDoCknuOKrzicm7Ruqwki6uie1G8Amra80hE'}
    data = requests.post(url, headers=headers)
    return data.json()


if __name__ == "__main__":
    print(post(url1))
    print(post(url2))