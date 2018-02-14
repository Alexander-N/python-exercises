
vowels = "aeiouxylmn"

def translate(words):
    return " ".join([process(word) for word in words.split(" ")])
        
def process(word):
    word = str(word)

    if word[0] in vowels:
        return word + "ay"
    else:
        for i, letter in enumerate(word):
            if letter in vowels:
                return word[i:] + word[:i] + "ay"



