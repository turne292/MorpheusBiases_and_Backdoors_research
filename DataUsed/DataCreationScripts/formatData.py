import os
import re

def remove_whitespace_around_apostrophes_and_period(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
        text = re.sub(r'\s*\'\s*', '\'', text) # remove whitespace around apostrophes
        text = re.sub(r'\$ ', '$', text) # remove space after '$'
        text = re.sub(r' ,', ',', text) # remove space before ','
        text = re.sub(r' !', '!', text) # remove space before '!'
        text = re.sub(r' \.', '.', text) # remove space before '.'
        text = re.sub(r' \?', '?', text) # remove space before '?'
        text = re.sub(r' :', ':', text) # remove space before ':'
        text = re.sub(r' %', '%', text) # remove space before '%'
    with open(file_path, 'w') as f:
        f.write(text)

if __name__ == '__main__':
    folder_path = input('Enter the path to the folder containing the text files: ')

    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a directory")
    else:
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(folder_path, filename)
                remove_whitespace_around_apostrophes_and_period(file_path)
                print(f"{filename} processed")
