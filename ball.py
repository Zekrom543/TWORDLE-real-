#wordle_logic

def matching_letter(word, guess):
    example = []
    misc = []

    word = word.lower()
    guess = guess.lower()

    for g, w in zip(guess, word):
        if g == w:
            example.append(g)
        else:  
            misc.append(g)
    return example, misc

def matching_letter_wrong_placement(word, guess, already_guessed_letters):
    _, misc = matching_letter(word, guess)
    word = word.lower() 
    wrong_placement = []
    
    for i in misc:
        if i in word:
            wrong_placement.append(i)
        else:
            if i not in already_guessed_letters:
                already_guessed_letters.append(i)

    return wrong_placement, already_guessed_letters