def main(): 
    print("--- Starting the report of books/frankenstein.txt ---")

#Part I: Word Counter
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    TotalWords = len(words) 
    
    print(f"{TotalWords} words found in the document.")

#Part II: Character Counter
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents
    LowerWords = words.lower()

    characters={}
    for l in LowerWords:
        if l.isalpha():
            if l not in characters:
                characters[l] = 1
            else:
                characters[l] += 1
        else:
            continue
    
#List of dictionaries
    char_list = []

    for k, v in characters.items():
        new_dict = {"letter": k, "frequency":v}
        char_list.append(new_dict)

#Sorting the list of dictionaries
    # function that takes a dictionary and returns the value of the frequency key
    #for .sort()
    def sort_on(dic):
        return dic["frequency"]
    
# Sorting them:
    char_list.sort(key=sort_on, reverse=True)

#priting the results for each character
    for l in char_list:
        print(f"The {l['letter']} was found {l['frequency']} times.")

    print("--- Completed! ---")
 
main()