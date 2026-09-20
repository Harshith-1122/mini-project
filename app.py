import os
from urllib.parse import quote_plus
from flask import Flask
from dotenv import load_dotenv
from models import db
from controllers.main_controller import main_bp
from controllers.db_controller import db_bp

load_dotenv()

app = Flask(__name__)

# Individual MySQL database settings
db_user = quote_plus(os.getenv("MYSQL_USER", "root"))
db_password = quote_plus(os.getenv("MYSQL_PASSWORD", ""))
db_host = os.getenv("MYSQL_HOST", "localhost")
db_port = os.getenv("MYSQL_PORT", "3306")
db_name = os.getenv("MYSQL_DB", "hotel_booking")

# Build SQLAlchemy connection URL from URL-encoded components
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize database extension
db.init_app(app)

# Register controller blueprints
app.register_blueprint(main_bp)
app.register_blueprint(db_bp)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
