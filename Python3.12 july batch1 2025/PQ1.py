# Base class
class Person:
    def __init__(self, name, age, gender, mobile):
        self.name = name
        self.age = age
        self.gender = gender
        self.mobile = mobile

# Doctor class
class Doctor(Person):
    def __init__(self, name, age, gender, mobile, specialization):
        super().__init__(name, age, gender, mobile)
        self.specialization = specialization

    def display(self):
        print(f"Doctor Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Mobile: {self.mobile}, Specialization: {self.specialization}")

# Patient class
class Patient(Person):
    def __init__(self, name, age, gender, mobile, patient_id):
        super().__init__(name, age, gender, mobile)
        self.patient_id = patient_id
        self.medical_history = []

    def display(self):
        print(f"Patient Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Mobile: {self.mobile}, Patient ID: {self.patient_id}")

# MedicalRecord class
class MedicalRecord:
    def __init__(self, diagnosis, treatment, date):
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.date = date

    def display(self):
        print(f"Date: {self.date}, Diagnosis: {self.diagnosis}, Treatment: {self.treatment}")

# Hospital Management System
class HospitalManagementSystem:
    def __init__(self):
        self.doctors = []
        self.patients = []

    # Doctor operations
    def add_doctor(self):
        name = input("Enter doctor name: ")
        age = int(input("Enter age: "))
        gender = input("Enter gender: ")
        mobile = input("Enter mobile number: ")
        specialization = input("Enter specialization: ")
        self.doctors.append(Doctor(name, age, gender, mobile, specialization))
        print("Doctor added successfully!\n")

    def view_doctors(self):
        print("\n--- Doctors List ---")
        if not self.doctors:
            print("No doctors found.")
        for doc in self.doctors:
            doc.display()
        print()

    def update_doctor(self):
        mobile = input("Enter doctor's mobile number to update: ")
        for doc in self.doctors:
            if doc.mobile == mobile:
                doc.name = input("Enter new name: ")
                doc.age = int(input("Enter new age: "))
                doc.gender = input("Enter new gender: ")
                doc.specialization = input("Enter new specialization: ")
                print("Doctor updated successfully!\n")
                return
        print("Doctor not found!\n")

    def delete_doctor(self):
        mobile = input("Enter doctor's mobile number to delete: ")
        for doc in self.doctors:
            if doc.mobile == mobile:
                self.doctors.remove(doc)
                print("Doctor deleted successfully!\n")
                return
        print("Doctor not found!\n")

    # Patient operations
    def add_patient(self):
        name = input("Enter patient name: ")
        age = int(input("Enter age: "))
        gender = input("Enter gender: ")
        mobile = input("Enter mobile number: ")
        patient_id = input("Enter patient ID: ")
        self.patients.append(Patient(name, age, gender, mobile, patient_id))
        print("Patient added successfully!\n")

    def view_patients(self):
        print("\n--- Patients List ---")
        if not self.patients:
            print("No patients found.")
        for pat in self.patients:
            pat.display()
        print()

    def update_patient(self):
        mobile = input("Enter patient's mobile number to update: ")
        for pat in self.patients:
            if pat.mobile == mobile:
                pat.name = input("Enter new name: ")
                pat.age = int(input("Enter new age: "))
                pat.gender = input("Enter new gender: ")
                pat.patient_id = input("Enter new patient ID: ")
                print("Patient updated successfully!\n")
                return
        print("Patient not found!\n")

    def delete_patient(self):
        mobile = input("Enter patient's mobile number to delete: ")
        for pat in self.patients:
            if pat.mobile == mobile:
                self.patients.remove(pat)
                print("Patient deleted successfully!\n")
                return
        print("Patient not found!\n")

    # Medical history
    def add_medical_record(self):
        mobile = input("Enter patient's mobile number: ")
        for pat in self.patients:
            if pat.mobile == mobile:
                diagnosis = input("Enter diagnosis: ")
                treatment = input("Enter treatment: ")
                date = input("Enter date (YYYY-MM-DD): ")
                pat.medical_history.append(MedicalRecord(diagnosis, treatment, date))
                print("Medical record added successfully!\n")
                return
        print("Patient not found!\n")

    def view_medical_history(self):
        mobile = input("Enter patient's mobile number: ")
        for pat in self.patients:
            if pat.mobile == mobile:
                print(f"\n--- Medical History for {pat.name} ---")
                if not pat.medical_history:
                    print("No medical records found.")
                for record in pat.medical_history:
                    record.display()
                print()
                return
        print("Patient not found!\n")

# ------------------------------
# Main menu
# ------------------------------
hospital = HospitalManagementSystem()

while True:
    print("===== Hospital Management System =====")
    print("1. Add Doctor")
    print("2. View Doctors")
    print("3. Update Doctor")
    print("4. Delete Doctor")
    print("5. Add Patient")
    print("6. View Patients")
    print("7. Update Patient")
    print("8. Delete Patient")
    print("9. Add Medical Record")
    print("10. View Medical History")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        hospital.add_doctor()
    elif choice == "2":
        hospital.view_doctors()
    elif choice == "3":
        hospital.update_doctor()
    elif choice == "4":
        hospital.delete_doctor()
    elif choice == "5":
        hospital.add_patient()
    elif choice == "6":
        hospital.view_patients()
    elif choice == "7":
        hospital.update_patient()
    elif choice == "8":
        hospital.delete_patient()
    elif choice == "9":
        hospital.add_medical_record()
    elif choice == "10":
        hospital.view_medical_history()
    elif choice == "0":
        print("Exiting system...")
        break
    else:
        print("Invalid choice. Try again!\n")
