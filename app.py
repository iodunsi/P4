from flask import Flask, render_template, request, redirect, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "supersecretkey"

DATABASE = "contact.db"

# Home Route
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Sustainability Tips
@app.route("/sus", methods=["GET"])
def sustainability_tips():
    return render_template("sus.html")

# Eco-Friendly Businesses
@app.route("/efb", methods=["GET"])
def eco_friendly_businesses():
    return render_template("efb.html")

# Resource Library
@app.route("/res", methods=["GET"])
def resource_library():
    return render_template("res.html")

# Contact Form
@app.route("/take-part", methods=["GET", "POST"])
def take_part():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        if not name or not email or not message:
            flash("Please fill out all fields", "danger")
            return redirect("/take-part")

        # Save to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)", (name, email, message))
        conn.commit()
        conn.close()

        success_message = f"Thank you for contacting us! We'll get back to you soon, {name}!"
        return render_template("take-part.html", success_message=success_message)

    return render_template("take-part.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
