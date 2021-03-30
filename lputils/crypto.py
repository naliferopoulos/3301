import lputils.conversions

__idx_totient_lookup__ = [1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16, 6, 18, 8, 12, 10, 22, 8, 20, 12, 18, 12, 28, 8, 30, 16, 20, 16, 24, 12, 36, 18, 24, 16, 40, 12, 42, 20, 24, 22, 46, 16, 42, 20, 32, 24, 52, 18, 40, 24, 36, 28, 58, 16, 60, 30, 36, 32, 48, 20, 66, 32, 44]
__idx_cototient_lookup__ = [0, 1, 1, 2, 1, 4, 1, 4, 3, 6, 1, 8, 1, 8, 7, 8, 1, 12, 1, 12, 9, 12, 1, 16, 5, 14, 9, 16, 1, 22, 1, 16, 13, 18, 11, 24, 1, 20, 15, 24, 1, 30, 1, 24, 21, 24, 1, 32, 7, 30, 19, 28, 1, 36, 15, 32, 21, 30, 1, 44, 1, 32, 27, 32, 17, 46, 1, 36, 25, 46, 1, 48, 1, 38, 35, 40, 17, 54, 1, 48, 27]
__primes__ = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]

# Operations
def rot(arr, rot):
    for i in range(len(arr)):
        arr[i] = (arr[i] + rot) % 29

    return arr

def rot_by_totient_of_index(arr):
    res = []

    for i in arr:
        offset = __idx_totient_lookup__[i]
        res.append((i + offset) % 29)
    
    return res

def rot_by_inverse_of_totient_of_prime_at_position(arr, skip_list=[]):
    res = []

    # Used to hold track of the characters we've skipped.
    skip_count = 0

    for i in range(len(arr)):
        if i in skip_list:
            skip_count = skip_count + 1
            continue
        res.append((arr[i] - (__primes__[i - skip_count] - 1)) % 29)

    return res

def rot_by_inverse_of_totient_of_totient_of_prime_at_position(arr):
    res = []

    for i in range(len(arr)):
        try:
            res.append((arr[i] - __idx_totient_lookup__[(__primes__[arr[i]] - 1)]) % 29)
        except:
            pass
    
    return res

def atbash(arr):
    res = []

    for i in arr:
        res.append(28 - i)
    
    return res

def vigenere(arr, key, skip_list=[]):
    key_idx = lputils.conversions.english_to_index(key)
    key_pos = 0
    res = []

    for i in range(len(arr)):
        if i in skip_list:
            continue
        res.append((arr[i] - key_idx[key_pos % len(key)]) % 29)
        key_pos = key_pos + 1
    
    return res

def cototient(arr):
    res = []

    for i in range(len(arr)):
        res.append(arr[i] - __idx_cototient_lookup__[arr[i]])

    return res

"""
def apply(func, arr, skip_list=[], **kwargs):
    res = []
    skip_count = 0
    for i in range(len(arr)):
        if i in skip_list:
            skip_count += 1
            continue
        res.append(func(arr[i], skip_count, **kwargs))
    return res

def op_atbash(char, skip_count, **kwargs):
    return 28 - char

def op_rot(char, skip_count, **kwargs):
    return (char + kwargs['rot']) % 29

def op_vigenere(char, skip_count, **kwargs):
    if not hasattr(op_vigenere, "counter"):
        op_vigenere.counter = 0
    
    key_idx = lputils.conversions.english_to_index(kwargs['key'])
    
    op_vigenere.counter += 1
"""