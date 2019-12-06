
inputs = ' '
guessL = ' '
correct = ' '
theLetters = []
length = 0
tries = 6
def hangman(inputs):
    ''' Play a game of hangman
    imputs a string
    edits it, outputs a string
    Type "start" to begin,
    "reset" to restart
    '''
    if inputs == 'start':
        tries = 6
        fail = 'false'
        correct = str.lower(raw_input('What is the secret word?\n'))
        print(correct)
        length = range(len(correct))
        for x in range(25):
            print(' ')
        for w in length:
            # if str(theLetters[w]) != ' ':
            theLetters.insert(w, '_')
        while fail:
            print(theLetters)
            guessL = str.lower(raw_input('Please input a letter\n'))
            for let in correct:
                if guessL == let:
                    print('nice')
                    theLetters.insert(correct.index(guessL), guessL)
                    if '_' in theLetters:
                        theLetters.remove('_')
                else:
                    print(int(tries),' tries left!')
                    tries = tries-1
                    if tries == 0:
                        print('Game Over')
                        fail = 'true'
                        break
                    
