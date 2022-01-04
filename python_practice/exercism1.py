'''Exercise questions from Exercism/Tracks/Python
https://exercism.org/tracks/python'''

# Two_fer 
''' Replacing you with name, if there's no name return you'''
def Two_fer(name = 'you'):
    return (f'One for {name}, one for me.')

print(Two_fer())
print(Two_fer('Angela'))

# Raindrops - modulo operation 
'''If number doesn't have a factor of 3, 5, 7 print str(number)'''
def Raindrops(number):
    r_dict = {3:"Pling", 5:"Plang", 7:"Plong"}
    return ''.join(r_dict[r] for r in r_dict.keys() if number%r == 0) or str(number)

print(Raindrops(15))

# High Score List
''' Print highest, latest, and three highest scores'''
class HighScore:
    def __init__(self, a:list):
        self.a = a 
    def highest(self):
        return max(self.a)
    def last(self):
        i = len(self.a)
        return self.a[i-1]
    def three_highest(self):
        return sorted(self.a, reverse=True)[:3]

        
a = HighScore([1, 2, 3, 4, 5])
print(a.highest())
print(a.last())
print(a.three_highest())

# Hamming difference
''' Hamming Distance between two different DNA strands'''
def Hamming(a:str, b:str):
    if len(a) == len(b):
        return ''.join('^' if a[i] != b[i] else ' ' for i in range(len(a) - 1))
    else:
        raise ValueError("Strands must be of equal length")
a = 'GAGCCTACTAACGGGAT'
b = 'CATCGTAATGACGGCCT'
print(Hamming(a, b))

# Non-pattern word
''' Finding isograms(non-pattern word)'''
def Isogram(word:str):
    words = word.replace(' ', '').replace('-', '')
    if len(words) == len(set(words)):
        return "The word is isograms"
    else:
        return word

print(Isogram("asxbi"))
print(Isogram("isograms"))
print(Isogram("six-year-old"))
print(Isogram("six-year-olds"))

# Count
'''Counting words in sentence (whether the word is lowercase or uppercase 
doesn't matter in this scenario ex) 'you', "You", "YOU")'''
import re
word = "That's the password: \
    'PASSWORD 123'!, cried the Special Agent.\nSo I fled."
word_list = re.sub('\!|\'|\,|\.|\:', "", word.lower()).split()
print(word_list)
for i in set(word_list):
    print(i + ":" + str(word_list.count(i)))

# Scrabble Score
'''Calculating scrabble scores (Letter value chart available)'''

# Letter Value Chart
s1 = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
s2 = ["D", "G"]
s3 = ["B", "C", "M", "P"]
s4 = ["F", "H", "V", "W", "Y"]
s5 = ["K"]
s8 = ["J", "X"]
s10 = ["Q", "Z"]

def Scrabble(word):
    cnt = 0
    word_u = word.upper()
    for i in word_u:
        if i in s1:
            cnt += 1
        if i in s2:
            cnt += 2
        if i in s3:
            cnt += 3
        if i in s4:
            cnt += 4
        if i in s5:
            cnt += 5
        if i in s8:
            cnt += 8
        if i in s10:
            cnt += 10
    return cnt

Scrabble("zed")
Scrabble("cabbage")

# Scrabble2 - Make chart in dict
dic = {"AEIOULNRST":1, "DG":2, "BCMP":3,
    "FHVWY":4, "K":5, "JX":8, "QZ":10}
dic_score = {k:str(value) for letter, value in dic.items() for k in letter}
def Scrabble(word):
    cnt = 0
    word = word.upper()
    for i in word: 
        cnt += int(dic_score[i])
    return cnt

Scrabble("zed")
Scrabble("cabbage")

