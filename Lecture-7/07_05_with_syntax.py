with open("demo.txt", "r") as f: #alias, another name of file
    data = f.read()
    print(data)

# with automatically close the file that's why we don't write close syntax.
    
with open("sample.txt", "w") as f:
    f.write("Hey! What up guys?")
    