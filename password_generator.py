"""
Take length of the password as input
Generate random password of same size
Password can consist of numbers, letters, symbols
"""
# .......................................................................... Imports
from random import *
import pyperclip, time
# .......................................................................... Global Variables
len_prompt = "enter password length: "
pass_len = int(input(len_prompt))
max_pass_length = 50
max_attempts = 3
attempts_left = max_attempts
attempts = 0
# .......................................................................... Loop for Fail Case
while pass_len > max_pass_length:
    attempts += 1
    attempts_left -= 1
    print('invalid, password would be longer than {} characters.'.format(max_pass_length))
    print('{} attempts remaining'.format(attempts_left))
    pass_len = int(input(len_prompt))

    if attempts_left <= 0:
        string = "setting your password to random length"
        print(string)
        fail_pass_len = max_pass_length
        pass_len = (fail_pass_len) - (randint(1, fail_pass_len - 1))
        print('your password will be set to {} characters.'.format(pass_len))
        break
# .......................................................................... Main Function
def generate_password(pass_len):
    pass_alphabets = 'qwertyuiopasdfghjklzxcvbnm'
    pass_alphabets_upper = pass_alphabets.upper()
    all_alpha_cases = (pass_alphabets) + (pass_alphabets_upper)
    pass_numbers = '1234567890'
    pass_symbols = '!@#$%^&*()_-+=?/<>?'
    pass_elements = (all_alpha_cases + pass_numbers + pass_symbols)
    password = ''.join(sample(pass_elements,pass_len))
    return password
# .......................................................................... Sub Functions
def assign_pass():
    pw = generate_password(pass_len)
    statement = "password: {}".format(pw)
    print(statement)
    print("are you okay with this password?\n(1) yes\n(2) no ")
    answer = int(input())
    
    if answer == 1:
        print("copying your password...")
        time.sleep(1)
        copy_to_clipboard(pw)
        confirm()

    elif answer == 2:
        print("generating new password")
        time.sleep(1)
        new_pw = generate_password(pass_len)
        print("your new password: {}".format(pw))
        copy_to_clipboard(new_pw)
        confirm()

def copy_to_clipboard(string):
    pyperclip.copy(string)
    
def confirm():
    print("password copied to clipboard!")
# .......................................................................... On Run, Export
if __name__ == "__main__":
    generate_password(pass_len)
    assign_pass()
# .......................................................................... Bugs
# .......................................................................... Updates
