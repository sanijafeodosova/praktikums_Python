"""
    Funkcija Bilde akceptē divus argumentus - skaiļus a un b,
    aprēķina to kubu summu un atgriež to.
    Pārbaudiet funkcijas darbību ar dažādiem argumentiem, 
    nosakot trīs simbolus aiz komata.

    Argumenti:
        a {int vai float} -- pirmais skaitlis
        b {int vai float} -- otrais skaitlis
    Atgriež:
        int vai float -- argumentu summa
    
"""
import math

def Bilde(a,b):
    summa=pow(a,3)+pow(b,3)
    return summa

print(Bilde(2,1))