#!/usr/bin/python
import syntheticDataGen
import psycopg2
import getIds
import executeQuery

insertRange = 10
conn = psycopg2.connect("host=imt-563-db-hnsu.cs3bxymxzkz8.us-east-2.rds.amazonaws.com dbname=hnsu563db user=hnsu563 password=alohomora")
cur = conn.cursor()

for i in range(insertRange):
    # Insert Student Table
    student_id_current = getIds.get_student_id(cur)
    if(student_id_current == None):
        executeQuery.insert_student("1",cur)
    else:
        executeQuery.insert_student(student_id_current+1,cur)

# Insert Department Table

    department_id_current = getIds.get_department_id(cur)
    if(department_id_current == None):
        executeQuery.insert_department("1",cur)
    else:
        executeQuery.insert_department(department_id_current+1,cur)

# Insert Faculty Table

    faculty_id_current = getIds.get_faculty_id(cur)
    if(faculty_id_current == None):
        executeQuery.insert_faculty("1",cur)
    else:
        executeQuery.insert_faculty(faculty_id_current+1,cur)

# Insert Course Table

    course_id_current = getIds.get_course_id(cur)
    if(course_id_current == None):
        executeQuery.insert_course("1",cur)
    else:
        executeQuery.insert_course(course_id_current+1,cur)

# Insert Grade Table

    grade_id_current = getIds.get_grade_id(cur)
    if(grade_id_current == None):
        executeQuery.insert_grade("1",cur)
    else:
        executeQuery.insert_grade(grade_id_current+1,cur)

# Insert Enrollment Table

    reg_id_current = getIds.get_reg_id(cur)
    if(reg_id_current == None):
        executeQuery.insert_reg("1",cur)
    else:
        executeQuery.insert_reg(reg_id_current+1,cur)



conn.commit()
cur.close() 
