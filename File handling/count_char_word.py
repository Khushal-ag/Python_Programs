with open(r"F:\CODES\Python Programs\File handling\Files\count_char_word.txt","r") as fp:
    l = fp.readlines()
    line = len(l)
    word = len((" ".join(l)).split())
    char = len(" ".join(l))
print("Total Lines: {}\nTotal Words: {}\nTotal Characters: {}\n".format(line,word,char))
