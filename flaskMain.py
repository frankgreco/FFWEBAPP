from flask import Flask, render_template, request, redirect, url_for
from clients.DatabaseClient import DatabaseClient
from packages.Calculator import Calculator
from packages.TestDatabase.TestDatabase import TestDatabase

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    try:
        if request.method == "POST":
            league_id = request.form["league_id"]
            return redirect(url_for("leagueHomepage", league_id=league_id))
        else:
            return render_template("indexHomepage.html")
    except Exception as e:
        print("except", e)
        return render_template("indexHomepage.html")


@app.route("/testHomePage", methods=["GET"])
def testHomepage():
    return render_template("testHomepage.html", subtitle="Test Home Page")


@app.route("/test", methods=["GET", "POST"])
def test():
    subtitle = "Test"
    try:
        c = Calculator.Calculator()
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        sum = c.add(num1, num2)
        # TEST DATABASE
        id = 1
        dbClient = DatabaseClient(id)
        dbClient.setLeague(id, {"_id": id, "num1": num1, "num2": num2})
        # END TEST
        return render_template("test.html", subtitle=subtitle, sum=sum)
    except:
        return render_template("test.html", subtitle=subtitle, sum="N/A")


@app.route("/leaguehomepage/<league_id>")
def leagueHomepage(league_id):
    dbClient = DatabaseClient(int(league_id))
    if dbClient.getLeague():
        return dbClient.getLeague()
    else:
        return f"league with id {league_id} not found"


if __name__ == "__main__":
    app.run(debug=True)
