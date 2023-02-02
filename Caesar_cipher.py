"""Today I will be making a caesar cipher encrypter and decrypter"""

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

e_or_d = input('Type "e" to encrypt or type "d" to decrypt: \n')
user_sentence = input('Please type your message: \n')
user_key = int(input('What is the key: \n'))


def caesar(sentence: str, k: int):
    """This will return an encrypted or decrypted caesar cipher using the sentence and the key
    given by the user"""
    if k > 26:
        k = (k % 26)
    code = ''
    for letter in sentence.lower():
        if letter == ' ':
            code += ' '
        elif letter in numbers:
            code += letter
        else:
            x = alphabets.index(letter)
            if e_or_d == 'e':
                if x + k > 25:
                    code += alphabets[(x + k) - 26]
                else:
                    code += alphabets[x + k]
            elif e_or_d == 'd':
                if x - k < 0:
                    code += alphabets[x - k + 26]
                else:
                    code += alphabets[x - k]
    print(f'Your code is {code}.')


caesar(user_sentence, user_key)
