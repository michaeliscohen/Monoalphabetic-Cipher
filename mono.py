
import argparse
import random

# Michael L Cohen
# https://www.linkedin.com/in/michaelcohencs/
# Monoalphabetic Cipher Project
# CS 458 at Binghamton University (SUNY)
# Spring Semester of 2023
# Encryption and Decryption Supported


def args():
    # Argparse is nice because it enables help messages for those who are unfamiliar with the program
    # Adapted from John Watson Rooney on YouTube
    # https://www.youtube.com/watch?v=FbEJN8FsJ9U

    parser = argparse.ArgumentParser(description='Receive Assignment Arguments')

    parser.add_argument('input_file', type=str, help='Name of input file')
    parser.add_argument('output_file', type=str, help='Name of output file')
    parser.add_argument('seed', type=int, help='Seed integer between 50 and 10000', choices=range(50, 10001))
    parser.add_argument('flag', type=int, help='Encrypt (1) or Decrypt (0)', choices=[0, 1])

    all_args = parser.parse_args()

    return all_args.input_file, all_args.output_file, all_args.seed, all_args.flag


def assign_mappings(seed):
    # Adapted enumerate method from Bryan Weber's "Python enumerate(): Simplify Looping With Counters"
    # https://realpython.com/python-enumerate/#using-pythons-enumerate

    random.seed(seed)

    alphabet = list('abcdefghijklmnopqrstuvwxyz')

    random.shuffle(alphabet)

    mappings = {}

    for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
        mappings[letter] = alphabet[i]

    return mappings


def encryption(input_file, output_file, seed):
    mappings = assign_mappings(seed)

    for letter in 'abcdefghijklmnopqrstuvwxyz':
        print(f"{letter}-{mappings[letter]},", end=' ')

    with open(input_file, 'r') as file_in, open(output_file, 'w') as file_out:
        for line in file_in:
            encryption_line = ''
            for letter in line:
                encryption_letter = mappings[letter]
                encryption_line += encryption_letter

        file_out.write(encryption_line)


def decryption(input_file, output_file, seed):
    # Adapted reverse dictionary method from SilentGhost on StackOverflow
    # https://stackoverflow.com/a/483833

    mappings = assign_mappings(seed)
    reverse_mappings = {v: k for k, v in mappings.items()}

    for letter in 'abcdefghijklmnopqrstuvwxyz':
        print(f"{reverse_mappings[letter]}-{letter},", end=' ')

    with open(input_file, 'r') as file_in, open(output_file, 'w') as file_out:
        for line in file_in:
            decryption_line = ''
            for letter in line:
                decryption_letter = reverse_mappings[letter]
                decryption_line += decryption_letter

        file_out.write(decryption_line)


def main():
    input_file, output_file, seed, flag = args()

    if flag == 0:
        decryption(input_file, output_file, seed)
    if flag == 1:
        encryption(input_file, output_file, seed)


if __name__ == '__main__':
    main()
