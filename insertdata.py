import psycopg2
try:
   connection = psycopg2.connect(user="postgres",
                                  password="debten",
                                  host="192.168.40.214",
                                  port="5432",
                                  database="puskarda")
   PostgreSQL_select_Query = "select * from master_agama ORDER by nama"
   cursor = connection.cursor()
   cursor.execute(PostgreSQL_select_Query)
   records = cursor.fetchall()
   #print ("Printing first record", records)

   print("Print each row and it's columns values")
   for row in records:
       print( row[0], row[1], row[2], row[3], row[4], row[5],)
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
