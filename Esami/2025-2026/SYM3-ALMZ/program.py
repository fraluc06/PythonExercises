#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# %%

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare la simulazione e' necessario ottenere il punteggio 18 o più.
(15 per studenti con DSA)

Il voto finale e' la somma dei punteggi dei problemi risolti.
"""
nome       = "A"
cognome    = "S"
matricola  = "42"

################################################################################
################################################################################
################################################################################
# ---------------------------- DEBUG SUGGESTIONS ----------------------------- #
# To run only some of the tests, you can comment the entries with which the
# 'tests' list is assigned at the end of grade.py
################################################################################


# %% ---------------------------- FUNC 1 ---------------------------- #

'''
Func 1: 8 punti
Si definisca la funzione func1(png_input) che riceve come argomento:
- png_input:  il percorso di una inmagine PNG

Il file png_input contiene una immagine a sfondo nero, contenente stelline,
ovvero crocette di dimensione 3x3 pixel in diagonale di colori qualsiasi.
Esempio:
.x.x....
..xo.o..
.x.xo...
...o.o..
........

Nell'esempio sono presenti una stellina di colore 'x' ed una di colore 'o'.

Assumete che due qualsiasi stelline dello stesso colore siano separate da almeno un pixel
e quindi non si toccano nè in orizzontale/verticale nè in diagonale.
Assumete che i pixel della immagine siano solo stelline o sfondo nero.

La funzione deve contare il numero di stelline presenti, per ciascun colore
e tornare un dizionario che ha come chiavi i colori delle stelline presenti nell'immagine
e come valori il numero di stelline di quel colore.

Esempio:
Se l'immagine è 'func1/in_2.png' il risultato sarà il dizionario
{(150, 200, 150): 3, (200, 150, 125): 4, (125, 175, 200): 2,
(125, 100, 125): 3, (125, 175, 125): 4, (200, 100, 150): 2}

'''

import images

def func1_bis(png_input):
    pass
    # Inserisci qui il tuo codice

    # idea 1: trova i centri e contali
    # leggo l'immagine
    nero = 0,0,0
    img = images.load(png_input)
    L = len(img[0])
    A = len(img)
    D = {}
    # scandisco i pixel x,y della immagine
    for y, riga in enumerate(img):
        for x, pixel in enumerate(riga):
            if (pixel != nero and  0 < x < L-1 and 0 < y < A-1 and
               pixel == img[y-1][x-1] == img[y-1][x+1] == img[y+1][x-1] == img[y+1][x+1]):
                if pixel in D:
                    D[pixel] += 1
                else:
                    D[pixel]  = 1
    return D
                    
    # quando trovo un centro lo conteggio col suo colore


def func1(png_input):
    pass
    
    # idea 2: conta i colori e dividi per 5
    img = images.load(png_input)
    D = {}
    for riga in img:
        for pixel in riga:
            if pixel != (0,0,0):
                if pixel in D:
                    D[pixel] += 1
                else:
                    D[pixel]  = 1
    for colore in D:
        D[colore] //= 5
    return D



# print(func1('func1/in_2.png'))
# %% ----------------------------------- FUNC2 ------------------------- #
'''
Func 2: 10 punti
Si definisca la funzione func2(txt_input, width, height, png_output) che riceve come argomenti

- txt_input:  il percorso di un file che contiene un elenco di figure da disegnare
- width:      larghezza in pixel dell'immagine da creare
- height:     altezza in pixel dell'immagine da creare
- png_output: il percorso di una immagine PNG che dovete creare, contenente le figure

La funzione deve creare una immagine a sfondo nero e disegnarci sopra
tutte le figure indicate nel file 'txt_input', nell'ordine in cui
appaiono nel file.

Il file txt_file contiene, una per riga, separate da spazi:
- una parola che indica il tipo di figura da disegnare
- le tre componenti R G B del colore da usare
- le coordinate e gli altri parametri necessari a definire la figura

Possono essre presenti 2 tipi di figura:
- diagonale discendente di un quadrato (in direzione -45°)
    diagonalDOWN R G B x y L
    La diagonale inizia nel punto (x,y), si dirige in BASSO a destra, ed è lunga L pixel
- diagonale ascendente di un quadrato (in direzione +45°)
    diagonalUP R G B x y L
    La diagonale inizia nel punto (x,y), si dirige in ALTO a destra, ed è lunga L pixel

Quindi deve salvare l'immagine ottenuta nel file 'png_output' usando la funzione images.save.
Inoltre deve ritornare il numero di diagonali disegnate dei due tipi
come tupla dei due valori (DIAGUP,DIAGDOWN)

NOTA: va gestito correttamente lo sbordare delle figure dalla
immagine, infatti sono ammesse anche coordinate negative, e dimensioni
o parametro L tali da far sbordare la figura dalla immagine

Esempio: se il file func2/in_1.txt contiene le 3 righe
diagonalDOWN 0 255 0 -30 -40 110
diagonalUP 255 0 0 20 100 200
diagonalUP 0 0 255 10 120 50

l'esecuzione della funzione func2('func2/in_1.txt', 50, 100, 'func2/your_image_1.png')
produrrà una figura uguale al file 'func2/expected_1.png'
e tornerà la coppia (2, 1)
'''

def func2(txt_input, width, height, png_output):
    pass
    # Inserisci qui il tuo codice

    # idea: leggi il file, disegna le diagonali un pixel alla volta, 
    #       contando e colorando solo i pixel dentro l'immagine
    figure = leggi_file_txt(txt_input)
    img = [ [ (0,0,0) for _ in range(width) ] for _ in range(height) ]

    U = D = 0
    for figura, colore, x, y, L in figure:
        if figura == 'diagonalDOWN':
            diagonalDown(img, colore, x, y, L)
            D += 1
        else:
            diagonalUp(img, colore, x, y, L)
            U += 1
    images.save(img, png_output)
    return U, D

def leggi_file_txt(txt_input):
    figure = []
    with open(txt_input, encoding='utf8') as F:
        for riga in F:
            if riga.strip() == '': continue
            fig, R, G, B, x, y, L = riga.split()
            figura = fig, (int(R), int(G), int(B)), int(x), int(y), int(L)
            figure.append(figura)
    return figure

def diagonalDown(img, colore, x, y, L):
    W = len(img[0])
    H = len(img)
    for _ in range(L):
        if 0 <= x < W and 0 <= y < H:
            img[y][x] = colore
        x += 1
        y += 1

def diagonalUp(img, colore, x, y, L):
    W = len(img[0])
    H = len(img)
    for _ in range(L):
        if 0 <= x < W and 0 <= y < H:
            img[y][x] = colore
        x += 1
        y -= 1



# print(leggi_file_txt('func2/in_4.txt'))

# print(func2('func2/in_1.txt', 50, 100, 'func2/out_1.png'))

# %% ----------------------------------- FUNC3 ------------------------- #
""" func3: 6 points
Si scriva una funzione func3(imagefile, output_imagefile, color) che prende
in ingresso due stringhe che rappresentano due nomi di file di immagini PNG.
L'immagine nel file 'imagefile' contiene esclusivamente segmenti orizzontali
bianchi su uno sfondo nero. Ogni riga ha al più un segmento bianco.
La funzione deve creare una nuova immagine in cui sono presenti gli stessi
segmenti dell'immagine in ingresso e modificare il colore dei segmenti con
lunghezza massima utilizzando il colore color preso in ingresso.

L'immagine così ottuenuta deve essere salvata in formato PNG nel file con
percorso output_imagefile.

La funzione ritorna il numero di segmenti colorati nell'immagine in output.
"""
import images
def func3(imagefile, output_imagefile, color):
    pass
    # Inserisci qui il tuo codice

    # idea: trova la lunghezza e posizione di ciascun segmento
    #       trova la lunghezza massima
    #       conta e colora i segmenti con quella lunghezza
    img = images.load(imagefile)
    segmenti = trova_segmenti(img)   # -> lista di (x,y,L)
    lunghezza_massima = max( [ L for x,y,L in segmenti ])
    quanti = 0
    for x,y,L in segmenti:
        if L == lunghezza_massima:
            quanti += 1
            for X in range(L):
                img[y][x+X] = color
    images.save(img,output_imagefile)
    return quanti

def trova_segmenti(img):
    bianco = 255, 255, 255
    segmenti = []
    for y, riga in enumerate(img):
        minx = -1
        maxx = None
        for x, pixel in enumerate(riga):
            if pixel == bianco:
                if minx == -1:
                    minx = x
                maxx = x
        if minx != -1:
            segmenti.append((minx, y, maxx-minx+1))
    return segmenti

# print(func3('func3/image01.png', 'func3/your_image01.png', (255,0,0)))

# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 points
Si definisca la funzione func4(L, A, sfondo, file_rettangoli, imagefile_out) 
che riceve come argomenti:
    - la larghezza L, altezza A e colore di sfondo di una immagine da creare
    - il path di un file che contiene, su ciascuna riga, i parametri di un rettangolo
    - il path imagefile_out in cui salvere l'immagine ottenuta
Il file dei rettangoli contiene su ciascuna riga 7 valori
    - x, y, larghezza, altezza, R, G, B
    dove x, y sono le coordinate dell'angolo in alto a sinistra del rettangolo.    
    NOTA: i rettangoli potrebbero sbordare dall'immagine
La funzione deve:
    - disegnare nell'ordine i rettangoli pieni per la parte contenuta nella immagine
    - sommare il numero di pixel di ciascun rettangolo che sono stati disegnati
        nell'immagine (anche se successivamente sovrascritti, ed escludendo quelli 
        esterni all'immagine)
    - restituire tale somma
"""
import images
def func4(L : int, A : int, sfondo : tuple[int,int,int], file_rettangoli : str, imagefile_out : str) -> int:
    pass
    # Inserisci qui il tuo codice

    img = [ [ sfondo for _ in range(L) ] for _ in range(A) ]
    N = 0
    # Idea: leggi il file dei rettangoli
    rettangoli = leggi_rettangoli(file_rettangoli)
    #       disegna ciascun rettangolo pixel per pixel
    for x, y, larghezza, altezza, colore in rettangoli:
        N += disegna_rettangolo(img, x, y, larghezza, altezza, colore, L, A)
    #       conta i pixel solo se disegnati dentro l'immagine
    images.save(img, imagefile_out)
    return N

def disegna_rettangolo(img, x, y, larghezza, altezza, colore, L, A):
    N = 0
    for dx in range(larghezza):
        for dy in range(altezza):
            X = x + dx
            Y = y + dy
            if  0 <= X < L and 0 <= Y < A:
                img[Y][X] = colore
                N += 1
    return N



def leggi_rettangoli(filename):
    rettangoli = []
    with open(filename, encoding='utf8') as F:
        for riga in F:
            if '' == riga.strip(): continue
            x, y, larghezza, altezza, R, G, B = [int(X) for X in riga.split()]
            rettangoli.append((x, y, larghezza, altezza, (R,G,B)))
    return rettangoli

# print(leggi_rettangoli('func4/rect_01.txt'))


# print(func4(50,50,(0,255,0),'func4/rect_01.txt', 'func4/out_01.png'))    # 67
