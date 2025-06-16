from app import app
import os

app.secret_key = os.getenv("FLASK_KEY", "default-key")

if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    app.run(debug=debug)
