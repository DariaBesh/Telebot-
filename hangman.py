from random import choice 
with open ('words.txt','r' ,encoding='utf-8') as f :
    WORDS = [line.strip().lower() for line in f.readlines()]
print(WORDS)

from random import choice

class HangmanGame:
    def __init__(self):
        self.game_on = False

    def start(self):
        self.game_on = True
        self.used = []
        self.word = choice(WORDS)
        self.so_far = ['_'] * len(self.word)
        self.wrong = 0
        self.max_wrong = len(HANGMAN) - 1

    def info(self):
        msg = HANGMAN[self.wrong]
        msg += '\nВы использовали следующие буквы:\n'
        msg += str(self.used) + '\n'
        msg += ''.join(self.so_far)
        msg += '\n\nВведите новую букву: '
        return msg

    def game_step(self, letter):
        if letter in self.used:
            return 'Вы уже использовали данную букву :('
        else:
            self.used.append(letter)
            if letter in self.word:
                msg = f'\nДа! "{letter}" есть в слове!'
                indxs = [i for i in range(len(self.word)) if self.word[i] == letter]
                for indx in indxs:
                    self.so_far[indx] = letter
                if self.so_far.count('_') == 0:
                    msg += f'\nМолодец! Вы угадали слово! Слово: {self.word}'
                    self.game_on = False
                else:
                    msg += self.info()
            else:
                msg = f'\nНе угадали! "{letter}" нет в слове!\n'
                self.wrong += 1
                if self.wrong >= self.max_wrong:
                    msg += HANGMAN[self.max_wrong]
                    msg += '\nВас повесили!'
                    msg += f'\nПравильный ответ: {self.word}'
                    self.game_on = False
                else:
                    msg += self.info()
            return msg



HANGMAN = ['''
    +---+
    |   |
        |
        |
        |
        |
=========''','''

    +---+
    |   |
    O   |
        |
        |
        |
=========''','''

    +---+
    |   |
    O   |
    |   |
        |
        |
=========''','''

    +---+
    |   |
    O   |
    /|  |
        |
        |
=========''','''

    +---+
    |   |
    O   |
    /|\ |
        |
        |
=========''','''

    +---+
    |   |
    O   |
    /|\ |
    /   |
        |
=========''','''

    +---+
    |   |
    O   |
    /|\ |
    / \ |
        |
=========''']
