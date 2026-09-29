import random
from datetime import datetime

responses = {
    "hello": [
        "Hello! 👋 What are you working on today?",
        "Hey! Nice to meet you!",
        "Hi there! How can I help?"
    ],

    "how are you": [
        "I'm running perfectly! 😄",
        "All systems are working!",
        "I'm doing great. Thanks for asking!"
    ],

    "python": [
        "Python is excellent for automation, AI and data science.",
        "Python keeps your code simple and readable.",
        "Are you learning Python for development or data analysis?"
    ],

    "internship": [
        "Projects are a great way to strengthen your internship profile.",
        "Try building projects instead of only collecting certificates.",
        "GitHub can help you showcase your projects."
    ],

    "motivation": [
        "Small progress every day becomes a big achievement.",
        "Don't compare your beginning with someone else's middle.",
        "Keep building. Your skills grow through practice."
    ],

    "bye": [
        "Goodbye! Keep coding! 🚀",
        "See you again!",
        "Bye! Have a productive day!"
    ]
}

print("=" * 50)
print("        🤖 NOVA - PYTHON CHATBOT")
print("=" * 50)

print("Type 'bye' whenever you want to leave.")

while True:

    user = input("\nYou: ").lower().strip()

    if not user:
        print("NOVA: Say something and I'll try to respond!")
        continue

    if user == "time":
        current_time = datetime.now().strftime("%I:%M %p")
        print("NOVA: The current time is", current_time)
        continue

    found = False

    for keyword, messages in responses.items():

        if keyword in user:

            print("NOVA:", random.choice(messages))
            found = True

            if keyword == "bye":
                print("\n🤖 Session ended.")
                exit()

            break

    if not found:

        if "thank" in user:
            print("NOVA: You're welcome! 😊")

        elif "name" in user:
            print("NOVA: I'm NOVA, your small Python chatbot.")

        elif "help" in user:
            print(
                "NOVA: You can talk to me about "
                "Python, internships, motivation or time."
            )

        else:
            print(
                "NOVA: Interesting! I don't have an answer "
                "for that yet, but I'm learning."
            )
