# ライブラリから使いたい関数・クラスをimport
from flask import Flask, render_template, request, abort, redirect, url_for, g
import sqlite3

# /application/から関数をimportする
from application.location import get_teacher_locations, get_teacher_location_states, register_location_state, update_teacher_location
from application.account import create_teacher, login_teacher, auth_teacher_token

# Flaskアプリケーションの作成
app = Flask(__name__)

# データベースの接続
@app.before_request
def handle_before_request():
	g.database = sqlite3.connect("db/todo.db")

# データベースの接続解除
@app.teardown_request
def handle_teardown_request(exception):
	g.database.close()

# http://URL/ にGETリクエストが送信されるときに、この関数が処理される
@app.get("/")
def index():
	return render_template("index.html")

# もしターミナルから直接呼ばれたなら
if __name__ == '__main__':
	# サーバーを立ち上げる
	app.run(debug=True)
