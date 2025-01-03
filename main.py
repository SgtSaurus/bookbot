#Opens frankenstien.txt and copies it to string file_contents
def pull_book_text(path):
        with open(path) as f:
            return f.read()

#Returns the word count of the text
def get_word_count(text):
     return len(text.split())

#Returns the text as a string array
def text_to_array(text):
     return text.split()

#Returns the character count of the given text
def character_count(text_in_array):
    letter_count = {
        "a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0,
        "h" : 0, "i" : 0, "j" : 0, "k" : 0, "l" : 0, "m" : 0, "n" : 0,
        "o" : 0, "p" : 0, "q" : 0, "r" : 0, "s" : 0, "t" : 0, "u" : 0, 
        "v" : 0, "w" : 0, "x" : 0, "y" : 0, "z" : 0
    } 
    for word in text_in_array:
        lowered_word = word.lower()
        #print(lowered_word)
        letter_list = list(lowered_word)
        for l in letter_list:
            if(l.isalpha()):
                letter_count[l] += 1
    #print(letter_count)
    return letter_count


def title():
    print("--- Begin report of books/frankenstein.txt ---")

def end():
    print("--- End report ---")
#Creates Main Method where functions are called
def main():
    title()
    file_contents = pull_book_text("books/frankenstein.txt")
    
    print(str(get_word_count(file_contents)) + " words found in the document\n")
    char_array = character_count(text_to_array(file_contents))
    sorted_char_array = {}
    for key in sorted(char_array, key = char_array.get,reverse = True):
        sorted_char_array[key] = char_array[key]
    for key in sorted_char_array:
        print(f"The {key} character was found {sorted_char_array[key]} times")
    end()

#Runs the program
main()
