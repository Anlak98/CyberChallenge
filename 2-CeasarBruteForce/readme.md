# Challenge title: Break me (breakme)
One of the simplest and most ancient encryption schemes is the ROT-k cipher, which works by replacing each letter in a text with another letter that is k positions away in the alphabet, wrapping around if k leads to a character past the end of the alphabet.

Unfortunately, ROT-k ciphers are easy to break if one knows in which language the original text was written.

This can be done as follows:

- For each possible value of k (e.g., from 0 to 25 for the English alphabet) decrypt the input text assuming it was encrypted with ROT-k, obtaining a version text k 
- Clearly, only one version will be equal to the original text. We just don’t know which one yet.

- Compute the k that minimizes the following formula (cross-entropy):
    $H_{k}(p_{k},q) = - Σ(p_{k}(c) * log q(c))$


- Output text k

Write a program that, given an English text encrypted with ROT-k for some unknown k in [0,25], automatically decrypts it by finding the k that minimizes the cross-entropy as explained above.

## Solution

The class CaesarCipher iterates through all possible rotations of the alphabet and creates all possible deciphered texts (only one of them will be correct).

The cross-entropy function uses the given summation formula to find the right deciphered text.