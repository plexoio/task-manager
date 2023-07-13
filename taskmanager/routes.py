from flask import render_template, request, url_for, redirect
from taskmanager import app, db
from taskmanager.models import Category, Tasks


@app.route("/")
def home():
    tasks = list(Tasks.query.order_by(Tasks.id).all())
    return render_template("tasks.html", tasks=tasks)

# Add Categories

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

# UPDATE


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("category"))
    return render_template("edit_category.html", category=category)

# DELETE


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("category"))

# Add Tasks

# READ

# CREATE


@app.route("/add_task", methods=["GET", "POST"])
def add_task():

    categories = list(Category.query.order_by(Category.category_name).all())

    if request.method == "POST":

        task = Tasks(
            task_name=request.form.get("task_name"),
            text_description=request.form.get("text_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            category_id=request.form.get("category_id"))

        db.session.add(task)
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("add_task.html", categories=categories)

# UPDATE

# DELETE
