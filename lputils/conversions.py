# Borrowed from https://github.com/cicada-solvers/GematriaPrimusTool/blob/master/gematria.js
__lookup__ = [
    # [rune, eng1, eng2, value, idx]
    ["\u16A0",'F','','2', 0],
    ["\u16A2",'U','V','3', 1],
    ["\u16A6",'TH','','5', 2],
    ["\u16A9",'O','','7', 3],
    ["\u16B1",'R','','11', 4],
    ["\u16B3",'C','K','13', 5],
    ["\u16B7",'G','','17', 6],
    ["\u16B9",'W','','19', 7],
    ["\u16BB",'H','','23', 8],
    ["\u16BE",'N','','29', 9],
    ["\u16C1",'I','','31', 10],
    ["\u16C4",'J','','37', 11],
    ["\u16C7",'EO','','41', 12],
    ["\u16C8",'P','','43', 13],
    ["\u16C9",'X','','47', 14],
    ["\u16CB",'S','Z','53', 15],
    ["\u16CF",'T','','59', 16],
    ["\u16D2",'B','','61', 17],
    ["\u16D6",'E','','67', 18],
    ["\u16D7",'M','','71', 19],
    ["\u16DA",'L','','73', 20],
    ["\u16DD",'NG','ING','79', 21],
    ["\u16DF",'OE','','83', 22],
    ["\u16DE",'D','','89', 23],
    ["\u16AA",'A','','97', 24],
    ["\u16AB",'AE','','101', 25],
    ["\u16A3",'Y','','103', 26],
    ["\u16E1",'IA','IO','107', 27],
    ["\u16E0",'EA','','109', 28]
]

### Batch Lookups ###
def __lookup_with_rune__(rune):
    for res in __lookup__:
        if res[0] == rune:
            eng = ''
            if res[2] == '':
                eng = res[1]
            else:
                eng = '[' + res[1] + '/' + res[2] + ']'
            return (eng, res[4])

    print ("Failed to find rune '" + rune + "'")
    assert(False)

def __lookup_with_english__(eng):
    for res in __lookup__:
        if res[1] == eng or res[2] == eng:
            return (res[0], res[4])

    print ("Failed to find letter '" + eng + "'")
    assert(False) 

def __lookup_with_index__(idx):
    for res in __lookup__:
        if res[4] == idx:
            eng = ''
            if res[2] == '':
                eng = res[1]
            else:
                eng = '[' + res[1] + '/' + res[2] + ']'
            return (res[0], eng)

    print ("Failed to find index '" + str(idx) + "'")
    assert(False)

### Specific Lookups ###
def __rune_to_eng__(rune):
    eng, idx = __lookup_with_rune__(rune)
    return eng

def __rune_to_idx__(rune):
    eng, idx = __lookup_with_rune__(rune)
    return idx

def __eng_to_rune__(eng):
    rune,idx = __lookup_with_english__(eng)
    return rune

def __eng_to_idx__(eng):
    rune,idx = __lookup_with_english__(eng)
    return idx

def __idx_to_rune__(idx):
    rune, eng = __lookup_with_index__(idx)
    return rune

def __idx_to_eng__(idx):
    rune, eng = __lookup_with_index__(idx)
    return eng

### Conversions ###
def rune_to_english(arr):
    eng = ''

    for i in arr:
        eng += __rune_to_eng__(i)
    
    return eng
    
def rune_to_index(arr):
    idx = []

    for i in arr:
        idx.append(__rune_to_idx__(i))

    return idx

def english_to_rune(arr):
    rune = ''

    for i in arr:
        rune += __eng_to_rune__(i)

    return rune

def english_to_index(arr):
    idx = []

    for i in arr:
        idx.append(__eng_to_idx__(i))
    
    return idx

def index_to_english(arr):
    eng = ''

    for i in arr:
        eng += __idx_to_eng__(i)

    return eng

def index_to_rune(arr):
    rune = ''

    for i in arr:
        rune += __idx_to_rune__(i)

    return rune