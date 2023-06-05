from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  "id": 1,
  "title": "Data Analyst",
  "location": "Bengalore",
  "salary": "Rs 15,00,000"
}, {
  "id": 2,
  "title": "Data Scientist",
  "location": "Remote",
  "salary": "Rs 17,00,000"
}, {
  "id": 3,
  "title": "Frontend Engineer",
  "location": "San Francisco",
  "salary": "150000 USD"
}, {
  "id": 4,
  "title": "Programmer  Analyst",
  "location": "Bengalore",
  "salary": "Rs 15,00,000"
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


print(__name__)
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
