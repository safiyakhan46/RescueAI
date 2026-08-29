from services.conversation import ConversationEngine


engine = ConversationEngine()


print("\n========== MESSAGE 1 ==========")

result = engine.process_message(
    "My brother fell down the stairs and he's dizzy."
)

print(result["incident"].model_dump_json(indent=2))


print("\n========== MESSAGE 2 ==========")

result = engine.process_message(
    "He didn't pass out."
)

print(result["incident"].model_dump_json(indent=2))


print("\n========== MESSAGE 3 ==========")

result = engine.process_message(
    "He's breathing normally."
)

print(result["incident"].model_dump_json(indent=2))