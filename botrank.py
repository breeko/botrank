import csv
from flask import Flask, render_template, request
app = Flask(__name__)

ITEMS_PER_PAGE = 250

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

  sort = request.args.get("sort", "rank")
  order = request.args.get("order")
  page = request.args.get("page", "1")

  cols = [ "rank", "name", "score", "good-votes", "bad-votes" ]

  numeric_cols = {"rank", "score", "good-votes", "bad-votes"}
  reverse_cols = {"score", "good-votes", "bad-votes"}

  if sort not in cols:
    sort = "rank"

  if sort in reverse_cols:
    reverse = True
  else:
    reverse = False

  if order:
    reverse = not reverse

  total = len(bots)
  if total > int(page) * ITEMS_PER_PAGE:
    more = True
  else:
    more = False

  bots = sorted(bots, key=lambda k: float(k[sort]) if sort in numeric_cols else k[sort], reverse=reverse)

  if page.isdigit() and int(page) > 0:
    page = int(page)
    page = page - 1
    bots = bots[(page * ITEMS_PER_PAGE):((page * ITEMS_PER_PAGE) + ITEMS_PER_PAGE)]
    page = page + 1
  else:
    page = 1

  params = {"sort": sort, "order": order, "page": page, "total": total, "more": more}

  return render_template("index.html", bots=bots, params=params)
