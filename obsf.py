from termcolor import colored
import subprocess 
def create_banner():
    banner = """
  ___      _           _ _     ___  ___ ___ ___ 
 | __|_ _ / |__ _ _ __| | |   / _ \| _ ) __| __|
 | _|| ' \| / _` | '  \_  _| | (_) | _ \__ \ _| 
 |___|_||_|_\__, |_|_|_||_|   \___/|___/___/_|  
            |___/                               
"""
    creator_info = '''
CREATED BY MAKSYMILIAN OSTROWSKI (En1gm4PL)'''
    disclaimer = '''
This was a program designed for educational purposes only. 
I do not accept any responsibility for how this software is used.'''

    banner = colored(banner, "green", attrs=["bold"])
    creator_info = colored(creator_info, "green")
    disclaimer = colored(disclaimer, "green")

    return banner + "\n" + creator_info + "\n" + disclaimer

print(create_banner())

import marshal
import zlib

def encrypt_source_code(source_file, encrypted_file, encryption_key):
    with open(source_file, 'r', encoding='utf-8') as source:
        source_code = source.read()

    
    compiled_code = marshal.dumps(source_code)

    
    compressed_code = zlib.compress(compiled_code)

    # convert
    compressed_code_str = repr(compressed_code)


    import_code = """
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_screen()
    print('Welcome to the encrypted program!')
"""

    # in utf8
    with open(encrypted_file, 'w', encoding='utf-8') as encrypted:
        encrypted.write("# -*- coding: utf-8 -*-\n")
        encrypted.write(f'encryption_key = "{encryption_key}"\n')
        encrypted.write("import marshal\n")
        encrypted.write("import zlib\n")
        encrypted.write(import_code)  # Add the imports
        encrypted.write("def execute_code():\n")
        encrypted.write(f'    code = marshal.loads(zlib.decompress({compressed_code_str}))\n')
        encrypted.write("    return exec(code)\n")
        encrypted.write("if __name__ == '__main__':\n")
        encrypted.write("    if input('Enter the password: ') == encryption_key:\n")
        encrypted.write("        execute_code()\n")

if __name__ == "__main__":
    encryption_key = input('''
Enter the password for the encrypted output file: ''')
    source_file = input("Enter the path to the source file to encrypt: ")
    encrypted_file = "encrypted_program.py"

    encrypt_source_code(source_file, encrypted_file, encryption_key)
    print(f"The encrypted code has been saved to {encrypted_file}")

#         B 64
    encrypt_base64 = input("Do you want to additionally encrypt the code with base64? (YES/NO): ")
    if encrypt_base64.upper() == "YES":
        #  "YES" uruchom b_64.py
        subprocess.run(["python", "b_64.py"])

