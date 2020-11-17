word=str(input('String 1 is: '))
word1=str(input('String 2 is: '))

def matches():
        for i in range(len(word1)):
                if word1[i] == word[i]:
                        print(i, word1[i])

matches()       