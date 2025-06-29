# Projeto Apollaris Client

from app import create_app
from flaskwebgui import FlaskUI

app = create_app()

ui = FlaskUI(app=app, server="flask", width=800, height=600)

if __name__ == "__main__":
    ui.run()