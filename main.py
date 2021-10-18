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


def daca_sunt_cres(l):
    rezultat=[]
    for x in l:
        if x>=0:
            rezultat.append(x)
    for i in range (len(rezultat)-1):
        if rezultat[i]>rezultat[i+1]:
            return False
    return True
def test_daca_sunt_cresc():
    assert daca_sunt_cres([1,-2,4,8,-6]) is True
    assert daca_sunt_cres([1,-2,4,8,3]) is False
    assert daca_sunt_cres([-1,34,2,8]) is False

test_daca_sunt_cresc()
def nr_divizori(n):
    divizori=0
    d=2
    while d<n:
        if n%d==0:
            divizori+=1
        d+=1
    return divizori

def test_nr_divizori():
    assert nr_divizori(3)==0
    assert nr_divizori(25)==1

test_nr_divizori()

def afisare_care_apare_o_singura_data(l):
    """
    Afișarea listei obținute din lista inițială în care numerele care apar doar o singură dată sunt
înlocuite cu numărul de divizori proprii ai numărului.
    :param l:lista care trebuie verificata
    :return:Se returneaza o noua lista
    """
    rezultat=[]
    for i in range (len(l)):
        ok=1
        for j in range(len(l)):
            if l[i]==l[j] and i!=j:
                ok=0
        if ok==1:
            rezultat.append(nr_divizori(l[i]))
        else:
            rezultat.append(l[i])
    return rezultat

def test_afisare_care_apare_o_singura_data():
    assert afisare_care_apare_o_singura_data([25,13,13,19])==[1,13,13,0]
    assert afisare_care_apare_o_singura_data([3,5,9])==[0,0,1]
    assert afisare_care_apare_o_singura_data([13,13,13])==[13,13,13]

test_afisare_care_apare_o_singura_data()