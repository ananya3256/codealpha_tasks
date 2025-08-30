# Basic Chatbot using if-elif, functions, loops, and input/output

def chatbot():
    print("Chatbot: Hello! I am your simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()   # convert input to lowercase for easy matching
        
        if user_input == "hello":
            print("Chatbot: Hi! 👋")
        
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks! How about you?")
        
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day 😊")
            break   # exit the loop and end the chatbot
        
        else:
            print("Chatbot: Sorry, I don't understand that.")
            

# Run the chatbot
chatbot()