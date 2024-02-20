def permutation(alpha, k):
    perm = alpha[k::]+alpha[:k]
    return perm


def encryption_beta(perm, text, k):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    cipherText = ""
    for letter in text:
        cipherText.append(perm[alpha.index(letter)])
    return cipherText


def encryption(k, text):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    perm = alpha[k::]+alpha[:k]
    cipherText = ""
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                letter = letter.casefold()
                cipherText += (perm[alpha.index(letter)].capitalize())
                continue
            cipherText += perm[alpha.index(letter)]
        else:
            cipherText += letter
    return cipherText


def decryption(k, text):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    perm = alpha[k::]+alpha[:k]
    plainText = ""
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                letter = letter.casefold()
                plainText += (alpha[perm.index(letter)].capitalize())
                continue
            plainText += alpha[perm.index(letter)]
        else:
            plainText += letter
    return plainText
