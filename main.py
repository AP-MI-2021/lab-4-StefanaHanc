def afisare_meniu():
    print("MENIU")
    print("1.Citeste datele ")
    print("2.Afișarea listei după eliminarea duplicatelor")
    print("3.Afișarea sumei primelor n numere pozitive din listă, unde n se citește de la tastatură.")
    print("4. Afișarea tuturor float-urilor ale căror parte fracționară este palindrom")
    print("5.Afișarea listei obținute din lista inițială în care float-urile cu partea întreagă a radicalului număr prim sunt puse ca string-uri cu caracterele în ordine inversă.")
    print("6.Iesire")


def citireLista():
    l = []
    givenString = input("Dati lista, cu elementele separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l

def afisarelistafaraduplicate(l):
    """
    Afișarea listei după eliminarea duplicatelor
    :param l: Lista pe care o verificam
    :return: Returnam lista fara duplicate
    """
    rezultat=[]
    for i in range(len(l)):
        ok=1
        for j in range(len(rezultat)):
            if l[i]==rezultat[j]:
                ok=0
        if ok==1:
            rezultat.append(l[i])
    return rezultat

def testafisarefaraduplicate():
    assert afisarelistafaraduplicate([12,23,45,12,10])==[12,23,45,10]
    assert afisarelistafaraduplicate([12,12,12,12])==[12]
    assert afisarelistafaraduplicate([12,12,13])==[12,13]

testafisarefaraduplicate()

def afisarea_primelor_n_nr(l,n):
    """
    Afișarea sumei primelor n numere pozitive din listă, unde n se citește de la tastatură. 
    :param l:Lista verifiata
    :param n:Cele n numere citite
    :return: Suma in caz ca exista n numere pozitiva ,none in caz ca nu exista 
    """
    s=0
    for x in l:
        if x>0 and n!=0:
            s=s+x
            n=n-1
    if n!=0:
        return None
    else:
        return s

def test_afisare_primele_n_numere():
    assert afisarea_primelor_n_nr([10,3,-25,1,4],3)==14
    assert afisarea_primelor_n_nr([10,-2,-3],2)is None
    assert afisarea_primelor_n_nr([10,12,2,-2,-2],3)==24

test_afisare_primele_n_numere()