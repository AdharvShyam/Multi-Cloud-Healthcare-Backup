import csv
import random

# Sample data
names = ["Arjun", "Ravi", "Neha", "Asha", "Rahul", "Sneha", "Kiran", "Anjali", "Vikram", "Meera"]
diseases = ["Diabetes", "Hypertension", "Asthma", "Heart Disease", "Arthritis"]
doctors = ["Dr. Sharma", "Dr. Mehta", "Dr. Rao", "Dr. Kapoor", "Dr. Verma"]
medicines = ["Metformin", "Amlodipine", "Aspirin", "Salbutamol", "Ibuprofen"]

# Generate patients
with open("data/healthcare_data/patients.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["patient_id","name","age","gender","blood_group","disease","doctor"])

    for i in range(1,501):
        writer.writerow([
            f"P{i:03}",
            random.choice(names),
            random.randint(20,80),
            random.choice(["Male","Female"]),
            random.choice(["A+","B+","O+","AB+","O-"]),
            random.choice(diseases),
            random.choice(doctors)
        ])

# Generate appointments
with open("data/healthcare_data/appointments.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["appointment_id","patient_id","doctor","date","time","status"])

    for i in range(1,701):
        writer.writerow([
            f"A{i:03}",
            f"P{random.randint(1,500):03}",
            random.choice(doctors),
            f"2026-03-{random.randint(1,28)}",
            f"{random.randint(9,17)}:{random.choice(['00','15','30','45'])}",
            random.choice(["Completed","Scheduled"])
        ])

# Generate lab reports
with open("data/healthcare_data/lab_reports.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["report_id","patient_id","test_name","result","date"])

    tests = ["Blood Sugar","ECG","Blood Pressure","Cholesterol"]

    for i in range(1,401):
        writer.writerow([
            f"R{i:03}",
            f"P{random.randint(1,500):03}",
            random.choice(tests),
            random.randint(80,200),
            f"2026-03-{random.randint(1,28)}"
        ])

# Generate prescriptions
with open("data/healthcare_data/prescriptions.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["prescription_id","patient_id","medicine","dosage","doctor"])

    for i in range(1,601):
        writer.writerow([
            f"PR{i:03}",
            f"P{random.randint(1,500):03}",
            random.choice(medicines),
            f"{random.randint(1,2)} tablet/day",
            random.choice(doctors)
        ])

print("Healthcare dataset generated successfully!")