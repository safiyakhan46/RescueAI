from core.gemini import client, MODEL


response = client.models.generate_content(
    model=MODEL,
    contents="Say hello to RescueAI in one short sentence."
)


print(response.text)