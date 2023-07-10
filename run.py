import os
from taskmanager import app

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )

run.py > env.py > __init__.py > routes.py > base.html