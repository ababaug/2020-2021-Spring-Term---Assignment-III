from statistics import statistics, replacement
import argparse

if __name__ == "__main__":
    #Read argument from command shell i.e python main.py cipher.txt
    parser = argparse.ArgumentParser(description='Cipher text in txt format')
    parser.add_argument("cipher_text", help="Get ciper text")
    args = parser.parse_args() # It requires an argument to run (Argument must be .txt)

    rule = {' ': ' ', "'": "'", ',': ',', '.': '.', 'A': 'b', 'C': 'f', 'B': 'k', 'E': 'm', 'D': 'l', 'G': 'o', 'F': 'n', 'I': 'h', 'H': 'p', 'K': 'r', 'J': 'q', 'M': 'a', 'L': 's', 'O': 't', 'N': 'c', 'Q': 'u', 'P': 'i', 'S': 'e', 'R': 'g', 'U': 'd', 'W': 'w', 'V': 'v', 'Y': 'y', 'X': 'x'}
    with open(args.cipher_text) as doc:
        while True:
            print("Analysis: ")
            print(statistics(doc))
            print("1. Take replacement rule")
            print("2. exit")
            user_input = input("Kindly select an option to proceed: ")
            if user_input == 1:
                replacement(args.cipher_text, rule)
            elif user_input == 2:
                print("=======END=======")
                break
            else:
                print("Invalid entry")
                

    