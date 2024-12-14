from flask import Flask, render_template, request, redirect, flash
import psycopg2
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

# PostgreSQL Connection URL from Render
DATABASE_URL = os.environ.get("DATABASE_URL")

# Home Route
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Contact Form Submission
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
        conn = psycopg2.connect(DATABASE_URL, sslmode="require")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)", 
            (name, email, message)
        )
        conn.commit()
        cursor.close()
        conn.close()

        success_message = f"Thank you for contacting us! We'll get back to you soon, {name}!"
        return render_template("take-part.html", success_message=success_message)

    return render_template("take-part.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
