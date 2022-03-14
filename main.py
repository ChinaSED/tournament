from flask import Flask, jsonify, render_template, request
import sqlite3

app = Flask(__name__,static_folder='/')

# # 数据库查询到的数据默认是元组形式，如果想json输出需要转字典
# def dict_factory(cursor, row):
#     data = {}
#     for idx, col in enumerate(cursor.description):
#         data[col[0]] = row[idx]
#     return data
# table_name="sample_table"
# con = sqlite3.connect(table_name,check_same_thread=False)
# con.row_factory=dict_factory
# cur = con.cursor()
# tmp = cur.execute("select max(rowid) from {}".format(table_name)).fetchone()
# totalid = tmp['max(rowid)']


database = []
@app.route('/jsondata', methods=['POST', 'GET'])
def infos():
    """
    CombinedMultiDict([ImmutableMultiDict([]), ImmutableMultiDict([('pos', '31.976494, 118.824829'), ('title', '12123'), ('type', 'GUIDE'), ('article', '123123')])])   
    31.976494, 118.824829
    12123
    None
    123123
    """
    if request.method == 'POST':
        pos = request.values.get('pos').split(', ')
        title = request.values.get('title')
        type = request.values.get('type')
        article = request.values.get('article')
        data = [pos,title,type,article]
        database.append(data)

#     if request.method == 'GET':
#         info = request.values
#         limit = info.get('limit', 10)  # 每页显示的条数
#         offset = info.get('offset', 0)  # 分片数，(页码-1)*limit，它表示一段数据的起点
#         search = info.get('search','')
#     A=int(offset)+1
    return "haha"
@app.route('/')
def sheet():
    return render_template('index.html')

@app.route('/index-upload.html')
def sheet1():
    return render_template('index-upload.html')

@app.route('/index-personal.html')
def sheet2():
    return render_template('index-personal.html')
    
if __name__ == '__main__':
    app.run()
