# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 21:34:19 2022

@author: djela
"""
import random

# a1 Ü3

##okatl in bin
#i=750;
#print("Der binäre Code von 750 ist:", bin(750));

##random number between 1, 49 -->import the random bib first
#print(random.randint(1, 49));

##random number bettwen 0,0 and 10,0 1 comma
#print(round(random.uniform(0.0, 10.0),1));

##Geldbeträge ohne Rundungsfehler


##True == 1

####Anführungszeichnen
#print("hello" + "''")

##Extrahieren
#var = 'bla [wichtig] mehr bla'
#print(var.replace('wichtig', ''))

##rechtbündigkeit str.rjust(Breite[, Füllzeichen]), kein füllzeichen=leer
#string= 'hello world'
#print(string.rjust(50))

##umgekehrte Reihenfolge
#var='Hello, World'
#print(var[::-1])

##A2 Ü3
##zahl= float(input ("geben sie eine komma Zahl ein: ")) #fractionnl part auf a float
##var=913.745673849
##print(var%1)


######a1 ü4


a=3; b=3; c=4
print(a is c)
# == gleichheit test is test ob die variable auf das gleiche Objekt zeigen

#rest der division
print(225%17)

#daten typ
a=1+2*3**4; b=100<a<200
print("typ a ist", type(a), "typ b ist", type(b))

#a2
print("enter anfangskapital wert:")
k=float(input())
print("die anfangskapital ist:" + str(k) + "Euro")
print("enter Zinssatzt:")
p=float(input())
print("die Zinsatzt ist:" + str(p)+ "%")
print("enter jahren:")
n=float(input())
print("das Jahr ist:" + str(k))
kn =k*(((1+(p/100)))**n)
print("Verzisung für" + str(k) +"Euro"+ "ist" + str(kn))

# zahlen =[[2,4,3],[4,"acht"], "sieben"]
# print("zahlen sind :", zahlen[1][0])
# for zahl in zahlen:
#     print(zahl)