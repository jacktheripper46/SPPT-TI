from flask import Flask
from flask import jsonify

import psycopg2
import psycopg2.extras
import json

app = Flask(__name__)

@app.route('/')
def index():
    data=opendb()
    return jsonify(data)

def opendb():
    #records = {}
    #print("Open DB")
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="debten",
                                  host="192.168.10.107",
                                  port="5432",
                                  database="puskarda")
        PostgreSQL_select_Query = "select * from master_agama"
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        #cursor = connection.cursor()
        #print("Open")
        cursor.execute(PostgreSQL_select_Query)
        records = cursor.fetchall()
        result = records
   #print ("Printing first record", records)

        #print("Print each row and it's columns values")
        #for row in records:
        #    print(row)
            result[]["Id"] = row[row(1)]
        #    print( row[0], row[1])
    #print("Id = ", row[1], )
    #print("Kode = ", row[2])
    #print("Nama = ", row[3])
    #print("Created = ", row[4])
    #print("Updated  = ", row[5], "\n")

#   records_two = cursor.fetchone()
#   print("Printing second record", records_two)
#   records_three = cursor.fetchone()
#   print("Printing second record", records_three)
#   records_four = cursor.fetchone()
#   print("Printing second record", records_four)
    except (Exception, psycopg2.Error) as error :
        print ("Error while getting data from PostgreSQL", error)
    finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    return records
if (__name__ == "__main__"):
	app.run(host = '0.0.0.0', port = 8000)
