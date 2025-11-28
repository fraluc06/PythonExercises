#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
nome       = "NOME"
cognome    = "COGNOME"
matricola  = "MATRICOLA"

################################################################################
################################################################################
################################################################################
# ---------------------------- DEBUG SUGGESTIONS ----------------------------- #
# To run only some of the tests, you can comment the entries with which the
# 'tests' list is assigned at the end of grade.py
################################################################################


#%% ---------------------------- FUNC 1 ---------------------------- #

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

def func1(png_input):
    pass
    # Inserisci qui il tuo codice

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
    
# print(func4(50,50,(0,255,0),'func4/rect_01.txt', 'func4/out_01.png'))    # 67
