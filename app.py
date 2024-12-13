from flask import Flask, render_template, request, redirect, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "supersecretkey"

DATABASE = "contact.db"

# Route for the contact form page
@app.route("/take-part", methods=["GET"])
def take_part():
    return render_template("take-part.html")

# Route to handle form submission
@app.route("/submit-contact", methods=["POST"])
def submit_contact():
    # Get form data
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    if not name or not email or not message:
        flash("All fields are required.", "danger")
        return redirect("/take-part")

    # Save to the database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)", (name, email, message))
    conn.commit()
    conn.close()

    success_message = f"Thank you for contacting us! We'll get back to you soon, {name}!"
    return render_template("take-part.html", success_message=success_message)

if __name__ == "__main__":
    app.run(debug=True)
