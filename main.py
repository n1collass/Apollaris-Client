from flask import Flask
from flask import render_template
from flaskwebgui import FlaskUI # import FlaskUI

app = Flask(__name__)

import routes

if __name__ == "__main__":
  # If you are debugging you can do that in the browser:
  # app.run()
  # If you want to view the flaskwebgui window:
  FlaskUI(app=app, server="flask").run()