from services.conversation import ConversationEngine


engine = ConversationEngine()


result = engine.process_message(
    """
    My brother fell down the stairs about 20 minutes ago.
    He hit his head and is now dizzy.
    """
)


print("\n=== INCIDENT ===")
print(result["incident"].model_dump_json(indent=2))


print("\n=== TRIAGE ===")
print(result["triage"].model_dump_json(indent=2))


print("\n=== HISTORY ===")
print(engine.get_history())