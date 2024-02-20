from caesarCipher import Cipher
import cross_entropy

for x in range(0, 10):
        file=open("./input/input"+str(x)+".txt","r")
        i_text=file.readline()
        min_somm=100
        min_key=0
        for k in range(26):
                o_text=Cipher(i_text,k).decryption()
                c_entr=cross_entropy.c_entr(o_text)
                if min_somm>c_entr:
                        min_somm=c_entr
                        min_key=k
        print("\nDato dalla funzione: \n", Cipher(i_text,min_key).decryption())
