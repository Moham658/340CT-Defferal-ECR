import sqlite3 as db

def getCourses():
    """This Function returns all courses from the Course time table
        as a list for Course table"""
    
    conn = db.connect('ECRS_db.db')
    c = conn.cursor()
    
    courses = c.execute('SELECT * FROM Courses').fetchall()

    return courses


