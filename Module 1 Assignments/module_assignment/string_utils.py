def capitalize_words(text:str):
    text_list = text.split()
    capitalize_words = ""
    for word in text_list:
        capitalize_words = capitalize_words + word.capitalize() + " "
        
    return capitalize_words.strip()

def reverse_string(text:str):
    return text[::-1]