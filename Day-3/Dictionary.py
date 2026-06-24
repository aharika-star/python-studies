patient = {
    "patient_name": "Rahul",
    "age": 32,
    "hospital": "Sunrise Hospital",
    "disease": "Migraine",
    "room_no": 205,
    "doctor": "Dr. Mehta",
    "admitted": True
}

print(patient)
print(patient["patient_name"])     
print(patient["doctor"])          
print(patient["room_no"])         
print(patient.get("blood_group", "Not Available"))
