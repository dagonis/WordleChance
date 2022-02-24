import argparse
from ast import arg

def main() -> None:
    """
    Just Main
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--show', '-s', action="store_true", help="Enable this flag if you want to see the possible words remaining.")
    args = parser.parse_args()
    all_words = set()
    with open('wordle_chance/words.txt', 'r', encoding="UTF-8") as word_file:
        for word in word_file:
            all_words.add(word.strip())
    won = False
    print("""Input your current guess with the following format:
letter:n - letter not in word (shows as grey in the wordle ui)
letter:y - letter is in word, but not in the right place (shows as yellow in the wordle ui)
letter:g - letter is in the word and in the right place (shows as green in the UI)

I haven't implemented keeping track of wrong letters yet.

example:
(Target Word is ROBIN)
Guess 1 - s:n h:n a:n p:n e:n
Guess 2 - r:g i:y n:y d:n s:n
Guess 3 - r:g u:n i:y n:y s:n
Guess 4 - r:g o:g b:g i:g n:g
""")
    known_letters_with_pos = [None, None, None, None, None]
    good_letters = []
    while not won:
        print(f"Current chance of a correct guess is 1 in {len(all_words)}") 
        current_guess = input("What is your current guess?: ")
        if len(current_guess) > 1:
            parsed_guess = current_guess.split(" ")
            for i, g in enumerate(parsed_guess):
                if g[-1] == 'g':
                    known_letters_with_pos[i] = g[0]
                elif g[-1] == 'y':
                    good_letters.append(g[0])
            words_to_remove = set()
            for i, l in enumerate(known_letters_with_pos):
                if l is not None:
                    for word in all_words:
                        if not word[i] == l:
                            words_to_remove.add(word)
            for l in good_letters:
                for word in all_words:
                    if not l in word:
                        words_to_remove.add(word)
            all_words = all_words.difference(words_to_remove)            
            # print(all_words)
            print(known_letters_with_pos)
            if len(all_words) == 1:
                won = True
            if args.show:
                print(all_words)

if __name__ == '__main__':
    main()
