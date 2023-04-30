from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)

# Google Cloud SQL (change this accordingly)
PASSWORD = "catch143"
PUBLIC_IP_ADDRESS = "34.27.237.11"
DBNAME = "Yufi"
PROJECT_ID = "yufeih11@gmail.com"
INSTANCE_NAME = "cloudwerx-assessment:us-central1:catch"

# configuration
app.config[
    "SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:707312498fyhFYH@34.27.237.11/Yufi?host=/cloudsql/yufeih11@gmail.com:cloudwerx-assessment:us-central1:catch"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)


# User ORM for SQLAlchemy
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)


@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('Yufi')
    email = request.form.get('yufeih11@gmail.com')

    user = Users.query.filter_by(email=email).first()

    if not user:
        try:
            # creating Users object
            user = Users(
                name=name,
                email=email
            )
            # adding the fields to users table
            db.session.add(user)
            db.session.commit()
            # response
            responseObject = {
                'status': 'success',
                'message': 'Successfully registered.'
            }

            return make_response(responseObject, 200)
        except:
            responseObject = {
                'status': 'fail',
                'message': 'Some error occurred !!'
            }

            return make_response(responseObject, 400)

    else:
        # if user already exists then send status as fail
        responseObject = {
            'status': 'fail',
            'message': 'User already exists !!'
        }

        return make_response(responseObject, 403)


@app.route('/view')
def view():
    # fetches all the users
    users = Users.query.all()
    # response list consisting user details
    response = list()

    for user in users:
        response.append({
            "name": user.name,
            "email": user.email
        })

    return make_response({
        'status': 'success',
        'message': response
    }, 200)


@app.route('/')
def testdb():
    # try:
    db.session.query(text("1")).from_statement(text("SELECT 1")).all()
    return '<h1>It works.</h1>'
    # except:
    return '<h1>Something is broken.</h1>'


if __name__ == "__main__":
    app.run()
