import sqlite3 as db


def get_registered_student(student_id):
    conn = db.connect('ECRS_db.db')
    c = conn.cursor()


    # get the students details from college database (students table)
    student_contact = c.execute("SELECT title,DoB, name,surname, address1,address2,county,postcode,phoneNo,\
                           email FROM Students WHERE id=?", (student_id,)).fetchall() 
    details_list = student_contact[0]
    



    # gets the students college username/email from college database (students college details table)
    student_college_details = c.execute("SELECT CollUsername, CollEmail FROM StudentCollegeDet WHERE StudentId=?", (student_id,)).fetchall() 
    college_list = student_college_details[0]
    

    # gets the registered students course code from college database (registered table)
    registered_course_code = c.execute("SELECT courseId FROM registered WHERE StudentId=?", (student_id,)).fetchall() 
    registered_course_code_ = registered_course_code[0][0]


    # gets the full course details from college database (course table) based on the registered table
    course_details = c.execute("SELECT Course,Type,Start,End,Hours FROM Courses WHERE Code=?", (registered_course_code_,)).fetchall() 
    course_list = course_details[0]

    
    
    print(details_list)
    print(college_list)
    print(registered_course_code_)
    print(course_list)

get_registered_student("10003")
