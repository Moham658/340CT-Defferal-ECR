import sqlite3 as db


def get_registered_student(student_id):
    conn = db.connect('ECRS_db.db')
    c = conn.cursor()


    # get the students details from college database (students table)
    student_contact = c.execute("SELECT title,DoB, name,surname, address1,address2,county,postcode,phoneNo,\
                           email FROM Students WHERE id=?", (student_id,)).fetchall() 
    details_list = student_contact[0]


    #Extracting individual values (PERSONAL DETAILS)for notification message
    title = details_list[0]
    DoB = details_list[1]
    name = details_list[2]
    surname = details_list[3]
    
    address = details_list[4] + "\n" + \
              "               " + \
              details_list[5] + "\n" +\
              "               "+ \
              details_list[6]

    postcode = details_list[7]
    number = details_list[8]
    email = details_list[9]
    



    # gets the students college username/email from college database (students college details table)
    student_college_details = c.execute("SELECT CollUsername, CollEmail FROM StudentCollegeDet WHERE StudentId=?", (student_id,)).fetchall() 
    college_list = student_college_details[0]

    #Extracting individual values (COLLEGE DETAILS)for notification message
    student_username = college_list[0]
    student_college_email = college_list[1]
    

    # gets the registered students course code from college database (registered table)
    registered_course_code = c.execute("SELECT courseId FROM registered WHERE StudentId=?", (student_id,)).fetchall() 
    registered_course_code_ = registered_course_code[0][0]


    # gets the full course details from college database (course table) based on the registered table
    course_details = c.execute("SELECT Course,Type,Start,End,Hours FROM Courses WHERE Code=?", (registered_course_code_,)).fetchall() 
    course_list = course_details[0]
    
    #Extracting individual values (COURSE DETAILS)for notification message
    course_name = course_list[0]
    course_type = course_list[1]
    course_duration = course_list[2] + " - " + course_list[3]
    course_hours = course_list[4]

    #Genereate message for notification
    message = " "*32 + "CONGRATULATIONS  " + name.upper()+"\n"+" "*18+\
              "you have successfully registered at coventry college" +"\n"+\
              "-"*90+"\n"+"#"*90+"\n"+"-"*90+"\n"+" "*26+"-:YOUR PERSONAL DETAILS BELOW:- " +"\n" +"\n"+ \
              "Name:          " + title + " " + name + " " + surname + "\n"*2+\
              "Date of Birth: " + DoB + "\n" *2+\
              "Address:       " + address + "\n" +\
              "Postcode:      " + postcode + "\n"*2 +\
              "Contact No:    " + number + "\n" +\
              "Contact Email: " + email + "\n" +"-"*90+"\n"+"#"*90+"\n"+"-"*90+"\n" * 5 + \
              " "*32 + "IMPORTANT INFORMATION  "+"\n" +" "*5+\
              "please write down your College username, Student ID Number and college email "+"\n"+"-"*90+"\n"+"#"*90+"\n"+"-"*90+\
              "\n"+" "*26+"-:YOUR STUDENT DETAILS BELOW:- " +"\n" +"\n"+ \
              "YOUR STUDENT ID:---------->>>   " + student_id +"\n" +\
              "YOUR STUDENT USERNAME:---->>>   " + student_username + "\n" + \
              "YOUR STUDENT EMAIL:------->>>   " + student_college_email+ "\n" +"-"*90+"\n"+"#"*90+"\n"+"-"*90+"\n"+\
              " "*26+"-:YOUR COURSE DETAILS BELOW:- " +"\n" +"\n"+ \
              "COURSE:------------------->>>   " + course_name + "\n" +\
              "COURSE TYPE:-------------->>>   " + course_type + "\n" +\
              "COURSE DURATION:---------->>>   " + course_duration + "\n" +\
              "COURSE HOURSE PER WEEK:--->>>   " + course_hours + "\n" + "-"*90+"\n"+"#"*90+"\n"+"-"*90
              
              
        
    with open("notification_message.txt", "w") as text_file:
        text_file.write(message)        



