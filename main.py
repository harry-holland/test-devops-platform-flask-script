from flask import Flask
from influxdb import InfluxDBClient

app = Flask(__name__)


@app.route("/")
def index():
    client = InfluxDBClient(host="influxdb", port=8086, username="admin", password="admin")
    databases = client.get_list_database()
    return "<br>".join([f"Database: {db['name']}" for db in databases])


@app.route('/devops')
def devops():
    return 'devops это круто'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7777)
