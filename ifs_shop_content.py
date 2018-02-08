import requests


code_map = {}


def update_store_desc_by_code(code, desc):
    url = 'https://shengyiplus.idata.mobi/saas-api/api/portal/custom'
    params = {'dataSourceCode': 'DATA_000005',
              'repCode': 'REP_001230',
              'code': code,
              'desc': desc,
              }
    response = requests.get(url=url, params=params)
    r = response.json()
    try:
        rec_id = r.get('data', [])[0].get('id')
    except IndexError:
        return False
    if rec_id > 0:
        return True
    return False


def main():

    with open('store_code_link.csv') as s:
        for code in s.readlines():
            code = code.split(',')
            lcode = code[0]
            scode = code[1].lower()
            code_map[scode] = lcode

    with open('shoplist.csv') as f:
        for i in f.readlines():
            items = i.split('|')
            scode = items[1][1:-1].lower()
            if '&' in scode:
                scode = scode.split('&')[0].strip()
            if '-' in scode:
                scode = scode.split('-')[0].strip()
            if ',' in scode:
                scode = scode.split(',')[0].strip()
            shop_code = code_map.get(scode)
            desc = items[4][1:-1].strip()
            if not shop_code:
                print('1\t', scode)
            else:
                result = update_store_desc_by_code(shop_code, desc)
                if result is False:
                    print('2\t', scode)


if __name__ == '__main__':
    import time
    start = time.time()
    main()
    dur = time.time() - start
    print(dur)

