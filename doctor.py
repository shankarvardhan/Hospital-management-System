from db import cursor, db

class doctor:

    def add_doctor(self, name, specialization, fees):
        cursor.execute(
            "INSERT INTO doctors(name, specialization, fees) VALUES (%s,%s,%s)",
            (name, specialization, fees)
        )
        db.commit()
        print(" Doctor Added")

    def view_doctors(self):
        cursor.execute("SELECT * FROM doctors")
        for row in cursor.fetchall():
            print(row)