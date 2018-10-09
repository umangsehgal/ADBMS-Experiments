def get_student_id(cur):
    
    cur.execute('SELECT * FROM "Student" ORDER BY "Student_Id" DESC LIMIT 1')
    returnValue = None
    for line in cur.fetchall():
        returnValue = line[0]
    return returnValue

def get_department_id(cur):
    
    cur.execute('SELECT * FROM "Department" ORDER BY "Department_ID" DESC LIMIT 1')
    returnValue = None
    for line in cur.fetchall():
        returnValue = line[0]   
    return returnValue

def get_reg_id(cur):
    
    cur.execute('SELECT * FROM "Enrollment" ORDER BY "Registration_Id" DESC LIMIT 1')
    returnValue = None
    for line in cur.fetchall():
        returnValue = line[0]   
    return returnValue

def get_faculty_id(cur):
    
    cur.execute('SELECT * FROM "Faculty" ORDER BY "Faculty_Id" DESC LIMIT 1')
    returnValue = None
    for line in cur.fetchall():
        returnValue = line[0]   
    return returnValue

def get_course_id(cur):
    
    cur.execute('SELECT * FROM "Course" ORDER BY "Course_ID" DESC LIMIT 1')
    returnValue = None
    for line in cur.fetchall():
        returnValue = line[0]   
    return returnValue

def get_grade_id(cur):
    
    cur.execute('SELECT * FROM "Grade" ORDER BY "Grade_ID" DESC LIMIT 1')
    returnValue = None
    for line in cur.fetchall():
        returnValue = line[0]   
    return returnValue

def get_random_department_id(cur):
    
    cur.execute('SELECT * FROM "Department" ORDER BY random() DESC LIMIT 1')
    returnValue = None
    for line in cur.fetchall():
        returnValue = line[0]   
    return returnValue

def get_random_instructor_id(cur):
    
    cur.execute('SELECT * FROM "Faculty" ORDER BY random() DESC LIMIT 1')
    returnValue = None
    for line in cur.fetchall():
        returnValue = line[0]   
    return returnValue

def get_random_student_id(cur):
    
    cur.execute('SELECT * FROM "Student" ORDER BY random() DESC LIMIT 1')
    returnValue = None
    for line in cur.fetchall():
        returnValue = line[0]
    return returnValue

def get_random_course_id_line(cur):
    
    cur.execute('SELECT * FROM "Course" ORDER BY random() DESC LIMIT 1')
    returnValue = None
    for line in cur.fetchall():
        returnValue = line  
    return returnValue

def get_random_grade_id_line(cur):
    
    cur.execute('SELECT * FROM "Grade" ORDER BY random() DESC LIMIT 1')
    returnValue = None
    for line in cur.fetchall():
        returnValue = line   
    return returnValue
