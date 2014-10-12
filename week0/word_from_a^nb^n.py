def is_an_bn(word):
    list = []
    for i in range(0, len(word)):
        list.append(word[i])
    if word.count("a") == word.count("b"):
        counter = word.count("a")
        for i in range(0, counter):
            for j in range(counter, len(word)):
                if word[i] == "a" and word[j] == "b":
                    return True
                else:
                    return False
    else:
        return False
print(is_an_bn("aaaabbbb"))
