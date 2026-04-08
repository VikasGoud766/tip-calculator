from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        bill = float(request.form["bill"])
        tip = int(request.form["tip"])
        people = int(request.form["people"])

        tip_as_percent = tip / 100
        total_tip_amount = bill * tip_as_percent
        total_bill = bill + total_tip_amount
        bill_per_person = total_bill / people
        result = round(bill_per_person, 2)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
