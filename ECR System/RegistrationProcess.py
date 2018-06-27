import sqlite3 as db
import notificationsProcess

def set_student_details(list):
    """This function stores the students details (title, name, address, contact and personal email) in the college database"""

    #extracting required student details values from list given from register_student function (unregistered student from temporary table)
    title = list[1]
    DoB = list[2]
    name = list[3]
    surname = list[4]
    address1 = list[5]
    address2 = list[6]
    county = list[7]
    postcode = list[8]
    phoneNo = list[9]
    email = list[10]

    conn = db.connect('ECRS_db.db')
    c = conn.cursor()
    #storing details into college database
    c.execute('INSERT INTO Students values (? ,? ,? ,?, ?, ?, ?, ?, ?, ?, ?)' \
              ,(studentId,title,DoB, name,surname,address1,address2,county,postcode,phoneNo,email))
    conn.commit() 




def set_college_details(list):
    """This function stores the students College details (student ID, username, password) in the college database
        and generates a college email based on the students chosen username"""

    #extracting student college details from register_student function (unregistered student from temporary table)
    studentId = list[0]
    username = list[12]
    email = str(list[12]+"@cov.college.uk") #generates students college email
    password = list[13]


    conn = db.connect('ECRS_db.db')
    c = conn.cursor()
    #stores details into college database
    c.execute('INSERT INTO StudentCollegeDet values (? , ?, ?, ? )' \
              ,(studentId,username,email, password))
    conn.commit()


def set_registered(list):
    """This function stores the students ID and Course they are registered on into the colleges registered table"""

    #extracting student ID and course code from register_student function (unregistered student from temporary table)
    studentId = list[0]
    course = list[11]

    conn = db.connect('ECRS_db.db')
    c = conn.cursor()
    #inserting newly registered student into college database
    c.execute('INSERT INTO registered values (? , ?)' \
              ,(studentId,course))
    conn.commit()
    

def update_course_spaces(list):
    """This Function updates the spaces available in the course table after the student has registered"""

    
    course = list[11]# extracting course code from register_student function(unregistered student from temporary table)
    
    conn = db.connect('ECRS_db.db')
    c = conn.cursor()

    
    spaces = c.execute("SELECT AvSpc FROM Courses WHERE Code=?", (course,)).fetchall()#getting current spaces
    spaces_= spaces[0][0] 

    new_spaces = str(int(spaces_)-1)#reducing available spaces by 1 (registered student)


    #updating course
    c.execute('UPDATE Courses SET AvSpc = ?  WHERE Code=?' \
              ,(new_spaces,course))
    conn.commit() 



def register_student():
    """This function writes the registered students details from the temporary table and to their actual tables the student"""
    
    conn = db.connect('ECRS_db.db')
    c = conn.cursor()
    
    student_details = c.execute("SELECT studentId ,title,DoB, name,surname, address1,address2,county,postcode,phoneNo,\
                           email,courseId,CollUsername,CollPassword FROM temporary WHERE temp1=?", ("TempHere",)).fetchall() # get the students details from temporary table (unregistered)
    new_student = student_details[0]
    
    student_id = new_student[0]#student id required for notification process
    
    
    update_course_spaces(new_student) # reduce the course spaces by 1 (for registering student)
    set_registered(new_student) # write to registered table (student ID and Course code)
    set_college_details(new_student) # write to students college details table (student ID, username, password)
    set_student_details(new_student) # write to students table (title, name, address, contact and personal email)

    #After registering we notifiy the notification processor(registration processor complete)
    notificationsProcess.get_registered_student(student_id)
    


    

    

