patient = {
    "name": "Rahul",
    "age": 25,
    "disease": "Fever"
}

print("Before Update:")
print(patient)

patient["age"] = 26
patient["disease"] = "Cold"

patient["doctor"] = "Dr. Sharma"

print("\nAfter Update:")
print(patient)
