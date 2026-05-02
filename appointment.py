from db import cursor, db

class appointment:

    def book(self, pid, did):
        cursor.execute(
            "INSERT INTO appointments(patient_id, doctor_id, date) VALUES (%s,%s,CURDATE())",
            (pid, did)
        )
        db.commit()
        print(" Appointment Booked")

    def view_appointments(self):
        cursor.execute("SELECT * FROM appointments")
        for row in cursor.fetchall():
            print(row)