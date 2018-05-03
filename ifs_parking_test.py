import requests

url1 = "https://wechatapp.cdifs.cn/wechat/ifs/coupons"

# this script used in local network of IFS
auth_url = "http://172.28.6.234:8088/wechat/ifs/authenticate"
coup_url = "http://172.28.6.234:8088/wechat/ifs/coupons"


def post(url):
    headers = {'Content-Type': 'application/json', 'authorization': 'token 0HVL2FwLGRMAro4rPutvNbH63y7qkcZVYtstTMq4kDEAPchCpJpY6Rgk7VoaDxWlvdfDb3HgXJd2hUug2L2p0lFSQnDcoDoCknuOKrzicm7Ruqwki6uie1G8Amra80hE'}
    data = requests.post(url, headers=headers)
    return data.json()


if __name__ == "__main__":
    resp = requests.post(auth_url, json={"app_id": "1", "app_secret": "1"})
    jr = resp.json()
    print(jr)
    token = jr["token"]

    res = requests.post(
        coup_url,
        headers={'authorization': "token " + token},
        json={
            "method": "usecoupon_parking_ifs",
            "conditions": {
                "coupon_no": "ZH805020000001",
                "ticket": "5347645804116744432601202898"
        }})
    print(res.json())
