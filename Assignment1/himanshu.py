#!/usr/bin/python
import syntheticDataGen
import psycopg2
import getIds
import executeQuery
import csv
import datetime

def main():
    #Reads CSV:
    with open('/Users/umangsehgal/Downloads/Student_Data.csv', 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)

    #Execute Query
    conn = psycopg2.connect("host=imt-563-db-hnsu.cs3bxymxzkz8.us-east-2.rds.amazonaws.com dbname=hnsu563db user=hnsu563 password=sehgalu123")
    cur = conn.cursor()
    sql = """INSERT INTO "Student"("Student_Id", "Student_College_Id", "Student_Name", "Address", "Program", "Email") VALUES (%s,%s,%s,%s,%s,%s)"""
    a = datetime.datetime.now()
    cur.executemany(sql,your_list[:10])
    b = datetime.datetime.now()
    print('Time Taken = ' + str(b-a))
    conn.commit()
    cur.close() 
    
if __name__ == '__main__':
    main()