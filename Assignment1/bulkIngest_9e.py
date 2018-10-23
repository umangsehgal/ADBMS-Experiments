#!/usr/bin/python
import syntheticDataGen
import psycopg2
import getIds
import executeQuery
import csv
import datetime


time_dict_serial = {}
time_dict_bulk = {}

fileRange = 10000
conn = psycopg2.connect("host=imt-563-db-hnsu.cs3bxymxzkz8.us-east-2.rds.amazonaws.com dbname=hnsu563db user=hnsu563 password=sehgalu123")
cur = conn.cursor()

def insert_faculty_bulk(faculty_id, fileRange):
    with open('bulkIngestFile_faculty.csv', mode='w') as bulkIngestFile:
        for i in range(fileRange):
            departmentCollegeId = getIds.get_random_department_id(cur)
            facultyCollegeId = syntheticDataGen.getStudentId()
            facultyName = syntheticDataGen.getProgram()
            qualif = syntheticDataGen.getCity()
            salary = syntheticDataGen.getComputedScore()
            facultyContact = syntheticDataGen.getAddress()[:45]
            facultyEmail = syntheticDataGen.getEmail()
    
            
            writer = csv.writer(bulkIngestFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([faculty_id+i,facultyName, qualif, salary, facultyContact, facultyEmail, departmentCollegeId ])
    bulkIngestFile.close()

def writeBulkInsertTime(start,end):
    with open('bulkIngestFile_faculty.csv', 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    
    sql = """INSERT INTO public."Faculty"("Faculty_Id", "Faculty_Name", "Qualification", "Salary", "Contact_Info", "Email_Id", "Department_Id")VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    a = datetime.datetime.now()
    cur.executemany(sql,your_list[start:end])
    b = datetime.datetime.now()

    time_dict_bulk[end-start]=(b-a).total_seconds()
    # print('Time Taken for bulk insert '+ str(end-start) +' records = ' + str(b-a))

def writeInsertTime(start,end):
    with open('bulkIngestFile_faculty.csv', 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    
    sql = """INSERT INTO public."Faculty"("Faculty_Id", "Faculty_Name", "Qualification", "Salary", "Contact_Info", "Email_Id", "Department_Id")VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    
    a = datetime.datetime.now()
    for line in your_list[start:end]:
         cur.execute(sql, line)
    b = datetime.datetime.now()
    time_dict_serial[end-start]=(b-a).total_seconds()
    # print('Time Taken for serial insert'+ str(end-start) +' records = ' + str(b-a))

def queryInsertTime(): 
    #MAIN CODE
    faculty_id_current = getIds.get_faculty_id(cur)
    if(faculty_id_current is not None):
        insert_faculty_bulk(faculty_id_current+1, fileRange)
    else: 
        insert_faculty_bulk(1, fileRange)
    

#GENERATE CSV
#queryInsertTime()
#BULK INSERT
rangeItems = [1, 5, 10, 20, 50, 100, 1000]
start=0

for i in range(0,len(rangeItems)):
    end = start+rangeItems[i] 
    writeBulkInsertTime(start,end)
    start = end 
    

#NORMAL INSERT
# writeInsertTime(0,10000)

print("Serial Dict:")
print(time_dict_serial)
print("Bulk Dict:")
print(time_dict_bulk)


with open('experiemnt_results_9e_unclustered.csv', mode='w') as resultFile:
    writer = csv.writer(resultFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Number of Records','Time Duration'])
    for k,v in time_dict_bulk.items(): 
        writer.writerow([k,v])

resultFile.close()

conn.commit()
cur.close() 
