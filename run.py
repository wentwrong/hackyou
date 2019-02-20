from flask import Flask, render_template, request, redirect, url_for
from hackyou import gameserver

app = Flask(__name__)

@app.route('/')
def index():
    # TODO
    serv = gameserver.GameServer()
    return render_template('index.html', serv = serv)


app.run(debug=True)
