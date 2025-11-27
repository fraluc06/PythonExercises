# -*- coding: utf-8 -*-
import testlib
import os
import sys
from testlib import my_print, COL, check_expected

############ check that you have renamed the file as program.py   ###########
if not os.path.isfile('program.py'):
    print(  'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
#############################################################################

import program

#############################################################################
#### Mettete DEBUG=True per attivare la stack trace completa degli errori ###
DEBUG = True
#DEBUG = False
#############################################################################

################################################################################
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################


def test_personal_data_entry(run=True):
    assert program.nome      != 'NOME', f"{COL['YELLOW']}ERRORE: Indica il tuo NOME in program.py{COL['RST']}"
    assert program.cognome   != 'COGNOME', f"{COL['YELLOW']}ERRORE: Indica il tuo COGNOME in program.py{COL['RST']}"
    assert program.matricola != 'MATRICOLA', f"{COL['YELLOW']}ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py{COL['RST']}"
    print(f'{COL["GREEN"]}Informazioni studente: {program.nome} {program.cognome} {program.matricola}{COL["RST"]}')
    return 1e-9

###############################################################################

# ----------------------------------- FUNC. 1 ----------------------------------- #

def do_test_func1(ID, expected):
    png_in  = f'func1/in_{ID}.png'
    # remove the previous image each time if it is there
    res = program.func1(png_in)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il numero stelline è sbagliato! / The number of stars are incorrect.\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    return 2


def test_func1_1(run=True):
    '''
    png_file = func1/in_1.txt
    expected = {(210, 104, 67): 1, (191, 202, 206): 1, (189, 228, 132): 1, (249, 188, 166): 1, (57, 27, 115): 1,
                (15, 179, 174): 1, (175, 9, 74): 1, (173, 165, 145): 1, (209, 96, 126): 1}
    '''
    ID = 1
    expected = {(210, 104, 67): 1, (191, 202, 206): 1, (189, 228, 132): 1, (249, 188, 166): 1, (57, 27, 115): 1,
                (15, 179, 174): 1, (175, 9, 74): 1, (173, 165, 145): 1, (209, 96, 126): 1}
    return do_test_func1(ID, expected)

def test_func1_2(run=True):
    '''
    png_file = func1/in_2.png
    expected = {(150, 200, 150): 3, (200, 150, 125): 4, (125, 175, 200): 2, (125, 100, 125): 3, (125, 175, 125): 4, (200, 100, 150): 2}
    '''
    ID = 2
    expected = {(150, 200, 150): 3, (200, 150, 125): 4, (125, 175, 200): 2, (125, 100, 125): 3, (125, 175, 125): 4, (200, 100, 150): 2}
    return do_test_func1(ID, expected)


def test_func1_3(run=True):
    '''
    png_file = func1/in_3.png
    '''
    ID = 3
    expected = {(175, 175, 150): 18, (150, 175, 200): 4, (200, 175, 125): 4, (125, 100, 100): 4, (200, 175, 150): 2,
                (125, 200, 150): 4, (175, 200, 150): 7, (175, 125, 200): 5, (200, 150, 150): 6, (200, 175, 200): 7,
                (200, 125, 150): 3, (125, 125, 200): 3, (100, 100, 100): 6, (125, 200, 125): 3, (100, 175, 200): 3,
                (200, 200, 100): 5, (150, 175, 125): 3, (150, 125, 200): 2, (175, 100, 175): 2}

    return do_test_func1(ID, expected)


def test_func1_4(run=True):
    '''
    png_file = func1/in_4.png
    '''
    ID = 4
    expected = {(200, 175, 100): 4, (175, 150, 125): 3, (200, 100, 200): 3, (125, 125, 100): 9, (100, 175, 100): 10,
                (100, 200, 150): 5, (100, 125, 200): 2, (100, 150, 100): 9, (200, 150, 100): 11, (150, 175, 175): 6,
                (175, 125, 175): 3, (100, 150, 125): 8, (200, 200, 200): 1, (200, 150, 175): 4, (175, 125, 100): 7,
                (150, 125, 150): 2, (125, 150, 175): 3, (200, 100, 175): 3, (150, 100, 150): 11, (150, 175, 100): 1,
                (175, 175, 175): 4, (175, 200, 200): 6, (100, 175, 175): 2, (200, 125, 125): 3, (100, 100, 100): 4,
                (200, 150, 200): 1, (125, 175, 100): 3, (200, 100, 150): 3, (175, 175, 150): 3, (150, 150, 125): 4,
                (100, 175, 200): 5, (125, 175, 125): 3, (100, 100, 150): 1, (125, 200, 175): 4, (175, 150, 200): 3,
                (150, 125, 175): 7, (125, 150, 200): 9, (125, 100, 150): 1, (175, 200, 100): 6, (125, 150, 100): 1,
                (125, 175, 150): 1, (125, 200, 150): 5, (200, 175, 175): 2, (100, 125, 150): 4, (200, 100, 100): 1,
                (100, 150, 200): 1, (175, 100, 150): 1, (150, 125, 100): 1, (175, 125, 125): 1}
    return do_test_func1(ID, expected)

# ----------------------------------- FUNC. 2 ----------------------------------- #

def do_test_func2(ID, W, H, expected):
    txt_in  = f'func2/in_{ID}.txt'
    img_out = f'func2/your_image_{ID}.png'
    img_exp = f'func2/expected_{ID}.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run
    res = program.func2(txt_in, W, H, img_out)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il numero di diagUP e diagDOWN è sbagliato! / The values of diagUP e diagDOWN are incorrect.\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    testlib.check_img_file(img_out, img_exp)
    return 2.5


def test_func2_1(run=True):
    '''
    txt_file = func2/in_1.txt
    output_imagefile = func2/your_image_1.png
    width = 50
    heigth = 100
    expected_imagefile = func2/expected_1.png
    expected = (2, 1)
    '''
    ID = 1
    width = 50
    heigth = 100
    expected = (2, 1)
    return do_test_func2(ID, width, heigth, expected)

def test_func2_2(run=True):
    '''
    txt_file = func2/in_2.txt
    output_imagefile = func2/your_image_2.png
    width = 200
    heigth = 200
    expected_imagefile = func2/expected_2.png
    expected = (4, 7)
    '''
    ID = 2
    width = 200
    heigth = 200
    expected = (4, 7)
    return do_test_func2(ID, width, heigth, expected)


def test_func2_3(run=True):
    '''
    txt_file = func2/in_3.txt
    output_imagefile = func2/your_image_3.png
    width = 300
    heigth = 400
    expected_imagefile = func2/expected_3.png
    expected = (8, 13)
    '''
    ID = 3
    width = 300
    heigth = 400
    expected = (8, 13)
    return do_test_func2(ID, width, heigth, expected)


def test_func2_4(run=True):
    '''
    txt_file = func2/in_4.txt
    output_imagefile = func2/your_image_4.png
    width = 500
    heigth = 200
    expected_imagefile = func2/expected_4.png
    expected = (32, 23)
    '''
    ID = 4
    width = 500
    heigth = 200
    expected = (32, 23)
    return do_test_func2(ID, width, heigth, expected)

# ----------------------------------- FUNC. 3 ----------------------------------- #

def do_test_func3(ID, color, expected):
    img_in  = f'func3/image0{ID}.png'
    img_out = f'func3/your_image0{ID}.png'
    img_exp = f'func3/expected0{ID}.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run

    res = program.func3(img_in, img_out, color)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il numero di segmenti colorati è sbagliato! / The number of colored segments is incorrect.\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    testlib.check_img_file(img_out, img_exp)
    return 1.5


def test_func3_1(run=True):
    '''
    imagefile = func3/image01.png
    output_imagefile = func3/expected01.png
    color = (255,0,0)
    '''
    ID = 1
    color = (255,0,0)
    expected = 1
    return do_test_func3(ID, color, expected)


def test_func3_2(run=True):
    '''
    imagefile = func3/image02.png
    output_imagefile = func3/expected02.png
    color = (255,0,0)
    '''
    ID = 2
    color = (255,0,0)
    expected = 1
    return do_test_func3(ID, color, expected)


def test_func3_3(run=True):
    '''
    imagefile = func3/image03.png
    output_imagefile = func3/expected03.png
    color = (100,160,200)
    '''
    ID = 3
    color = (100,160,200)
    expected = 45
    return do_test_func3(ID, color, expected)


def test_func3_4(run=True):
    '''
    imagefile = func3/image04.png
    output_imagefile = func3/expected04.png
    color = (0,0,0)
    '''
    ID = 4
    color = (0,0,0)
    expected = 90
    return do_test_func3(ID, color, expected)


# ----------------------------------- FUNC. 3 ----------------------------------- #

def do_test_func4(ID, W, H, color, expected):
    txt_in  = f'func4/rect_0{ID}.txt'
    img_out = f'func4/out_0{ID}.png'
    img_exp = f'func4/expected_0{ID}.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run

    res = program.func4(W, H, color, txt_in, img_out)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] L'area totale è sbagliata! / The total area is incorrect.\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    testlib.check_img_file(img_out, img_exp)
    return 1.5

def test_func4_1(run=True):
    '''
    L = 50
    A = 50
    sfondo = (0, 255, 0)
    file_rettangoli = func4/rect_01.txt
    imagefile_out = func3/out_01.png
    '''
    ID = 1
    L = A = 50
    color = (0,255,0)
    expected = 55
    return do_test_func4(ID, L, A, color, expected)


def test_func4_2(run=True):
    '''
    L = 150
    A = 50
    sfondo = (0, 0, 0)
    file_rettangoli = func4/rect_02.txt
    imagefile_out = func3/out_02.png
    '''
    ID = 2
    L = 150
    A = 50
    color = (0,0,0)
    expected = 5100
    return do_test_func4(ID, L, A, color, expected)

def test_func4_3(run=True):
    '''
    L = 200
    A = 200
    sfondo = (255, 255, 255)
    file_rettangoli = func4/rect_03.txt
    imagefile_out = func3/out_03.png
    '''
    ID = 3
    L = 200
    A = 200
    color = (255,255,255)
    expected = 9458
    return do_test_func4(ID, L, A, color, expected)

def test_func4_4(run=True):
    '''
    L = 500
    A = 200
    sfondo = (0, 255, 0)
    file_rettangoli = func4/rect_03.txt
    imagefile_out = func3/out_03.png
    '''
    ID = 4
    L = 500
    A = 200
    color = (255,255,255)
    expected = 63923
    return do_test_func4(ID, L, A, color, expected)

################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2, test_func1_3, test_func1_4,   # OK
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,   # OK
    test_func3_1, test_func3_2, test_func3_3, test_func3_4,   # OK
    test_func4_1, test_func4_2, test_func4_3, test_func4_4,   # OK
    test_personal_data_entry,
]


if __name__ == '__main__':
    if test_personal_data_entry() < 0:
        print(f"{COL['RED']}PERSONAL INFO MISSING. PLEASE FILL THE INITIAL VARS WITH YOUR NAME SURNAME AND STUDENT_ID{COL['RST']}")
        sys.exit()
    check_expected()
    testlib.runtests(   tests,
                        verbose=True,
                        logfile='grade.csv',
                        stack_trace=DEBUG)
################################################################################
