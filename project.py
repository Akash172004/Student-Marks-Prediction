
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Read dataset
data = pd.read_csv("pp.csv")

X = data['Study_Hours']
Y = data['Marks']

n = len(X)

mean_x = sum(X) / n
mean_y = sum(Y) / n

numerator = sum((X - mean_x) * (Y - mean_y))
denominator = sum((X - mean_x) ** 2)

m = numerator / denominator
c = mean_y - (m * mean_x)


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        hours = float(request.form["hours"])

        prediction = m * hours + c

        prediction = round(prediction, 2)

    return render_template(
        "index.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)