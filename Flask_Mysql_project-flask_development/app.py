from database_connection import *
from queries import *
from forms import PersonalInfoForm, UserIdForm, ChooseSubjectForm, FoodForm, TeacherRankingForm
from flask import render_template, request, redirect, url_for, session


@app.route('/index')
@app.route('/')
def index():
	return render_template('index.html')


##############################################################
# authentication section
@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

		# Check if the entered username exists in the student table
		cursor = mysql.connection.cursor()
		student_query = "SELECT * FROM student WHERE student_id = %s"
		cursor.execute(student_query, (username,))
		student = cursor.fetchone()
		# TODO: session set for student

		# Check if the entered username exists in the teacher table
		teacher_query = "SELECT * FROM teacher WHERE idteacher = %s"
		cursor.execute(teacher_query, (username,))
		teacher = cursor.fetchone()
		# TODO: session set for teacher and head

		cursor.close()

		if student or teacher:
			# TODO: authentication logic(compare passwords)

			return redirect('index.html')
		else:
			# Invalid username
			error = 'Invalid username'
			return render_template('login.html', error = error)

	return render_template('login.html')


@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('login'))


############################################################################
@app.route('/update_profile', methods = ['GET', 'POST'])
def profile():
	form = PersonalInfoForm()  # Create an instance of the form

	if form.validate_on_submit():
		name = request.form.get('name')
		lastname = request.form.get('lastname')
		phone_number = request.form.get('phone_number')
		sex = request.form.get('sex')
		address = request.form.get('address')
		date_of_birth = request.form.get('date_of_birth')
		expr = request.form.get('expr')
		if personal_information(name = name, lastname = lastname, phone_number = phone_number, sex = sex,
		                     address = address, date_of_birth = date_of_birth, expr = expr):
			return redirect('/index.html', message = 'Success')
	return render_template('update_profile.html', form = form)


if __name__ == '__main__':
	app.run()

# TODO : create r
#  equirements.txt
