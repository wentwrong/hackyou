from flask import Flask, render_template, request, redirect, url_for
from hackyou import gameserver
from hackyou import gameapp

app = Flask(__name__)

@app.route('/cli')
def cli():
    return render_template('console.html')

@app.route('/')
def index():
    serv = gameserver.GameServer()
    serv.download_app(gameapp.GameApp(name="brute", size=50))
    return render_template('server.html', server = serv)

app.run(debug=True)
