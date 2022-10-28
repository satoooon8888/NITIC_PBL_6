#!/bin/bash -ex

sqlite3 db/todo.db < sql/init.sql

python3 server.py
