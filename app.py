from flask import Flask, render_template
from random import choice,randint
import json

"""
A example for creating a Table that is sortable by its header
"""

#生成一些随机数据
app = Flask(__name__)
data = []
names = ('香', '草', '瓜', '果', '桃', '梨', '莓', '橘', '蕉', '苹')
for i in range(1, 1000):
    d = {}
    d['id'] = i
    d['name'] = choice(names) + choice(names) + choice(names)
    d['price'] = randint(1,10001)
    data.append(d)

# other column settings -> http://bootstrap-table.wenzhixin.net.cn/documentation/#column-options
columns = [
  {
    "field": "id", # which is the field's name of data key 
    "title": "id", # display as the table header's name
    "sortable": True,
  },
  {
    "field": "name",
    "title": "name",
    "sortable": True,
  },
  {
    "field": "price",
    "title": "price",
    "sortable": True,
  }
]

#jdata=json.dumps(data)

@app.route('/')
def index():
    return render_template("table.html",
      data=data,
      columns=columns,
      title='Flask Bootstrap Table')


app.run(debug=True)