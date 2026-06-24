# EXERCISE 1 :

patient_name = input("Enter patient name: ")
department = input("Enter department: ")
doctor_name = input("Enter doctor name: ")

print(f"Patient {patient_name} registered in {department} under Dr. {doctor_name}")

# EXERCISE 2 :

def check_insurance_available(insurance_available):
    if insurance_available:
        print("Insurance details available")
    else:
        print("Insurance details not available - PLEASE VERIFY")

check_insurance_available(True)
check_insurance_available(False)
