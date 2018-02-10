import requests
import time
import random
import string


def timefun(func):

    def wrap(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        dur = time.time() -start
        print(dur)
        return result
    return wrap


@timefun
def get_response_json(rep=None, **kwargs):
    url = 'https://shengyiplus.idata.mobi/saas-api/api/portal/custom'
    data = {'dataSourceCode': 'DATA_000005',
            'repCode': rep,
            }
    data.update(kwargs)
    response = requests.get(url=url, params=data)
    r = response.json()
    # print(r)
    return r


@timefun
def post_response_json(rep=None, **kwargs):
    url = 'https://shengyiplus.idata.mobi/saas-api/api/portal/custom'
    data = {'dataSourceCode': 'DATA_000005',
            'repCode': rep,
            }
    data.update(kwargs)
    response = requests.post(url=url, json=data)
    r = response.json()
    return r


def saas_benchmark(string=None):
    rep = 'REP_001243'
    response = get_response_json(rep=rep, str=string)
    if response.get('code') is not 0:
        return False
    if response.get('data'):
        return True
    return False


def get_store_category(mall=None):
    rep = 'REP_001225'
    response = get_response_json(rep=rep, mall=mall)
    if response.get('code') is not 0:
        return False
    if response.get('data'):
        return True
    return False



def gen_random_string(min_len=1, max_len=20):
    """生成随机字符串"""
    s = ''
    for i in range(random.randint(min_len, max_len)):
        s += random.choice(string.ascii_letters)
    return s

def main(loops=100):
    for i in range(loops):
        # s = gen_random_string()
        # saas_benchmark(string=s)
        get_store_category(mall=1)


if __name__ == '__main__':
    start = time.time()
    main()
    dur = time.time() - start
    print(dur)

