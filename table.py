from flask import Flask, jsonify, render_template, request
import sqlite3

app = Flask(__name__)

# 数据库查询到的数据默认是元组形式，如果想json输出需要转字典
def dict_factory(cursor, row):
    data = {}
    for idx, col in enumerate(cursor.description):
        data[col[0]] = row[idx]
    return data
table_name="sample_table"
con = sqlite3.connect(table_name,check_same_thread=False)
con.row_factory=dict_factory
cur = con.cursor()
tmp = cur.execute("select max(rowid) from {}".format(table_name)).fetchone()
totalid = tmp['max(rowid)']

@app.route('/jsondata', methods=['POST', 'GET'])
def infos():
    lastsearch = ''
    lasttotal = 0
    # if request.method == 'POST':
    #     print('post')
    if request.method == 'GET':
        info = request.values
        limit = info.get('limit', 10)  # 每页显示的条数
        offset = info.get('offset', 0)  # 分片数，(页码-1)*limit，它表示一段数据的起点
        search = info.get('search','')
    A=int(offset)+1
    B=(int(offset) + int(limit))
    #没有数据库筛选时，用 selector = con.select(select="*", table_name=table_name, where="id BETWEEN "+str(A)+" AND "+str(B))
    if search=='':
        selector = "SELECT * FROM {} WHERE (ID BETWEEN {} AND {})".format(table_name,A,B)
        total = totalid
    else:
        if search == lastsearch:
            total = lasttotal
        else:
            selector = "SELECT COUNT(NAME) AS TOTAL FROM {} WHERE (name LIKE '%{}%')".format(table_name,search)
            tmp = cur.execute(selector).fetchone()
            total = tmp['TOTAL']
            lasttotal , lastsearch  = total,search
        selector = "SELECT * FROM {} WHERE (name LIKE '%{}%') LIMIT {} OFFSET {}".format(table_name,search,limit,offset)
    result = cur.execute(selector).fetchmany(100)
    return jsonify({'total': total, 'rows': result})
    # return jsonify({'total': len(data), 'rows': data[int(offset):(int(offset) + int(limit))]})
    # 注意total与rows是必须的两个参数，名字不能写错，total是数据的总长度，rows是每页要显示的数据,它是一个列表
    # 前端根本不需要指定total和rows这俩参数，他们已经封装在了bootstrap table里了

@app.route('/')
def sheet():
    return render_template('test.html')

if __name__ == '__main__':
    app.run()
