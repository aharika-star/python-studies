patients = [
    {"id": 101, "name": "Rahul", "disease": "Migraine"},
    {"id": 102, "name": "Sneha", "disease": "Fever"},
    {"id": 103, "name": "Arjun", "disease": "Allergy"}
]

for p in patients:
    print(f"[{p['id']}] {p['name']} - {p['disease']}")

def register_patient(name, age, disease):
    return {
        "name": name,
        "age": age,
        "disease": disease
    }

patient = register_patient("Meera", 30, "Back Pain")

print(patient)
