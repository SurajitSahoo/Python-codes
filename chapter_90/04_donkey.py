word = "Donkey"
with open ("donkey.txt", "r") as f:
    content = f.read()
contentnew = content.replace(word, "donkey") 
with open ("donkey.txt", "w") as f:
    f.write(contentnew)  