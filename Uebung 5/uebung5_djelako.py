#a1
# for i in range (1,3):
#     print('das ist i:', i)
#     for j in range(i):
#         print('j', j)
#         print('2. for:',i+j)

#a1 2.

# i=0; j=9
# while i<j:
#     print(i,j)
#     if i>=3:
#         break
#     i+=1
#     j-=1

#a1 3.

i=100
j=5
# while i>=0:
#     print(i)
#     i-=5

# for x in range( 0,i+1,5) :
#     if x<=100:
#         a=100-x
#         print(a)


##a2

# def schrauben():
        
#     Typ1= {
#     "Durchmesser": 3,
#     "Länge": 20
#     },

#     Typ2= {
#         "Durchmesser": 6,
#         "Länge": 30
#     },

#     Typ3= {
#         "Durchmesser": 20,
#         "Länge": 50
#     }
#     print(list)
#     print('geben sie eine Durchmesser an:')
#     Durchmesser= int(input())
#     print('geben sie eine Länge an:')
#     Länge= int(input())

#     # values= type.values()
#     # print(values)
#     # for key in Typ1:
#     #     if Durchmesser <= Typ1.key()[0] and Länge <= Typ1.key()[1]:
#     #         print('Schraube in von Typ1')
#     #     else:
#     #         print('egal')

#     if Durchmesser <=3 and Länge<=20:
#         print('Schrauibe is von Typ1')
#     elif Durchmesser <=6 and Länge<=30:
#         print('Schrauibe is von Typ2')
#     elif Durchmesser <=20 and Länge<=50:
#         print('Schrauibe is von Typ1')
#     else:
#         print('Unbekannter Schrauben Typ')
# schrauben()


###a3 Calendar

Monat = {"1":31,
        "2":28,
        "3":31,
        "4":30,
        "5":31,
        "6":30,
        "7":31,
        "8":31,
        "9":30,
        "10":31,
        "11":30,
        "12":31
        }
print("geben sie den Monat an:")
monat= str(input())

print("geben sie das Jahr an:")
jahr= int(input())


if ((jahr%400 ==0) and monat=='2'):
    print('der 2. Monat des Jahres',jahr,'hat 29 Tgae')
else:
    print('der',monat,'. Monat des Jahr',jahr,'hat',Monat[monat],'Tage')

