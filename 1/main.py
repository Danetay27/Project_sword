def scan_words():
    text_file = open(f'./1/words.txt','r')
    content = text_file.read()  
    lines = content.splitlines()   
    return lines

 
def find_letters(words): 
    a =words[0]
    b=words[1]
    c=words[2]
    d = words[3]
    f = words[4]
    l =len(words)
    # for i in range(l):