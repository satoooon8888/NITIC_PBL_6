from flask import Flask, redirect, url_for, flash, render_template, jsonify
from flask_login import login_required, logout_user, current_user
from .config import Config
from .models import db, login_manager, get_teachers
from .oauth import blueprint
from .cli import create_db


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(blueprint, url_prefix="/login")
app.cli.add_command(create_db)
db.init_app(app)
login_manager.init_app(app)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have logged out")
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("home.html")

@app.route("/api/teacher")
def handle_teacher():
    teachers = get_teachers()
    teacher_dicts = []
    for teacher in teachers:
        teacher_dicts.append({
            "id": teacher.id, 
            "email": teacher.email, 
            "location": teacher.location
        })
    return jsonify(teacher_dicts)

@app.route("/api/teacher/location")
@login_required
def update_location():
    update_teacher_location(current_user, request.form.location)
    return "ok"

