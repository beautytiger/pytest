import MySQLdb
import json


db = MySQLdb.connect(
    host='localhost',
    user='wxmall',
    passwd='wxmall',
    db='shimao',
    charset='utf8mb4',
)

cur = db.cursor()
cur.execute("""select id, user_id, game, date, data from game_usergamerecords order by id;""")
# game_result_data
grd = cur.fetchall()
with open('coupon_data.csv', 'w') as f:
    for row in grd:
        output = []
        # print(row)
        row_id, user_id, game_name, game_time, game_data = row

        # handle game result first
        game_json = json.loads(game_data)
        game_result = game_json['result']['status']
        if game_result != 'success':
            continue

        openid = game_json['game']['user']['openid']
        coupon_name = game_json['result']['message']['coupon']['name']

        output.extend([row_id, user_id, openid, game_name, coupon_name, game_time])

        cur.execute("""select id, phone, membercode, cardnum, `name`, nickname, plateno 
            from mc_wechatbindopencard 
            where openid_id = %d"""
            % user_id)
        # member info
        member = cur.fetchone()
        member_row_id, phone, membercode, cardnum, name, nickname, plateno = member

        output.extend([member_row_id, phone, membercode, cardnum, name, nickname, plateno, '\n'])

        f.write(','.join(map(str, output)))
