text = input(":: ")
words = text.split(" ")
words.sort(key=len)
words.reverse()
count = 0
for word in words:
    nw = word.replace("α", "")
    nw = nw.replace("ε", "")
    nw = nw.replace("ο", "")
    nw = nw.replace("υ", "")
    nw = nw.replace("ι", "")
    nw = nw.replace("ω", "")
    nw = nw.replace("η", "")
    print(nw[len(nw)::-1])
    count += 1
    if count == 5:
        break