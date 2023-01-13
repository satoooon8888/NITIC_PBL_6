from flask import Flask, redirect, url_for, flash, render_template, jsonify, request
from flask_login import login_required, logout_user, current_user
from .config import Config
from .models import db, login_manager, get_teachers, update_teacher_location, get_teacher_locations
from .oauth import blueprint
from .cli import create_db


app = Flask(
    __name__, 
    static_folder='static', 
    static_url_path=''
)
app.config.from_object(Config)
app.register_blueprint(blueprint, url_prefix="/login")
app.cli.add_command(create_db)
db.init_app(app)
login_manager.init_app(app)

@app.route("/")
def index():
    return redirect("/index.html")

@app.route("/api/logout")
@login_required
def logout():
    logout_user()
    flash("You have logged out")
    return redirect(url_for("index"))

@app.route("/api/teacher")
def handle_teacher():
    teachers = get_teachers()
    teacher_dicts = []
    for teacher in teachers:
        teacher_dicts.append({
            "id": teacher.id, 
            "email": teacher.email, 
            "location": lookup_location_by_id(teacher.location_id),
            "name": teacher.name
        })
    return jsonify(teacher_dicts)

@app.route("/api/teacher/location", methods=["POST"])
@login_required
def update_location():
    update_teacher_location(current_user, int(request.form["location_id"]))
    return redirect(url_for("index"))

@app.route("/api/teacher/location", methods=["POST"])
@login_required
def register_loc():
    register_location(current_user, request.form["location"])
    return redirect(url_for("index"))

@app.route("/api/teacher/location")
@login_required
def get_location():
    locations = get_teacher_locations(current_user)
    location_dicts = []
    for loc in locations:
        location_dicts.append({
            "user_id": loc.user_id,
            "location": loc.location
        })
    return jsonify(location_dicts)
