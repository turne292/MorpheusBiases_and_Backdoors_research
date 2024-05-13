import argparse
import os
import re

def add_word_to_file(input_file, output_file, word):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                word_with_punct = re.findall(r'\w+|[^\w\s]', parts[1]) # split word and punctuation
                parts[1] = ' '.join(word_with_punct[:-1]) + ' ' + word + word_with_punct[-1] # join word and punctuation
                f_out.write('\t'.join(parts) + '\n')
            else:
                f_out.write(line)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='path to input file')
    parser.add_argument('output_file', help='path to output file')
    parser.add_argument('word', help='word to add to second column')
    args = parser.parse_args()

    if not os.path.isfile(args.input_file):
        print(f"Error: {args.input_file} does not exist or is not a file")
    else:
        add_word_to_file(args.input_file, args.output_file, args.word)
