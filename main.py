from patient import patient
from doctor import doctor
from appointment import appointment
from billing import billing

p = patient()
d = doctor()
a = appointment()
b = billing()

while True:
    print("\n1.Register Patient\n2.Add Doctor\n3.Book Appointment\n4.Admit\n5.Discharge\n6.Search Patient\n7.Generate Bill\n8.View Doctors\n9.View Appointments\n10.View Patients\n11.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        p.register(
            input("Name: "),
            int(input("Age: ")),
            input("Gender: "),
            input("Disease: ")
        )

    elif ch == 2:
        d.add_doctor(
            input("Doctor Name: "),
            input("Specialization: "),
            int(input("Fees: "))
        )

    elif ch == 3:
        a.book(
            int(input("Patient ID: ")),
            int(input("Doctor ID: "))
        )

    elif ch == 4:
        p.admit(int(input("Patient ID: ")))

    elif ch == 5:
        p.discharge(int(input("Patient ID: ")))

    elif ch == 6:
        p.search(int(input("Patient ID: ")))

    elif ch == 7:
        b.generate(
            int(input("Patient ID: ")),
            int(input("Amount: "))
        )

    elif ch == 8:
        d.view_doctors()

    elif ch == 9:
        a.view_appointments()

    elif ch == 10:
        p.view_all()

    elif ch == 11:
        print("Exiting...")
        break