import nltk
nltk.download('punkt') 

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def preprocess_input(input_text):
    tokens = word_tokenize(input_text.lower())
    stop_words = set(stopwords.words('english'))
    return {t for t in tokens if t.isalnum() and t not in stop_words}

def get_jaccard_similarity(set1, set2):
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    
    if len(union) == 0:
        return 0.0
    
    return len(intersection) / len(union)

def get_response(user_input):
    responses = {
        "hello": "Hello! How can I help you?",
        "how are you": "I'm just a chatbot, but thanks for asking!",
        "what's your name?": "I do not have a name. I'm just a robot",
        "bye": "Goodbye! Have a great day!",
    }
    
    preprocessed_input = preprocess_input(user_input)
    
    best_match = max(responses.keys(), key=lambda pattern: get_jaccard_similarity(preprocess_input(pattern), preprocessed_input))
    jaccard_similarity = get_jaccard_similarity(preprocess_input(best_match), preprocessed_input)
    
    if jaccard_similarity > 0.0:
        return responses[best_match]
    
    return "I'm sorry, I don't understand. Can you rephrase your question?"

def main():
    print("Chatbot: Hello! How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
            
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
