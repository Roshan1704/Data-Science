from aifc import Error

from flask import Flask, request, jsonify
import mysql.connector as con
import pymongo

api_data_sql = Flask(__name__)


@api_data_sql.route('/sql_data', methods=['GET'])
def test_api_sql():
    conn = con.connect(host="localhost", user="root", password="")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ds_db_001.students")
    return jsonify(cursor.fetchall())


@api_data_sql.route('/mongoDB_data', methods=['GET'])
def test_api_mongoDB():
    client = pymongo.MongoClient(
        "mongodb+srv://mongodb:mongodb@roshanmongodb.xeh33.mongodb.net/Ds_mongodb?retryWrites=true&w=majority")
    db = client.Ds_mongodb
    get = db.BC_Database
    data = {"result": str(list(get.find()))}
    return data

if __name__ == '__main__':
    api_data_sql.run(debug=True)
