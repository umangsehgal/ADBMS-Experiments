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

def insert_student_bulk(student_id, fileRange):
    with open('bulkIngestFile.csv', mode='w') as bulkIngestFile:
        for i in range(fileRange):
            # execute the INSERT statement
            studentCollegeId = syntheticDataGen.getStudentId()
            studentName = syntheticDataGen.getName()
            address = syntheticDataGen.getAddress()
            program = syntheticDataGen.getProgram()
            email = syntheticDataGen.getEmail()
        
            
            writer = csv.writer(bulkIngestFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([student_id+i,studentCollegeId,studentName,address,program,email])
    bulkIngestFile.close()

def writeBulkInsertTime(start,end):
    with open('bulkIngestFile.csv', 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    
    sql = """INSERT INTO "Student"("Student_Id", "Student_College_Id", "Student_Name", "Address", "Program", "Email") VALUES (%s,%s,%s,%s,%s,%s)"""
    a = datetime.datetime.now()
    cur.executemany(sql,your_list[start:end])
    b = datetime.datetime.now()

    time_dict_bulk[end-start]=(b-a).total_seconds()
    # print('Time Taken for bulk insert '+ str(end-start) +' records = ' + str(b-a))

def writeInsertTime(start,end):
    with open('bulkIngestFile.csv', 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    
    sql = """INSERT INTO "Student"("Student_Id", "Student_College_Id", "Student_Name", "Address", "Program", "Email") VALUES (%s,%s,%s,%s,%s,%s)"""
    
    a = datetime.datetime.now()
    for line in your_list[start:end]:
         cur.execute(sql, line)
    b = datetime.datetime.now()
    time_dict_serial[end-start]=(b-a).total_seconds()
    # print('Time Taken for serial insert'+ str(end-start) +' records = ' + str(b-a))

def queryInsertTime(): 
    #MAIN CODE
    student_id_current = getIds.get_student_id(cur)
    if(student_id_current is not None):
        insert_student_bulk(student_id_current+1, fileRange)
    else: 
        insert_student_bulk(1, fileRange)
    

#GENERATE CSV
queryInsertTime()
#BULK INSERT
rangeItems = [1, 5, 10, 20, 50, 100, 1000]
start=0

for i in range(0,len(rangeItems)):
    end = start+rangeItems[i] 
    writeBulkInsertTime(start,end)
    start = end 
    

#NORMAL INSERT
writeInsertTime(0,10000)

print("Serial Dict:")
print(time_dict_serial)
print("Bulk Dict:")
print(time_dict_bulk)


with open('experiemnt_results_unclustered.csv', mode='w') as resultFile:
    writer = csv.writer(resultFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Number of Records','Time Duration'])
    for k,v in time_dict_bulk.items(): 
        writer.writerow([k,v])

resultFile.close()

conn.commit()
cur.close() 
