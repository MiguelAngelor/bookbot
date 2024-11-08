def main(): 

#Word Counter
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    TotalWords = len(words) 
    
    print(f"{TotalWords} words found in the document.")



main()