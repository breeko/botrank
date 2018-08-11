import csv
from flask import Flask, render_template, request
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

  cols = [ "name", "rank", "karma", "replies", "read_time" ]
  sort = request.args.get("sort")

  if sort in cols:
    if sort == "rank" or sort == "name":
      reverse = False
    else:
      reverse = True
    bots = sorted(bots, key=lambda k: k[sort], reverse=reverse)
  else:
    bots = sorted(bots, key=lambda k: k["rank"], reverse=False)

  return render_template("index.html", bots=bots)
