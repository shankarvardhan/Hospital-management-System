from db import cursor, db

class billing:

    def generate(self, pid, amount):
        cursor.execute(
            "INSERT INTO bills(patient_id, amount) VALUES (%s,%s)",
            (pid, amount)
        )
        db.commit()
        print(" Bill Generated")