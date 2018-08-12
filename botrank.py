import csv
from flask import Flask, render_template, request
app = Flask(__name__)

def read_csv(filename="bots.csv"):
  rt = []
  fh = open(filename, "r")
  reader = csv.reader(fh, delimiter=",")
  clean = lambda c: c.encode('ascii',errors='ignore').decode()
  headers = next(reader)
  clean_headers = [clean(h) for h in headers]
  for row in reader:
    rank = { col:row[idx] for idx, col in enumerate(clean_headers) }
    rt.append(rank)

  return rt

@app.route("/", methods=['GET'])
def index():
  bots = read_csv()

  sort = request.args.get("sort", "Rank")
  cols = [ "Rank", "Bot Name", "Score", "Good Bot Votes", "Bad Bot Votes" ]
  
  numeric_cols = {"Rank", "Score", "Good Bot Votes", "Bad Bot Votes"}
  reverse_cols = {"Score", "Good Bot Votes", "Bad Bot Votes"}

  if sort in cols:
    if sort in reverse_cols:
      reverse = True
    else:
      reverse = False

    bots = sorted(bots, key=lambda k: float(k[sort]) if sort in numeric_cols else k[sort], reverse=reverse)
  
  return render_template("index.html", bots=bots)
