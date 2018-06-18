import sqlite3 as db

def getCourses():
    """This Function returns all courses from the Course time table
        as a list for Course table"""
    
    conn = db.connect('ECRS_db.db')
    c = conn.cursor()
    
    courses = c.execute('SELECT * FROM Courses').fetchall()

    return courses


def checkExists(list):
    
    conn = db.connect('ECRS_db.db')
    c = conn.cursor()
    
    check_exists = c.execute("SELECT title,name,surname,id  FROM Students WHERE DoB=? AND name=? AND surname=?", (list[1],list[2],list[3])).fetchall() # checks if session is free
    return bool(check_exists)


def getRegStudId(list):
    
    conn = db.connect('ECRS_db.db')
    c = conn.cursor()
    
    check_exists = c.execute("SELECT title,name,surname,id  FROM Students WHERE DoB=? AND name=? AND surname=?", (list[1],list[2],list[3])).fetchall() # checks if session is free
    details = check_exists[0]
    return (details[3])

print(getRegStudId(('0','15/07/1994','Ahmed','Mohammed')))
        



def getRegCourseId(student_id):
   
    conn = db.connect('ECRS_db.db')
    c = conn.cursor()
    
    courseId = c.execute("SELECT courseId FROM registered WHERE studentId=?", (student_id,)).fetchall() # checks if session is free
    details = courseId[0]
    return (details[0])


print(getRegCourseId(getRegStudId(('0','15/07/1994','Ahmed','Mohammed'))))


def getCourseDetails(courseCode):
    
    conn = db.connect('ECRS_db.db')
    c = conn.cursor()
    
    courseDetails = c.execute("SELECT Course,Code,Type,Start, End  FROM Courses WHERE Code=?", (courseCode,)).fetchall() # checks if session is free
    details = courseDetails[0]
    return (details)

print(getCourseDetails(getRegCourseId(getRegStudId(('0','15/07/1994','Ahmed','Mohammed')))))
