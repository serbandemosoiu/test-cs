from flask import Flask, render_template, request, redirect, url_for
from wtforms import Form, StringField, PasswordField, SelectField, validators

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

class OnboardingForm(Form):
    name = StringField('Name', [validators.DataRequired()])
    email = StringField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    gender = SelectField('Gender', choices=[('', '--Select Gender--'), ('male', 'Male'), ('female', 'Female'), ('other', 'Other')], validators=[validators.DataRequired()])
    country = StringField('Country', [validators.DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = OnboardingForm(request.form)

    if request.method == 'POST' and form.validate():
        # Perform further validation and processing here...
        return redirect(url_for('success'))

    return render_template('index.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
