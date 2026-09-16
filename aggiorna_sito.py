# -*- coding: utf-8 -*-
"""Copia le due mappe costruite dentro il sito pubblicato.

Le mappe si costruiscono nelle rispettive cartelle di lavoro, che stanno accanto a
questa e non fanno parte di questo repository:

    ../Atlante_Roma_2021/atlante_roma2021.html   (build_dati_roma2021.py + build_pagina.py)
    ../Atlante_Sezioni/atlante.html              (build_pagina.py)

Qui dentro diventano roma-2021/index.html e europee-2024/index.html, cioe' i due
percorsi che GitHub Pages serve. Se una cartella di partenza non c'e', lo script lo
dice e lascia la copia che c'e' gia': meglio un sito vecchio di un sito rotto.

Uso: python aggiorna_sito.py
"""
import io, os, shutil

QUI = os.path.dirname(os.path.abspath(__file__))
FUORI = os.path.dirname(QUI)

COPIE = [
    # l'atlante con le tornate: e' quello buono, gli altri due restano per non
    # rompere gli indirizzi gia' in giro
    (os.path.join(FUORI, 'Atlante_Unificato', 'atlante.html'),
     os.path.join(QUI, 'atlante', 'index.html')),
    (os.path.join(FUORI, 'Atlante_Roma_2021', 'atlante_roma2021.html'),
     os.path.join(QUI, 'roma-2021', 'index.html')),
    (os.path.join(FUORI, 'Atlante_Sezioni', 'atlante.html'),
     os.path.join(QUI, 'europee-2024', 'index.html')),
]


def main():
    fatte, saltate = 0, 0
    for sorgente, destinazione in COPIE:
        nome = os.path.relpath(destinazione, QUI).replace(os.sep, '/')
        if not os.path.exists(sorgente):
            print('  SALTATA  %-24s sorgente assente: %s' % (nome, sorgente))
            saltate += 1
            continue
        prima = os.path.getsize(destinazione) if os.path.exists(destinazione) else 0
        if prima and io.open(sorgente, 'rb').read() == io.open(destinazione, 'rb').read():
            print('  invariata %-23s %.2f MB' % (nome, prima / 1048576.0))
            continue
        os.makedirs(os.path.dirname(destinazione), exist_ok=True)
        shutil.copyfile(sorgente, destinazione)
        print('  copiata  %-24s %.2f MB' % (nome, os.path.getsize(destinazione) / 1048576.0))
        fatte += 1
    print('\n%d file aggiornati, %d saltati.' % (fatte, saltate))
    if fatte:
        print('Ora: git add -A && git commit && git push')


if __name__ == '__main__':
    main()
