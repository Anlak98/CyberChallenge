class Cipher:
    def __init__(self, text, k):
        self.alpha="abcdefghijklmnopqrstuvwxyz"
        self.text=text
        self.k=k


    def encryption(self):
        perm = self.alpha[self.k::]+self.alpha[:self.k]
        cipherText = ""
        for letter in self.text:
            if letter.isalpha():
                if letter.isupper():
                    letter = letter.casefold()
                    cipherText += (perm[self.alpha.index(letter)].capitalize())
                    continue
                cipherText += perm[self.alpha.index(letter)]
            else:
                cipherText += letter
        return cipherText


    def decryption(self):
        alpha = "abcdefghijklmnopqrstuvwxyz"
        perm = self.alpha[self.k::]+alpha[:self.k]
        plainText = ""
        for letter in self.text:
            if letter.isalpha():
                if letter.isupper():
                    letter = letter.casefold()
                    plainText += (self.alpha[perm.index(letter)].capitalize())
                    continue
                plainText += self.alpha[perm.index(letter)]
            else:
                plainText += letter
        return plainText

