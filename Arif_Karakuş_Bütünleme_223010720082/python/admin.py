# app.py
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///admin_panel.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

@app.route("/")
def index():
    return render_template("index_admin.html")

@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    user_data = [{"id": user.id, "name": user.name} for user in users]
    return jsonify(user_data)

@app.route("/settings", methods=["POST"])
def save_settings():
    site_title = request.form["site-title"]
    site_description = request.form["site-description"]
    return jsonify({"message": "Settings saved successfully"})

if __name__ == "__main__":
    app.run(debug=True)