def word_count(text):
    words = text.split()
    word_count = len(words)
    return word_count

def char_count(text):

    lower_text = text.lower()

    character_dict = {}

    for char in lower_text:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    
    return character_dict    

def sort_count(dict):
    for letter in dict:
        count = dict[letter]
        if letter.isalpha():
            print(f"{letter}: {count}")
        else:
            pass
    
    
        
