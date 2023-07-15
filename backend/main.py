from flask import Flask, g, Response, request, abort
import flask_cors
import pymysql.cursors
import time
from config import *
import re

app = Flask(__name__)
flask_cors.CORS(app)

connection = None
while connection == None:
    try:
        connection = pymysql.connect(host=db_host,
                                     user=db_user,
                                     password=db_passwd,
                                     database=db_dbName,
                                     cursorclass=pymysql.cursors.DictCursor)
    except Exception as e:
        print(e)
        time.sleep(5)

def is_valid_ip(ip):
    regex = r'^((([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]))$'
    match = re.match(regex, ip)
    return match is not None

@app.route("/register", methods = ['POST'])
def register():
    data = request.get_json()
    
    if 'name' not in data or 'ip' not in data:
        return "invalid", 400
    
    if not is_valid_ip(data['ip']):
        return "invalid IP address", 400

    with connection.cursor() as cursor:
        sql = "DELETE FROM dns_db.devices WHERE `name` = %s;"
        cursor.execute(sql, (data['name'], ))
        sql = "INSERT INTO dns_db.devices (`name`, `ip`) VALUES (%s, %s);"
        cursor.execute(sql, (data['name'], data['ip']))
    
    connection.commit()
    
    return "ok";

@app.route("/query")
def query():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM dns_db.devices;"
        cursor.execute(sql)
        result = cursor.fetchall()
        return str(result)
