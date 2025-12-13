def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for character in text.lower(): 
        if character in chars:
            chars[character] += 1
        elif character == ' ':
            continue
        else:
            chars[character] = 1
    return chars

def dict_to_list(dictonairy):
    result = []
    for key, value in dictonairy.items():
        result.append({
            'char': key,
            'num': value,
            })
    return result

def sort_on(item):
     return item["num"]

def sort_chars(char_dict):
    chars_list = dict_to_list(char_dict)
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

