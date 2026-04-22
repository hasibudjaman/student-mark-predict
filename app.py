from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        try:
            hours = float(request.form["hours"])

            pred = model.predict([[hours]])[0]

            # 🔥 LIMIT FIX
            pred = max(0, min(100, pred))

            prediction = round(pred, 2)

        except:
            prediction = "Invalid input!"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)