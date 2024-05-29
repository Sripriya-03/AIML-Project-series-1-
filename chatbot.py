
responses = {
    "hello": "Hello! Welcome to Chatbot",
    "thank you": " How can I help you?",
    "how are you": "I'm just a bot, but I'm doing great!",
    "what can you do": "I can chat with you and answer basic questions.How can i help you?",
    "which is the booming programming languages":"ofcourse,it is python!",
    "thank you":"You're Welcome",
    "who is the prime minister of India":"Narendra Modi",
    "thank you":"You're Welcome",
    "why do we need to study":"hahha!Thats's a funny question ,but we need to study to succeed",
    "thank you":"You're Welcome",
    "bye": " Have a great day!",
}


def get_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, "I'm sorry, I don't understand that.")
def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: " + responses["bye"])
            break
        response = get_response(user_input)
        print("Chatbot: " + response)

 
if __name__ == "__main__":
    chat()
