import csv
from flask import Flask, render_template
app = Flask(__name__)

def read_csv(filename="bots.csv"):
  rt = []
  fh = open(filename, "r")
  reader = csv.reader(fh, delimiter=",")
  for row in reader:
    rank = {
      "name": row[0],
      "url": row[1],
      "rank": row[2],
      "karma": row[3],
      "replies": row[4],
      "read_time": row[5]
    }
    rt.append(rank)

  return rt

@app.route("/", methods=['GET'])
def index():
  bots = read_csv()
  bots = sorted(bots, key=lambda k: k["rank"]) 
  return render_template("index.html", bots=bots)
