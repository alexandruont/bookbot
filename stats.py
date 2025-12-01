def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text: str) -> dict:
    lwr = text.lower()
    char_dict = {} #initializare dictionar
    for char in lwr: #pentru fiecare character din stringul aflat in variabila lower
        if char not in char_dict: #daca cheia char nu se afla deja in dictionar
            char_dict[char] = 1 # initializam cu 1
        else:
            char_dict[char] += 1 #daca se afla adaugam 1
    
    return char_dict


def sorted_dict(char_dict: dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char":char, "num":count})
    
    def sort_key(items):
        return items["num"]
    
    char_list.sort(key= sort_key, reverse=True)

    return char_list