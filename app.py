import csv

from flask import Flask, render_template, request
from prettytable import PrettyTable
app = Flask(__name__)
data=[]
with open("result.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)

col = [x[1] for x in data]

#print(col)
@app.route("/", methods=["GET", "POST"])

def recommender():
    a = []
    error = ''
    try:
        if request.method == "POST":
            attempted_username = request.form['fname']
            print(attempted_username)
            if attempted_username in col:
                for x in range(0,len(data)):
                    if attempted_username == data[x][1]:
                        print(data[x][3])
                        a.append(data[x][3])

                return render_template("recommender.html", a=a)
            else:
                return render_template("recommender.html", a="not found")

        return render_template("recommender.html",error=error)

    except Exception as e:
        # flash(e)
        return render_template("recommender.html",error=error)

    return render_template('recommender.html')


if __name__ == '__main__':
    app.run(debug=True)