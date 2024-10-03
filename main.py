def main():
    count = 0
    with open('books/frankenstein.txt', encoding='utf-8') as f:
        file_contents = f.read()

    char_dict = {}

    for letter in file_contents:
        letter = letter.lower()
        if letter in char_dict:
            
            char_dict[letter] += 1
        else:
            
            char_dict[letter] = 1
            
        
    for key in char_dict:
        print(f"The '{key}' character was found {char_dict[key]} times")
    print("--- END REPORT ---")
        

main()