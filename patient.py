from db import cursor, db

class patient:

    def register(self, name, age, gender, disease):
        cursor.execute(
            "INSERT INTO patients(name, age, gender, disease) VALUES (%s,%s,%s,%s)",
            (name, age, gender, disease)
        )
        db.commit()
        print("Patient Registered")

    def admit(self, pid):
        cursor.execute("UPDATE patients SET admitted=TRUE WHERE patient_id=%s", (pid,))
        db.commit()
        print(" Patient Admitted")

    def discharge(self, pid):
        cursor.execute("UPDATE patients SET admitted=FALSE WHERE patient_id=%s", (pid,))
        db.commit()
        print(" Patient Discharged")

    def search(self, pid):
        cursor.execute("SELECT * FROM patients WHERE patient_id=%s", (pid,))
        res = cursor.fetchone()
        if res:
            print(res)
        else:
            print(" Patient Not Found")

    def view_all(self):
        cursor.execute("SELECT * FROM patients")
        for row in cursor.fetchall():
            print(row)