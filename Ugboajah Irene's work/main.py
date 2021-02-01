from flask import Flask, render_template, request


app = Flask (__name__)


@app.route("/")
def home():
    return render_template('home.html', title="Home")


@app.route("/signup/")
def signup():
    return render_template('signup.html', title="SIGN UP", information="Use the form displayed to register")


@app.route("/process-signup/", methods=['POST'])
def process_signup():

    firstname = request.form['firstname']
    surname = request.form['surname']
    dateofbirth = request.form['dateofbirth']
    residentialaddress= request.form['residentialaddress']
    nationality = request.form['nationality']
    nationalidentificationnumber = request.form['nationalidentificationnumber']

    try:
        user = models.User(firstname=firstname, surname=surname, dateofbirth=dateofbirth, residentialaddress=residentialaddress,
                           nationality=nationality, nationalidentificationnumber=nationalidentificationnumber)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

    except Exception as e:
        # Error caught, prepare error information for return
        information = 'Could not submit. The error message is {}'.format(e.__cause__)
        return render_template('signup.html', title="SIGN-UP", information=information)

    information = 'User by name {} {} successfully added. The login name is the firstname {}.'.format(firstname, surname, dateofbirth, residentialaddress, nationality, nationalidentificationnumber)

    return render_template('signup.html', title="SIGN-UP", information=information)


if __name__ == '__main__':
    app.run(port=5005)
