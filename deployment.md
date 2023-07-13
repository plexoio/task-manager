# Task Manager | Walkthrough Deployment: IDE

## Modifying your code

Now that you have a database, we need to make some modifications to the code in your IDE.

### In your IDE workspace

Before we can build our application on Heroku, we need to create a few files that Heroku will need to run our application:

1. A `requirements.txt` file which contains a list of the Python dependencies that our project needs in order to run successfully.
2. A `Procfile` which contains the start command to run the project.

### Process

Generate the `requirements.txt` file with the following command in the terminal. After you run this command, a new file called `requirements.txt` should appear in your root directory:

```
pip freeze --local > requirements.txt
```

Heroku requires a `Procfile` containing a command to run your program. Inside the root directory of your project, create the new file. It must be called `Procfile` with a capital 'P', otherwise Heroku won't recognize it.

Inside the file, add the following command:

```
web: python run.py
```

Ensure you do not add a blank line to the end of the file as this can cause problems for deployment.

Open your `__init__.py` file.

Add an `if` statement before the line setting the `SLQALCHEMY_DATABASE_URI`, and in the `else`, set the value to reference a new variable, `DATABASE_URL`.

```python
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
```

To ensure that SQLAlchemy can also read our external database, its URL needs to start with `postgresql://`, but we should not change this in the environment variable. Instead, we'll make an addition to our `else` statement from the previous step to adjust our `DATABASE_URL` in case it starts with `postgres://`:

```python
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri
```

Save all your files and then add, commit, and push your changes to GitHub.

## Up Next

Heroku will now know what to install before building the deployment, and has a file that tells it how to start the service once the build is complete.

Coming up, we will set everything up on Heroku ready for our app.