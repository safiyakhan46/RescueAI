from services.intake import extract_incident


message = """
My brother fell down the stairs about 20 minutes ago.
He hit his head and now he's dizzy and has a headache.
I don't know if he lost consciousness.
"""


incident = extract_incident(message)

print("\n--- EXTRACTED INCIDENT ---\n")
print(incident.model_dump_json(indent=2))