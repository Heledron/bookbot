
def main():
    character_count()
    word_count()

    
    report()
def read_book():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)


def word_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_counter= 0
        word_list=file_contents.split()
        
        for word in word_list:
            word_counter += 1
    return word_counter#, print(word_counter)
word_counter=word_count() 


def character_count():
    counter_dict ={}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read() 
        lower_file_contents = file_contents.lower()
        
        word_list=lower_file_contents.split()
        for word in word_list:
            for letter in word:
                if letter in counter_dict:
                    counter_dict[letter]= counter_dict[letter]+1
                else:
                    counter_dict[letter]= 1
    return counter_dict #, print(counter_dict)
character_counter=character_count()

def report():
    print("--- Begin report of books/frankenstein.txt ---\n"
          f"{word_counter} words found in the document")
    dict_keys=[]
    for dict_key in character_counter.keys():
        dict_keys.append(dict_key)


    alph_only=[]
    for key in dict_keys:
        if key.isalpha() ==True:
            alph_only.append(key)

    alph_only.sort()
   
    
    length = alph_only.__len__()
   
    for i in range(0,length):
        print(f"The '{alph_only[i]}' character was found {character_counter[alph_only[i]]} times")
    print("--- End report ---")

          

if __name__ == "__main__":
    main()
