# Hospital-management-System
Project Overview

The Hospital Management System is a simple database-driven application developed using Python and MySQL.
It is designed to manage hospital operations such as patient records, doctor details, appointments, billing, and admission status.

This project demonstrates Python Database Connectivity (PDBC) along with basic Object-Oriented Programming (OOP) concepts.

🚀 Features
👤 Patient Registration
👨‍⚕️ Doctor Management
📅 Appointment Booking
🏥 Admit / Discharge Patients
🔍 Search Patient Details
💰 Bill Generation
📊 View Records
🛠️ Technologies Used
Python
MySQL
mysql-connector-python
📂 Project Structure
hospital/
│
├── db.py              # Database connection and table creation
├── patient.py         # Patient module
├── doctor.py          # Doctor module
├── appointment.py     # Appointment module
├── billing.py         # Billing module
├── main.py            # Main menu-driven program
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/hospital-management.git
cd hospital-management
2️⃣ Install Dependencies
pip install mysql-connector-python
3️⃣ Setup MySQL Database
Create a database named:
CREATE DATABASE hospital_db;
Update credentials in db.py:
host="localhost"
user="root"
password="your_password"
database="hospital_db"
▶️ How to Run
python main.py
