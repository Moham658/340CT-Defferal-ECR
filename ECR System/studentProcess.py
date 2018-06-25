import sqlite3 as db

def getCourses():
    """This Function returns all courses from the Course time table
        as a list for Course table"""
    
    conn = db.connect('ECRS_db.db')
    c = conn.cursor()
    
    courses = c.execute('SELECT * FROM Courses').fetchall()

    return courses


def checkExists(list):
    """This function checks to see if a registering student is already registered """
    conn = db.connect('ECRS_db.db')
    c = conn.cursor()
    
    check_exists = c.execute("SELECT title,name,surname,id  FROM Students WHERE DoB=? AND name=? AND surname=?", (list[1],list[2],list[3])).fetchall() # checks if session is free
    return bool(check_exists) #if student exists it returns true 


def getRegStudId(list):
    """This function gets the registered students id for pop-up message"""
    conn = db.connect('ECRS_db.db')
    c = conn.cursor()
    
    getStudDet = c.execute("SELECT title,name,surname,id  FROM Students WHERE DoB=? AND name=? AND surname=?", (list[1],list[2],list[3])).fetchall() # checks if session is free
    details = getStudDet[0]
    return (details[3])



def getRegCourseId(student_id):
    """This function gets the registered students course theyre registered on for pop-up message"""
    conn = db.connect('ECRS_db.db')
    c = conn.cursor()
    
    courseId = c.execute("SELECT courseId FROM registered WHERE studentId=?", (student_id,)).fetchall() # checks if session is free
    details = courseId[0]
    return (details[0])




def getCourseDetails(courseCode):
    """This function gets the registered students course details for pop-up message"""
    conn = db.connect('ECRS_db.db')
    c = conn.cursor()
    
    courseDetails = c.execute("SELECT Course,Code,Type,Start, End  FROM Courses WHERE Code=?", (courseCode,)).fetchall() # checks if session is free
    details = courseDetails[0]
    return (details)


def TempStudDet(list):
    """This function stores the students details in a temporary table until full registration is complete"""

    studentId = incrementStudId()
    title = list[0]
    DoB = list[1]
    name = list[2]
    surname = list[3]
    address1 = list[4]
    address2 = list[5]
    county = list[6]
    postcode = list[7]
    phoneNo = list[8]
    email = list[9]

    conn = db.connect('ECRS_db.db')
    c = conn.cursor()    
    c.execute('UPDATE temporary SET studentId = ? ,title = ? ,name =? ,surname =?, address1 =?, address2=?,county=?, postcode = ?, phoneNo = ?, email = ?, DoB = ? WHERE temp1=?' \
              ,(studentId,title, name,surname,address1,address2,county,postcode,phoneNo,email,DoB,'TempHere'))
    conn.commit() 

    
def incrementStudId():
    """This function gets the last registered students id and increments it for the next registering student"""
    conn = db.connect('ECRS_db.db')
    c = conn.cursor()
    
    getlastStudent = c.execute("SELECT id FROM Students").fetchall() # checks if session is free
    lastStudent = getlastStudent[-1]
    newStudentId = int(lastStudent[0])+1
    
    return (newStudentId)

