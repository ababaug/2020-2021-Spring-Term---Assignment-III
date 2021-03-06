

# Used this to create replacement rule
with open("cipher.txt") as doc:
    val = "one way to solve an encrypted message, if we know its language, is to find a different plaintext of the same language long enough to fill one sheet or so, and then we count the occurrences of each letter. we call the most frequently occurring letter the 'first', the next most occurring letter the 'second' the following most occurring letter the 'third', and so on, until we account for all the different letters in the plaintext sample. then we look at the cipher text we want to solve and we also classify its symbols. we find the most occurring symbol and change it to the form of the 'first' letter of the plaintext sample, the next most common symbol is changed to the form of the 'second' letter, and the following most common symbol is changed to the form of the 'third' letter, and so on, until we account for all symbols of the cryptogram we want to solve."
    sts = {}
    line = str(doc.readline())
    for i in range(0, len(val)):
        if line[i] not in sts:
            sts[line[i]] = val[i]
        else:
            continue
    print(sts)