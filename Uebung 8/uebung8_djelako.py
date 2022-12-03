#1
def vielfach(number):
    liste=[]
    for i in range (1,101):
        liste.append(i*number)
    filtered= filter(lambda x:(x in range(1,101)),liste)#return x in liste for x in range (1,101)
    print(list(filtered))##kovertierung in list notwendig
#vielfach(7)

###2

vokalen=['a','e','i','o','u','ä','ö','ü']
word='Hello, World'
def extraktion(word):
    filtered= filter(lambda x: x in vokalen, word)
    liste = list(filtered)
    zeichnenkette=''.join(liste)
    print(zeichnenkette)
#extraktion(word)

#####3

liste = ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So']

def vertauschen (liste:list,i,j):
    letter1=liste[i-1]
    letter2=liste[j-1]

    liste[i-1]=letter2
    liste[j-1]=letter1

    print(liste)
vertauschen(liste,1,8)