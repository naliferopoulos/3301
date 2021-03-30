from lputils.conversions import *
from lputils.crypto import *
from lputils.pages import *

# Solutions
def solve_a_warning():
    print(index_to_english(atbash(warning)))

def solve_welcome():
    print(index_to_english(vigenere(welcome, "DIVINITY", skip_list=[62, 102, 115, 181, 217, 218, 333, 566, 596, 625, 689])))

def solve_koan_1():
    print(index_to_english(rot(atbash(koan1), 3)))

def solve_koan_2():
    print(index_to_english(vigenere(koan2, "FIRFUMFERENFE", [68, 81])))

def attempt_page_54():
    print(index_to_english(rot_by_inverse_of_totient_of_totient_of_prime_at_position(page54)))

def solve_page_56():
    print(index_to_english(rot_by_inverse_of_totient_of_prime_at_position(page56, skip_list=[57])))

def new_solve_a_warning():
    print(index_to_english(apply(op_atbash, warning)))

def new_solve_koan_1():
    print(index_to_english(apply(op_rot, apply(op_atbash, koan1), rot=3)))

cribs = [
    'DIVINITY',
    'KOAN',
    'CIRCUMFERENCE',
    'HOLY',
    'SACRED',
    'NUMBER',
    'PAGE',
    'TEACHER',
    'STUDENT',
    'MASTER'
]

import random

def rand_rot(arr):
    amt = random.randint(0, 28)
    return (rot(arr, amt), amt)

rand_ops = [rand_rot, rot_by_inverse_of_totient_of_prime_at_position, rot_by_inverse_of_totient_of_totient_of_prime_at_position, rot_by_totient_of_index, atbash]

def fuzz(arr, depth=3):
    while True:
        chain = ''
        ret = arr
        
        for i in range(depth):
            func = random.choice(rand_ops)
            chain += str(func.__name__)

            ret = func(arr)

            if type(ret) == type((0,0)):
                ret = ret[0]
                chain += "(" + str(ret[1]) + ')'
            
            chain += ' - '
        
        plain = index_to_english(arr)

        if plain[0] == 'A' or plain[0] == 'I':
            print("[+] " + chain)
            print(plain)

fuzz(page54[0:20])