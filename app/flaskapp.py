from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    import psycopg2
    conn = psycopg2.connect(
        user="user",
        password="passwd",
        host="db",
	dbname="test"
    )
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE increment (d text)''')
    except Exception as e:
        print('Table already created')
    conn.commit()
    conn.close()
    html = "<h3>Hello!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())


@app.route("/plus")
def plus():
    import psycopg2
    from datetime import date
    conn = psycopg2.connect(
        user="user",
        password="passwd",
        host="db",
        dbname="test"
    )
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM increment;');
    count = "Didn't get data!";
    try:
        count = cursor.fetchone()[0];
    except Exception as e:
        count = e;
    dt = date.today()
    cursor.execute('INSERT INTO increment VALUES (%s)',(dt.isoformat(),))
    conn.commit()
    conn.close()
    html = f"<h2>Number of records: {count}</h2><h3>New record: {dt}</h3>"
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
