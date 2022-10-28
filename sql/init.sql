-- 既にあるテーブルを削除
DROP TABLE IF EXISTS teacher;

-- テーブルを定義
CREATE TABLE teacher (
	-- id: 主キー
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	password TEXT,
	email TEXT,
	verified_email BOOL
	-- location_idを格納
	location INTEGER
);

-- 既にあるテーブルを削除
DROP TABLE IF EXISTS location;

-- テーブルを定義
CREATE TABLE location (
	-- id: 主キー
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	teacher_id INTEGER,
	name TEXT,
	FOREIGN KEY (teacher_id) references teacher(id)
);

-- 既にあるテーブルを削除
DROP TABLE IF EXISTS auth_token;

-- テーブルを定義
CREATE TABLE auth_token (
	-- id: 主キー
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	teacher_id INTEGER,
	token TEXT,
	expire_date DATE,
	FOREIGN KEY (teacher_id) references teacher(id)
);


