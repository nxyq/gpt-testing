from transformers import pipeline

chatbot = pipeline("text-generation", model="gpt2")
while True:
    prompt = input("You: ")
    response = chatbot(prompt, max_length=50, do_sample=True)[0]['generated_text']
    print(f"AI: {response}")
