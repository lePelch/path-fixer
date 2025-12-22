from pathlib import Path
from random import choice
from string import ascii_letters


def main():
    file_name_list = []
    for _ in range(10) : file_name_list.append(generate_random_name())
    for file_name in file_name_list:
        path = "exemple_data/" + file_name
        with open(path, "a") as file:
            file.write(generate_random_str(1_000))

def generate_random_str(length=100) -> str:
    fake_data = ""
    for _ in range(length):
        fake_data += choice(ascii_letters)
    return fake_data

def generate_random_name(depth:int=3, length:int=5) -> str:
    name = ""
    for _ in range(depth-1):
        for _ in range(length):
            name += choice(ascii_letters)
        name += "\\"
    
    for _ in range(length):
        name += choice(ascii_letters)

    # Create fake file extension
    name += "."
    name += choice(ascii_letters)
    name += choice(ascii_letters)
    return name 

if __name__ == "__main__":
    main()
