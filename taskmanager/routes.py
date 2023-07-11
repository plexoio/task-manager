from flask import render_template, request, url_for, redirect
from taskmanager import app, db
from taskmanager.models import Category, Tasks


@app.route("/")
def home():
    return render_template("tasks.html")

# READ
@app.route("/categories")
def category():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)

# CREATE
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("category"))
    return render_template("add_category.html")
