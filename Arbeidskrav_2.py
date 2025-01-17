
"""Arbeidsskrav 2 - PY1010-1 24H Grunnleggende programmering med Python
-Alexander Bårdsen
"""
# Oppgave 1

år = 2024 

alder = int(input("hvilket år er du født? "))

print(f"Dersom du er født i {alder} og året i år er {år}. Da er du {år-alder} gammel")

# Oppgave 2

import math

Pizza_per_elev = 1/4 

antall_elever = int(input("skriv inn antall elever? "))


resultat = (antall_elever * Pizza_per_elev)


runder_opp_resultat = math.ceil(resultat) # Benytter meg av funksjonen mat.ceil for å runde opp til nærmeste integer. 


print(f"Det må handles inn {runder_opp_resultat} pizzaer til festen")


# oppgave 3

import numpy as np

v_grad = float(input("Skriv inn gradtallet: "))

def grader_til_radianer(grader):
    radianer = grader * (np.pi/180)
    return radianer
 

radianer = grader_til_radianer(v_grad)

print(f"{v_grad} grader er {radianer} radianer")

   

# Oppgave 4

#a
data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike":["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

#b

for land in data: 
    print(land) # Ønsker å gi en oversikt i konsollen over valg alternativene. Benytter meg derfor av en for loop
print()
velg_land = input("Hvilket av disse lande ønsker du informasjon om? \n")
print(f"Hovedstaden i landet er {data[velg_land][0]} og det er {data[velg_land][1]} millioner innbyggere i hovedstaden")

#c
## Benytter meg av en while loop i oppgave 5c) for at spørrringen skal repetere seg dersom man ønsker å legge til flere land.

while True:
    nytt_land = input("Ønsker du å legge til et nytt land? Velg ja eller nei ")
    
    if nytt_land.lower() == "ja":
        nytt_land_valg = input("hvilket land? ")
        hovedstad = input("hva er hovedstaden? ")
        innbyggere = input("hvor mange innbyggere er det? ")
        data[nytt_land_valg] = [hovedstad, innbyggere]
    elif nytt_land.lower() == "nei":
        print("Du har valgt å ikke legge til flere land i dictionary dataen")
        break
    else:
        print("Svaret du har gitt er ikke gyldig. Du må svare enten ja eller nei")    
print(data)


# oppgave 5

import math

pi = math.pi

a = float(input("Skriv inn lengden av a: "))

b = float(input("Skriv inn lengden av b: "))

# I funksjonen under benyttes to formelle innargumenter. Hentet fra input fra variabel a og b

def Beregn_figur(a,b):
    
    radius = a/2 
    areal_halv_sirkel = 0.5 * pi * (radius**2)

    areal_trekant = 0.5 * a * b
    
    total_areal = areal_halv_sirkel + areal_trekant 

        
    omkrets_halv_sirkel = 0.5 * 2 * pi * radius
    omkrets_skrålinje = math.sqrt(a**2 + b**2)
    ytre_omkrets = omkrets_halv_sirkel + omkrets_skrålinje + b    
    
    return total_areal, ytre_omkrets
 
total_areal, ytre_omkrets = Beregn_figur(a, b)

print(f'Arealet til figuren er {total_areal:.2f} kvm')
print(f'Ytre omkretsen til figuren er {ytre_omkrets:.2f} meter')


## oppgave 6

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
         
fun_x = -x**2 -5

plt.plot(x, fun_x, linestyle= "dotted", color="black")
plt.xlabel("x")
plt.ylabel("Plotting av funksjonen f(x)")
plt.grid()
plt.show()
    

