#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    if len(string)%2==0:
        result=True
    else:
        result=False
    return result



def remove_third_char(string: str) -> str:
    liste=list(string)
    liste.pop(2)
    new_string=''.join([str(car) for car in liste])
    return new_string



def replace_char(string: str, old_char: str, new_char: str) -> str:
    liste=list(string)
    for i in range(len(liste)):
        if liste[i] == old_char:
            liste[i] =new_char
    new_string=''.join([str(car) for car in liste])
    return new_string



def get_number_of_char(string: str, char: str) -> int:
    liste=list(string)
    n=0
    for i in range(len(liste)):
        if liste[i]==char:
            n+=1
    return n


def get_number_of_words(sentence: str, word: str) -> int:
    mot=sentence.split()
    n=0
    for i in range(len(mot)):
        if mot[i]==word:
            n+=1
    return n



def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
