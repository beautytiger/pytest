import requests
import time


SOURCE = 'DATA_000005'


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


# mall@@code@@name@@phone@@acc_card@@location
def insert_store(**kwargs):
    # print(kwargs)
    rep = 'REP_001245'
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
    mallid = 1
    imurl = 'https://shengyiplus.idata.mobi/saas_images/ifs/store/'
    delete_all_store(mall=mallid)
    delete_all_store_category(mall=mallid)
    with open('20180211.txt') as f:
        for i, j in enumerate(f.readlines()):
            print('~~~~~~~~~~', i)
            items = j.split('\t')
            # if len(items) != 14:
            #     print(items)
            # continue
            # noinspection PyUnreachableCode
            (code, name, phone, acc_card, location) = map(str.strip, (items[0], items[1], items[4], items[9], items[2]))
            if acc_card == '是':
                acc_card = 1
            else:
                acc_card = 0
            # https://shengyiplus.idata.mobi/saas_images/ifs/store/1908c5ab-0572-460f-8ded-9aac568b7d3c.png
            icon = imurl + code + '-' + name + '.jpg'
            logo = icon
            image = imurl + name + '.jpg'
            # mall@@code@@name@@phone@@acc_card@@location
            storeid = insert_store(mall=mallid, code=code, name=name, phone=phone, acc_card=acc_card, location=location)
            if storeid is False:
                print('1\t', items)
                continue
            cate1, cate2, cate3, cate4 = map(str.strip, (items[5], items[6], items[7], items[8]))
            for cate in (cate1, cate2, cate3, cate4):
                cate = cate.strip()
                if cate:
                    if update_store_category(store=storeid, category=cate) is False:
                        print('3\t', items)
                        break
            try:
                silver, sp_silver, gold, diamond = map(str.strip, (items[10], items[11], items[12], items[13]))
                if silver and silver != '/':
                    if update_store_member_discount(store=storeid, grade='银卡', discount=silver) is False:
                        print('4\t', items)
                        break
                if sp_silver and silver != '/':
                    if update_store_member_discount(store=storeid, grade='特选银卡', discount=sp_silver) is False:
                        print('4\t', items)
                        break
                if gold and silver != '/':
                    if update_store_member_discount(store=storeid, grade='金卡', discount=gold) is False:
                        print('4\t', items)
                        break
                if diamond and silver != '/':
                    if update_store_member_discount(store=storeid, grade='钻石卡', discount=diamond) is False:
                        print('4\t', items)
                        break
            except Exception:
                continue


if __name__ == '__main__':
    start = time.time()
    main()
    dur = time.time() - start
    print(dur)

