from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import certifi  #만약 몽고 디비 돌릴때 문제가 없으셨다면 해당 줄은 주석 처리 하세요.
client = MongoClient('mongodb+srv://test:sparta@cluster0.0mzan.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta
app = Flask(__name__)

@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/')
def home_page():
    return render_template('friends.html')

@app.route('/nav')
def nav_page():
    name = request.args.get('name')
    print(name)
    return render_template(name + '.html')

@app.route('/chat')
def chat_page():
    name = request.args.get('name')
    return render_template('chat_' + name + '.html')

@app.route("/send_comment", methods=["POST"])
def web_guestbook_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    page_name_receive = request.form['page_name_give']
    timestamp_receive = request.form['timestamp_give']
    doc={"name":name_receive, "comment":comment_receive, "page_name":page_name_receive, "timestamp":timestamp_receive}
    db.guestbook.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})
#alt+j = ctrl + d

# http://localhost:5000/name?name=seungtae
# http://localhost:5000/name?name=gunhee
@app.route("/get_comments", methods=["GET"])
def web_mars_get():
    # name = request.args.get('name')
    comments_list = list(db.guestbook.find({}, {'_id': False}))
    return jsonify({'comments': comments_list})

@app.route("/delete_comment", methods=["DELETE"])
def del_comment():
    print(request.form)
    # name_receive = request.form['name_receive']
    # comment_receive = request.form['comment_receive']
    # page_name_receive = request.form['page_name_receive']
    timestamp_recieve = request.form['timestamp_receive']
    # doc = {"name": name_receive, "comment": comment_receive, "page_name": page_name_receive, "timestamp":timestamp_receive}
    doc = {"timestamp":timestamp_recieve}
    db.guestbook.delete_one(doc)
    return jsonify({'msg': '삭제 완료!'})

# @app.route("/update_comment", methods=["PATCH"])
# def update_comment():
#     name_receive = request.form['name_give']
#     comment_receive = request.form['comment_give']
#     page_name_receive = request.form['page_name_give']
#     doc = {"name": name_receive, "comment": comment_receive, "page_name": page_name_receive}
#     db.guestbook.upsert()
#     return jsonify({'msg': '수정 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)