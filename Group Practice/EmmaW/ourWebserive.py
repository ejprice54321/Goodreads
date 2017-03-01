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
    db.cur.execute("SELECT *  FROM books")
    ratings = []
    i = 1
    for row in db.cur:
        rating = {"rating":row["rating"]}
        rating = int(rating)
        ratings.append(rating)
        i += 1
    return json.dumps(ratings)


if __name__ == "__main__":
    app.run()
