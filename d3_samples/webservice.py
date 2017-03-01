from flask import Flask
from flask import request
from database import Database
import json
from statistics import mean
#pip3 install flask-cors
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

db = Database()




@app.route("/bookstats")
def bookstats():
    limit = request.args.get('limit')
    if not limit:
        limit = 10
    db.cur.execute("SELECT *, COUNT() FROM books JOIN reviews ON reviews.bookId = books.id")
    players = []
    i = 1
    for row in db.cur:
        player = {"position":i,"name":row["name"], "score":row["final"]}
        players.append(player)
        i += 1
    return json.dumps(players)

@app.route("/moneyByName")
def moneyByName():
    name = request.args.get('name')
    #SQL call to get money by name goes here

@app.route("/money")
def money():
    name = request.args.get('name')
    limit = request.args.get('limit')
    if not limit:
        limit = 10

    profession = request.args.get('profession')
    print(profession)

    sqlCall = "SELECT *, SUM(final) as money FROM scores JOIN players ON scores.playerId = players.id "
    clauses = []
    if name:
        clauses.append(" name LIKE \"%"+name+"%\" ")

    if profession:
        clauses.append(" background LIKE \"%"+profession+"%\" ")

    if clauses:
        sqlCall += " WHERE "+"AND".join(clauses)


    sqlCall += " GROUP BY playerId ORDER BY money DESC LIMIT "+str(limit)
    print(sqlCall)

    db.cur.execute(sqlCall)
    players = []
    for row in db.cur:
        player = {"name":row["name"],"money":int(row["money"]), "background":row["background"]}
        players.append(player)

    return json.dumps(players)




@app.route("/hello")
def hello():
    name = request.args.get('name')
    return "Hello "+str(name)+"!"


if __name__ == "__main__":
    app.run()
