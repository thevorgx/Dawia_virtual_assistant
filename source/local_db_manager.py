import pickle
import os

def load_chat_history():
    if os.path.exists("chat_history.pkl"):
        with open("chat_history.pkl", 'rb') as f:
            return pickle.load(f)
    else:
        return []

def save_chat_history(messages):
    with open('chat_history.pkl', 'wb') as f:
        pickle.dump(messages, f)

def clear_chat_db():
    """Clear the chat history database."""
    with open('chat_history.pkl', 'wb') as f:
        pickle.dump([], f)
