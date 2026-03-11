import csv
import random
from faker import Faker

fake = Faker()

diseases = [
"Diabetes","Hypertension","Asthma","Heart Disease","Arthritis",
"Kidney Stones","Migraine","Thyroid Disorder","Flu","Bronchitis",
"Pneumonia","Tuberculosis","Anemia","Depression","Allergy",
"Skin Infection","COVID-19","Back Pain","Gastritis","Obesity",
"Epilepsy","Glaucoma","Cataract","Liver Disease","Pancreatitis"
]

tests = [
"Blood Sugar","Blood Pressure","Cholesterol","ECG","MRI",
"CT Scan","X-Ray","Hemoglobin","Urine Test","Liver Function Test",
"Kidney Function Test","Thyroid Test","Vitamin D Test"
]

medicines = [
"Metformin","Amlodipine","Aspirin","Salbutamol","Ibuprofen",
"Paracetamol","Cetirizine","Atorvastatin","Amoxicillin",
"Omeprazole","Losartan","Azithromycin","Pantoprazole"
]

# Generate doctor list
doctors = [f"Dr. {fake.name()}" for _ in range(50)]


# PATIENTS
with open("data/healthcare_data/patients.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["patient_id","name","age","gender","blood_group","disease","doctor","city"])

    for i in range(1,1001):
        writer.writerow([
            f"P{i:05}",
            fake.name(),
            random.randint(18,85),
            random.choice(["Male","Female"]),
            random.choice(["A+","B+","O+","AB+","O-","A-","B-"]),
            random.choice(diseases),
            random.choice(doctors),
            fake.city()
        ])


# APPOINTMENTS
with open("data/healthcare_data/appointments.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["appointment_id","patient_id","doctor","date","time","status"])

    for i in range(1,1501):
        writer.writerow([
            f"A{i:05}",
            f"P{random.randint(1,1000):05}",
            random.choice(doctors),
            fake.date_this_year(),
            fake.time(),
            random.choice(["Completed","Scheduled","Cancelled"])
        ])


# LAB REPORTS
with open("data/healthcare_data/lab_reports.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["report_id","patient_id","test_name","result","date"])

    for i in range(1,800):
        writer.writerow([
            f"R{i:05}",
            f"P{random.randint(1,1000):05}",
            random.choice(tests),
            random.randint(50,200),
            fake.date_this_year()
        ])


# PRESCRIPTIONS
with open("data/healthcare_data/prescriptions.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["prescription_id","patient_id","medicine","dosage","doctor"])

    for i in range(1,1200):
        writer.writerow([
            f"PR{i:05}",
            f"P{random.randint(1,1000):05}",
            random.choice(medicines),
            f"{random.randint(1,3)} tablets/day",
            random.choice(doctors)
        ])

print("Large realistic healthcare dataset generated successfully!")