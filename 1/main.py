import json
def scan_words():
    text_file = open(f'./1/words.txt','r')
    content = text_file.read()  
    lines = content.splitlines()   
    return lines

def find_letters(words): 
    
    height = 20
    width = 40
    list1 = []
    base_word = words[0]
    start_col = 5
    start_row = 7
    letter_base = list(base_word)
    
    for i in range(height):
        row = [' '] * width
        for j in range(i):
            row.append(' ')
        list1.append(row)
    
   
    for i, ch in enumerate(base_word):
        list1[start_row+i][start_col] = ch
    
    for w in words[1:]:
        for letter in w:
            
            if letter in letter_base:
                h_ind = w.index(letter)
                v_ind = base_word.index(letter)
                
                cross_row = start_row +v_ind
                cross_col = start_col-h_ind
                
                place = True
                for i, ch in enumerate(w):
                    
                    ch1= list1[cross_row][cross_col+i]
                    if ch1 != ' ' and ch1 != ch:
                            can_place = False
                            break
                if place:
                    for i, ch in enumerate(w):
                        list1[cross_row][cross_col + i] = ch
                    
                       
                    letter_base.remove(letter)
                    break
                
                
       
    for row in list1:
        print(' '.join(row))


words = scan_words()
find_letters(words)



data = {
    "words": ['календарь', 'капуста', 'паста', 'лента', 'ель', 'малина', 'мода', 'аккорд', 'радуга'],  
    "hints": ["способ счисления дней в году", "овощь", "зубная", "Узкая полоса ткани", "хвойное дерево","",""], 
}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)