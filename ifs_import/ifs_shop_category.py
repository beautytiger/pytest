import requests
import time


SOURCE = 'DATA_000011'


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
    data = {'dataSourceCode': SOURCE,
            'repCode': rep,
            }
    data.update(kwargs)
    print(data)
    response = requests.get(url=url, params=data)
    r = response.json()
    print(r)
    return r


@timefun
def post_response_json(rep=None, **kwargs):
    url = 'https://shengyiplus.idata.mobi/saas-api/api/portal/custom'
    data = {'dataSourceCode': SOURCE,
            'repCode': rep,
            }
    data.update(kwargs)
    response = requests.post(url=url, json=data)
    r = response.json()
    return r


def delete_all_store(mall=None):
    rep = 'REP_001236'
    response = get_response_json(rep=rep, mall=mall)
    if response.get('code') is not 0:
        return False
    if response.get('data'):
        return False
    # 删除商铺成功
    return True


def delete_all_store_category(mall=None):
    rep = 'REP_001240'
    response = get_response_json(rep=rep, mall=mall)
    if response.get('code') is not 0:
        return False
    if response.get('data'):
        return False
    # 删除商铺成功
    return True


# REP_001244
def get_store_id_by_code(code=None):
    rep = 'REP_001244'
    response = get_response_json(rep, code=code)
    if response.get('code') is not 0:
        return False
    try:
        sto_id = response.get('data', [])[0].get('id')
    except IndexError:
        return False
    if sto_id > 0:
        return sto_id
    return False


# REP_001237
# mall@@code@@name@@floor@@phone@@acc_card@@location@@icon@@logo@@image@@brief
def insert_store(**kwargs):
    # print(kwargs)
    rep = 'REP_001237'
    response = get_response_json(rep, **kwargs)
    if response.get('code') is not 0:
        return False
    try:
        sto_id = response.get('data', [])[0].get('id')
    except IndexError:
        return False
    if sto_id > 0:
        return sto_id
    return False


# REP_001238
# store@@desc
def update_store_desc(store=None, desc=None):
    rep = 'REP_001238'
    response = post_response_json(rep, store=store, desc=desc)
    if response.get('code') is not 0:
        return False
    return True


# REP_001239
# store@@category
def update_store_category(store=None, category=None):
    rep = 'REP_001239'
    response = get_response_json(rep, store=store, category=category)
    if response.get('code') is not 0:
        return False
    try:
        sto_id = response.get('data', [])[0].get('id')
    except IndexError:
        return False
    if sto_id > 0:
        return True
    return False


# REP_001241
# store@@grade@@discount
def update_store_member_discount(store=None, grade=None, discount=None):
    rep = 'REP_001241'
    response = get_response_json(rep, store=store, grade=grade, discount=discount)
    if response.get('code') is not 0:
        return False
    try:
        sto_id = response.get('data', [])[0].get('id')
    except IndexError:
        return False
    if sto_id > 0:
        return True
    return False


def main():
    with open('store.txt') as f:
        for i, j in enumerate(f.readlines()):
            print('~~~~~~~~~~', i)
            items = j.split('\t')
            # noinspection PyUnreachableCode
            (code, name, floor, phone, acc_card, location) = map(str.strip, (items[0],
                                                                                        items[1], items[4], items[5],
                                                                                        items[11], items[2]
                                                                                        ))
            storeid = get_store_id_by_code(code=code)
            if storeid is False:
                print('1\t', items)
                continue
            cate1, cate2, cate3 = map(str.strip, (items[7], items[8], items[9]))
            for cate in (cate1, cate2, cate3):
                cate = cate.strip()
                if cate:
                    print(cate)
                    if update_store_category(store=storeid, category=cate) is False:
                        print('3\t', items)
                        break


if __name__ == '__main__':
    start = time.time()
    main()
    dur = time.time() - start
    print(dur)

