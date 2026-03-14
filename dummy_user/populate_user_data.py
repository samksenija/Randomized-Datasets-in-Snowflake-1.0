import sys
sys.path.insert(0, "../connections") 

import connection_snowflake
import generate_random_user

#Here, name, surname & email address will be generated in order to 
#Complete the random data population for doctors & patients
cursor = connection_snowflake.conn.cursor()


insert_name_surname_and_email_address = """
    INSERT INTO DUMMY_DATASETS.SCHEMA_FOR_DUMMY_DATA.DUMMY_DOCTOR_INFORMATION (first_name, last_name, email) VALUES (?, ?, ?)
"""

information = generate_random_user.generate_random_name_and_surname(1000)

cursor.executemany(insert_name_surname_and_email_address, information)

connection_snowflake.conn.commit()

cursor.close()