from database_connection import *

def query_exec(query):
	try:
		cur = mysql.connection.cursor()
		cur.execute(query)
		rows = cur.fetchall()
		cur.close()
		# response = [{'column1': row[0], 'column2': row[1]} for row in rows]
		# return jsonify(response)
		return rows

	except Exception as e:
		print(str(e))
		# return jsonify([])
		return None


def personal_information(name, lastname, sex, date_of_birth, address, phone_number, expr):
	# تغییر اطلاعات شخصی
	query = f'''
	CREATE DEFINER=`root`@`localhost` PROCEDURE `personal_information`(in name varchar(45), lastname varchar(45), sex varchar(45), date_of_birth datetime, address varchar(45), phone_number varchar(45), expr int(10))
	BEGIN
	    UPDATE `mydb`.`personal_information`
	    SET
	        `name` = {name},
	        `lastname` = {lastname},
	        `sex` = {sex},
	        `date_of_birth` = {date_of_birth},
	        `address` = {address},
	        `phone_number` = {phone_number}
	    WHERE `PK` = {expr};
	END
	'''
	return query_exec(query)


def absence(userid):
	# ثبت غیبت
	query = f'''
CREATE DEFINER=`root`@`localhost` PROCEDURE `absences`(in userid int(10))
BEGIN
 select title ,simeseter , `Absence number`,absence_reasons  from presence,subject where subject.idsubject = subject_idsubject and presence.student_user_iduser = {userid} ;
END
	'''
	return query_exec(query)


def result_report(userid):
	# کارنامه
	query = f'''
CREATE DEFINER=`root`@`localhost` PROCEDURE `result_report`(in userid int(10))
BEGIN
 select title,score_student , credits ,simeseter from presence,subject where subject.idsubject = subject_idsubject and presence.student_user_iduser = {userid} ;
END
	'''
	return query_exec(query)


def exam_dates(userid):
	# برنامه امتحانی
	query = f"""
CREATE DEFINER=`root`@`localhost` PROCEDURE `exam dates`(in userid int(10))
BEGIN
select title,exam_time from presence,subject where subject.idsubject = subject_idsubject and presence.student_user_iduser = {userid} ;
END
"""
	return query_exec(query)


def choose_subject(studentid, courseid):
	# انتخاب واحد
	query = f"""
CREATE DEFINER=`root`@`localhost` PROCEDURE `choose_subject`(in studentid int(10) , courseid int(10))
BEGIN
if(now()<(select distinct end_choose_subject_date from head_of_management) and now()>(select distinct begin_choose_subject_date from head_of_management) ) then
INSERT INTO `mydb`.`presence`
(`subject_idsubject`,`student_user_iduser`,`Signature`,`teacher_idteacher`,`simeseter`)
VALUES
({courseid},{studentid},0,(select teacher_idteacher from subject where idsubject= {courseid}),(select distinct Current_Term from head_of_management)) ;
else
SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Out of date error';
end if;
END
"""
	return query_exec(query)


def class_schedule(userid):
	# برنامه کلاسی
	query = f"""
CREATE DEFINER=`root`@`localhost` PROCEDURE `class_schedule`(in userid int(10))
BEGIN
select title, class_time from presence,subject where subject.idsubject = subject_idsubject and presence.student_user_iduser = {userid} ;
END
"""
	return query_exec(query)


def delete_one_subject(studentid, courseid):
	# حذف تک درس
	query = f"""
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_one_subject`(in studentid int(10) , courseid int(10))
BEGIN
if(now()<(select distinct end_delete_subject from head_of_management)) then
DELETE FROM `mydb`.`presence`
WHERE (select PK from presence where student_user_iduser = {studentid} and {courseid}=subject_idsubject and signature<>1);
end if;
END
"""
	return query_exec(query)


def delete_subject(studentid, courseid):
	# حذف درس در حذف و اضافه
	query = f"""
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_subject`(in studentid int(10) , courseid int(10))
BEGIN
if(now()<(select distinct end_choose_subject_day from head_of_management) and now()>(select distinct begin_choose_subject_day from head_of_management) ) then
DELETE FROM `mydb`.`presence`
WHERE (select PK from presence where student_user_iduser = {studentid} and {courseid}=subject_idsubject and signature<>1);
end if;
END
"""
	return query_exec(query)


def food_delete(food_id, student_id, reserve_date):
	# حذف غذا
	query = f"""
CREATE DEFINER=`root`@`localhost` PROCEDURE `food_delete`(in food_id int(5),student_id int(5),reserve_date datetime)
BEGIN
DELETE FROM `mydb`.`food`
WHERE Date = {reserve_date} and food_dict_idfood_dict = {food_id} and student_student_id = {student_id};
END
"""
	return query_exec(query)


def food_reserve(food_id, student_id, mood):
	# رزرو غذا
	query = f"""
CREATE DEFINER=`root`@`localhost` PROCEDURE `food_reserve`(in food_id int(5),student_id int(5),mood varchar(45))
BEGIN
INSERT INTO `mydb`.`food`
(`breakfast_lunch_dinner`,`Date`,`food_dict_idfood_dict`,`student_student_id`)
VALUES
({mood},now(),{food_id},{student_id});
END
"""
	return query_exec(query)


def teacher_ranking(subjectid, studentid, score):
	# نمره دهی به استاد
	query = f"""
CREATE DEFINER=`root`@`localhost` PROCEDURE `teacher ranking`(in subjectid int(10), studentid int(10), score int(10))
BEGIN
UPDATE mydb.presence
SET
`score_teacher` ={score}
WHERE `PK` = (select * from (select PK from presence where student_user_iduser={studentid} and Signature =0 and subject_idsubject ={subjectid} limit 1)as alpha);
END
"""
	return query_exec(query)
