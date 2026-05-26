from psycopg2 import connect
from flask import Flask
from configparser import ConfigParser


app = Flask(__name__)

def get_db_config(db_option):
        config = ConfigParser()
        config.read('/srv/app/conf/web.conf')
        try:
                result = config.get("database", db_option)
        except configparser.NoSectionError:
                print ('Cannot get {}. There is no such section or config file is unavailable/does not exist').format(db_option)
                exit ()
        return result


def get_db_time():
        conn = connect(f"host= {get_db_config('db_host')} dbname={get_db_config('db_name')} user={get_db_config('db_user')} password={get_db_config('db_password')}")
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute('SELECT current_user;;')
        return cur.fetchone()


text = f"<h1 style='color:blue'>Hello there!</h1> Everything is OK! DB Query was completed by {get_db_time()[0]} user"



@app.route("/")


def hello():
    return text

if __name__ == "__main__":
    app.run(host='0.0.0.0')