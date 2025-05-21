from flask import Flask
from routes.whoami import bp as whoami_bp

app = Flask(__name__)
app.register_blueprint(whoami_bp)

if __name__ == "__main__":
    app.run()
