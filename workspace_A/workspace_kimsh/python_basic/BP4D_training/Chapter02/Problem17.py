str="tomato potato pineapple carrot watermelon hello @#$%^&*()?!||"
def longest_word(str):
    word_final=''
    word_holder=''
    for w in str:
        #print(w)
        if w in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            word_holder=word_holder+w
            #print(word_holder)
            
            if len(word_final) <len(word_holder):
                word_final=word_holder
                #print(word_final)
                
        if w not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            word_holder=''
            
    return word_final

            
print(longest_word(str))
