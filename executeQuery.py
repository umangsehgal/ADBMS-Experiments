import syntheticDataGen
import getIds

def insert_student(student_id,cur):
    """ insert a new student into the students table """
    sql = """INSERT INTO "Student"("Student_Id", "Student_College_Id", "Student_Name", "Address", "Program", "Email") VALUES (%s,%s,%s,%s,%s,%s)"""
    
    # execute the INSERT statement
    studentCollegeId = syntheticDataGen.getStudentId()
    studentName = syntheticDataGen.getName()
    address = syntheticDataGen.getAddress()
    program = syntheticDataGen.getProgram()
    email = syntheticDataGen.getEmail()
    cur.execute(sql, (student_id,studentCollegeId,studentName,address,program,email))

def insert_department(department_id,cur):
    """ insert a new student into the department table """
    sql = """INSERT INTO "Department"("Department_ID", "Department_College_ID", "Department_Name", "Department_Location", "Department_Mail") VALUES (%s,%s,%s,%s,%s)"""
    
    # execute the INSERT statement
    departmentCollegeId = syntheticDataGen.getProgram()+str(syntheticDataGen.getStudentId())
    departmentName = syntheticDataGen.getProgram()
    departmentLocation = syntheticDataGen.getAddress() 
    departmentMail = syntheticDataGen.getCity()
    cur.execute(sql, (department_id,departmentCollegeId,departmentName,departmentLocation,departmentMail))


def insert_faculty(faculty_id,cur):
    """ insert a new student into the faculty table """
    sql = """INSERT INTO public."Faculty"("Faculty_Id", "Faculty_Name", "Qualification", "Salary", "Contact_Info", "Email_Id", "Department_Id", "Faculty_College_Id")VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    # execute the INSERT statement
    departmentCollegeId = getIds.get_random_department_id(cur)
    facultyCollegeId = syntheticDataGen.getStudentId()
    facultyName = syntheticDataGen.getProgram()
    qualif = syntheticDataGen.getCity()
    salary = syntheticDataGen.getComputedScore()
    facultyContact = syntheticDataGen.getAddress() 
    facultyEmail = syntheticDataGen.getEmail()
    cur.execute(sql, (faculty_id, facultyName, qualif, salary, facultyContact, facultyEmail, departmentCollegeId, facultyCollegeId ))

def insert_course(course_id,cur):
    """ insert a new student into the faculty table """
    sql = """INSERT INTO "Course"("Course_ID", "College_Course_ID ", "Course_Name", "Course_Capacity", "Credits", "Department_ID", "Year_Offered", "Term_Offered", "Instructor_ID") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    # execute the INSERT statement
    departmentCollegeId = getIds.get_random_department_id(cur)
    instructorid = getIds.get_random_instructor_id(cur)
    courseCollegeId = getIds.get_random_department_id(cur)
    year = syntheticDataGen.getCreatedTime()
    courseName = syntheticDataGen.getProgram()
    capacity = syntheticDataGen.getComputedScore()
    credit = syntheticDataGen.getsingleDigit()
    cur.execute(sql, (course_id,courseCollegeId, courseName, capacity, credit, departmentCollegeId, year, credit, instructorid  ))

def insert_grade(grade_id,cur):
    """ insert a new student into the faculty table """
    sql = """INSERT INTO "Grade"("Grade_ID", "GPA") VALUES (%s, %s)"""
    # execute the INSERT statement
    gpa = syntheticDataGen.getComputedGrade()
    cur.execute(sql, (grade_id, "%.2f" % gpa))

def insert_reg(reg_id,cur):
    """ insert a new student into the faculty table """
    sql = """INSERT INTO "Enrollment"("Registration_Id", "Registration_Number", "Student_Id", "Course_Id", "Enrollment_Start_Date", "Enrollment_End_Date", "Grade_Id", "Credits_Awarded") VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""
    # execute the INSERT statement
    registrationNumber = 'REG'+ str(syntheticDataGen.getStudentId())
    studentId = getIds.get_random_student_id(cur)
    courseId_line = getIds.get_random_course_id_line(cur)
    startDate = syntheticDataGen.getCreatedTime()
    endDate = syntheticDataGen.getCreatedTime()
    gradeId_line = getIds.get_random_grade_id_line(cur)
    cur.execute(sql, (reg_id, registrationNumber, studentId, courseId_line[0], startDate, endDate, gradeId_line[0], gradeId_line[1]* courseId_line[4]))
