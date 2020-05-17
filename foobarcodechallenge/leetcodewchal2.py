
def arrangeWords(text) -> str:

    words = text.split()  
    str=" "
    words.sort(key=len,reverse=False)
    return (str.join(words).capitalize())
    # for w in words:
        # print(w)



print(arrangeWords("Leetcode is cool"))