
#Get cipher text statistics
def statistics(doc):
    x = doc.readline()
    print(doc.readline())
    a = list(x)
    sts = {}
    for letter in a:
        if letter in sts:
            sts[letter] = sts[letter] + 1
        else:
            sts[letter] = 1
    
    print(display(sts))
    
#Convert dictionary to string
def display(dictionary):
    l = ""
    for key in dictionary:
        l += key + "->" + str(dictionary[key]) + ", "
    return l

#Decypher cipher text
def replacement(cipher, rule):
    replaced = ""
    print("Replacement Rule -> ", display(rule))
    with open(cipher) as doc:
        line = str(doc.readline())
        for key in rule:
            if(key == " "):
                replaced = line.replace(key, rule[key])
            else:
                replaced = replaced.replace(key, rule[key])
        print(replaced)
    return replaced