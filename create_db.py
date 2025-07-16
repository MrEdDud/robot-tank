from api import app, db  # imports the flask app and database instance from the api file

with app.app_context():  # opens the application context so that the database can run commands
    db.create_all()  # creates all tables defined in SQLAlchemy models