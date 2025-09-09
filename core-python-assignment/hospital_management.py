def search_patients_by_disease(patients, disease):
    result = [p["Name"] for p in patients if p["Disease"].lower() == disease.lower()]
    return result
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]

search_disease = "Flu"
matched_patients = search_patients_by_disease(patients, search_disease)
print(f"Patients with {search_disease}: {matched_patients}")