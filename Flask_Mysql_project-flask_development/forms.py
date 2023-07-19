from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, IntegerField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Length


class PersonalInfoForm(FlaskForm):
	name = StringField('First Name',
	                   validators = [DataRequired(), Length(min = 2, max = 45)])
	lastname = StringField('Last Name',
	                        validators = [DataRequired(), Length(min = 2, max = 45)])
	phone_number = StringField('Phone Number',
	                           validators = [DataRequired(), Length(min = 2, max = 45)])
	sex = RadioField('Gender', choices = [('F', 'Female'), ('M', 'Male')],
	                 validators = [DataRequired()])
	address = TextAreaField('Address', validators = [DataRequired(), Length(min = 2, max = 45)])
	date_of_birth = DateTimeField('Date of Birth', validators = [DataRequired()])
	expr = IntegerField('Expr', validators = [DataRequired(), Length(max = 10)])
	submit = SubmitField('Save Contact')


class UserIdForm(FlaskForm):
	userid = IntegerField('User ID', validators = [DataRequired(), Length(max = 10)])
	submit = SubmitField('Save Contact')


class ChooseSubjectForm(FlaskForm):
	studentid = IntegerField('Student ID', validators = [DataRequired(), Length(max = 10)])
	courseid = IntegerField('Course ID', validators = [DataRequired(), Length(max = 10)])
	submit = SubmitField('Save Contact')


class FoodForm(FlaskForm):
	mood = RadioField('Mood', choices = [('breakfast', 'breakfast'), ('lunch', 'lunch'), ('dinner', 'dinner')],
	                  validators = [DataRequired()])
	food_id = IntegerField('Food ID', validators = [DataRequired(), Length(max = 10)])
	studentid = IntegerField('Student ID', validators = [DataRequired(), Length(max = 10)])
	score = IntegerField('Score', validators = [DataRequired(), Length(max = 10)])
	submit = SubmitField('Save Contact')


class TeacherRankingForm(FlaskForm):
	studentid = IntegerField('Student ID', validators = [DataRequired(), Length(max = 10)])
	subjectid = IntegerField('Subject ID', validators = [DataRequired(), Length(max = 10)])
	submit = SubmitField('Save Contact')
