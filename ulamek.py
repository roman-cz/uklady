from tkinter import *
from tkinter import messagebox
import random


class Ulamek:
    def __init__(self, c=0, l=0, m=1):
        self.c = c
        self.l = l
        if m != 0:
            self.m = m
        else:
            self.m = 1

    def __str__(self):
        if self.l == 0:
            return '%s' % self.c
        elif self.c == 0:
            return '%s/%s' % (self.l, self.m)
        else:
            return '%s %s/%s' % (self.c, self.l, self.m)

    def __add__(self, inny):
        c = self.c + inny.c
        l = self.l * inny.m + inny.l * self.m
        m = self.m * inny.m
        k = nwd(l, m)
        l = l // k
        m = m // k
        return Ulamek.skrocUlamek(Ulamek.wylaczCalosc(Ulamek(c, l, m)))

    def dodajUlamki(self, inny):  # dodaje ułamki o wspólnym mianowniku użyte do nauki dodawania
        c = self.c + inny.c
        l = self.l + inny.l
        m = self.m
        return Ulamek(c, l, m)

    def czy_da_wyl(self, znak=""):
        # sprawdza czy mozna wylaczyc calosci; jesli tak wywoluje wylaczćalosc
        if self.l == 0:
            ost1 = self
        elif self.l >= self.m:
            tekstbox.insert(END, "\n\nWyłącz całości\n")
            petla()
            ost = self
            ost1 = Ulamek.wylaczCalosc(ost)
            t = "\n... = %s %s \n" % (znak, ost1)
            tekstbox.insert(END, t)
        else:
            ost1 = self
        return ost1

    def czy_da_skr(self, znak=""):  # sprawdza czy ulamek da sie skrocic, jesli tak wywoluje skrocUlamek
        if nwd(self.l, self.m) > 1:
            tekstbox.insert(END, "\n\nSkróć jeszcze ułamek\n")
            petla()
            ost3 = Ulamek.skrocUlamek(self)
            t = "\n... = %s %s \n" % (znak, ost3)
            tekstbox.insert(END, t)
        else:
            ost3 = self
        return ost3

    def wylaczCalosc(self):
        c = self.c + self.l // self.m
        l = self.l % self.m
        m = self.m
        return Ulamek(c, l, m)

    def skrocUlamek(self):
        c = self.c
        l = self.l // nwd(self.l, self.m)
        m = self.m // nwd(self.l, self.m)
        return Ulamek(c, l, m)


def nwd(a, b):
    if a == 0 or b == 0:
        return 1
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


def nww(a, b):
    return a * b // nwd(a, b)


def petla():
    m = messagebox.showinfo("KOLEJNY KROK", "Spróbuj policzyć samemu, gdy będzesz gotów naciśnij OK")


def podajwynik(self):
    # drukuje wynik, sprawdza czy mozna wyciagnac calosci i skrocic i jesli mozna robi to
    t = "... =  %s" % (self)
    tekstbox.insert(END, t)
    ost2 = Ulamek.czy_da_wyl(self)
    ost = Ulamek.czy_da_skr(ost2)
    tekstbox.insert(END, "\n\n   GOTOWE!!!")


def dodawanie(x, y):
    if x.m != y.m:
        if nwd(x.l, x.m) > 1:
            tekstbox.insert(END, "\n\nSkróć pierwszy ułamek\n\n")
            petla()
            x = Ulamek.skrocUlamek(x)
            t = "... = %s + %s =" % (x, y)
            tekstbox.insert(END, t)
        if nwd(y.l, y.m) > 1:
            tekstbox.insert(END, "\n\nSkróć drugi ułamek\n\n")
            petla()
            y = Ulamek.skrocUlamek(y)
            t = "... = %s + %s =" % (x, y)
            tekstbox.insert(END, t)
        if x.l >= x.m:
            tekstbox.insert(END, "\n\nWyłącz całości z pierwszego ułamka\n\n")
            x = Ulamek.wylaczCalosc(x)
            petla()
            t = "... = %s + %s =" % (x, y)
            tekstbox.insert(END, t)
        if y.l >= y.m:
            tekstbox.insert(END, "\n\nWyłącz całości z drugiego ułamka\n\n")
            y = Ulamek.wylaczCalosc(y)
            petla()
            t = "... = %s + %s =" % (x, y)
            tekstbox.insert(END, t)

    if x.m != y.m and x.l != 0 and y.l != 0:

        tekstbox.insert(END, "\n\nSprowadź ułamki do wspólnego mianownika\n")

        petla()
        nm1 = nww(x.m, y.m)
        nm2 = nww(x.m, y.m)
        nl1 = nm1 // x.m * x.l
        nl2 = nm2 // y.m * y.l
        s1 = Ulamek(x.c, nl1, nm1)
        s2 = Ulamek(y.c, nl2, nm2)
        t = "\n... = %s + %s = \n" % (s1, s2)
        tekstbox.insert(END, t)
        tekstbox.insert(END, "\n\nDodaj teraz całości do całości, licznik do licznika i przepisz wspólny mianownik\n\n")
        petla()
        suma = Ulamek.dodajUlamki(s1, s2)
    elif x.m == y.m and x.l != 0:
        tekstbox.insert(END, "\n\nDodaj całości i ułamki\n\n")
        petla()
        suma = Ulamek.dodajUlamki(x, y)
    else:
        tekstbox.insert(END, "\n\nDodaj do siebie obie liczy całkowite\n\n")
        petla()
        if x.l == 0:
            x.m = y.m
        if y.l == 0:
            y.m = x.m
        suma = Ulamek.dodajUlamki(x, y)

    return suma


def mnozenie(x, y):
    """Funkca wykonuje mnozenie dwoch ulamkow zwyklych"""
    if nwd(x.l, x.m) > 1:
        tekstbox.insert(END, "\n\nSkróć pierwszy ułamek\n\n")
        petla()
        x = Ulamek.skrocUlamek(x)
        t = "... = %s * %s =" % (x, y)
        tekstbox.insert(END, t)
    if nwd(y.l, y.m) > 1:
        tekstbox.insert(END, "\n\nSkróć drugi ułamek\n\n")
        petla()
        y = Ulamek.skrocUlamek(y)
        t = "... = %s * %s =" % (x, y)
        tekstbox.insert(END, t)

    if x.l == 0 and y.l == 0:
        tekstbox.insert(END, "\n\nW tym przypadku pomnóż przez siebie obie liczby całkowite\n\n")
        petla()
        wynik_c = x.c * y.c
        wynik_l = 0
        wynik_m = 1
        wynik = Ulamek(wynik_c, wynik_l, wynik_m)
    elif x.l == 0 or y.l == 0:
        tekstbox.insert(END,
                        "\n\nW takim przypadku najprościej pomnożyć liczbę całkowitą przez liczbę całkowitą\noraz przez licznik ułamka\n\n")
        petla()
        if x.l == 0:
            wynik_c = x.c * y.c
            wynik_l = x.c * y.l
            wynik_m = y.m
            wynik = Ulamek(wynik_c, wynik_l, wynik_m)
        else:
            wynik_c = x.c * y.c
            wynik_l = y.c * x.l
            wynik_m = x.m
            wynik = Ulamek(wynik_c, wynik_l, wynik_m)
    elif x.c != 0 and y.c != 0:
        tekstbox.insert(END, "\n\nZamień obie liczby mieszane na ułamki niewłaściwe\n")
        petla()
        l1 = x.m * x.c + x.l
        l2 = y.m * y.c + y.l
        x = Ulamek(0, l1, x.m)
        y = Ulamek(0, l2, y.m)
        t = "\n... = %s * %s =" % (x, y)
        tekstbox.insert(END, t)
        wynik = wymnoz(x, y)
    elif x.c == 0 and y.c != 0:
        tekstbox.insert(END, "\n\nZamień drugi ułamek na niewłaściwy\n")
        petla()
        l2 = y.m * y.c + y.l
        y = Ulamek(0, l2, y.m)
        t = "\n... = %s * %s =" % (x, y)
        tekstbox.insert(END, t)
        wynik = wymnoz(x, y)
    elif x.c != 0 and y.c == 0:
        tekstbox.insert(END, "\n\nZamień pierwszy ułamek na niewłaściwy\n")
        petla()
        l1 = x.m * x.c + x.l
        x = Ulamek(0, l1, x.m)
        t = "\n... = %s * %s =" % (x, y)
        tekstbox.insert(END, t)
        wynik = wymnoz(x, y)
    else:
        wynik = wymnoz(x, y)

    return wynik


def wymnoz(a, b):
    if nwd(a.l, a.m) > 1:
        tekstbox.insert(END, "\n\nSkróć pierwszy ułamek\n")
        petla()
        a = Ulamek.skrocUlamek(a)
        t = "\n... = %s * %s =" % (a, b)
        tekstbox.insert(END, t)
    if nwd(b.l, b.m) > 1:
        tekstbox.insert(END, "\n\nSkróć drugi ułamek\n")
        petla()
        b = Ulamek.skrocUlamek(b)
        t = "\n... = %s * %s =" % (a, b)
        tekstbox.insert(END, t)
    if nwd(a.l, b.m) > 1:
        tekstbox.insert(END, "\n\nSkróć licznik pierwszego ułamka z mianownikiem drugiego ułamka\n")
        petla()
        k = nwd(a.l, b.m)
        a.l = a.l // k
        b.m = b.m // k
        t = "\n... = %s * %s =" % (a, b)
        tekstbox.insert(END, t)
    if nwd(a.m, b.l) > 1:
        tekstbox.insert(END, "\n\nSkróć licznik drugiego ułamka z mianownikiem pierwszego ułamka\n")
        petla()
        k = nwd(a.m, b.l)
        a.m = a.m // k
        b.l = b.l // k
        t = "\n... = %s * %s =" % (a, b)
        tekstbox.insert(END, t)
    tekstbox.insert(END, "\n\nPomnóż licznik przez licznik, a potem mianownik przez mianownik\n\n")
    petla()
    w = Ulamek(0, a.l * b.l, a.m * b.m)
    return w


def dzielenie(x, y):
    if nwd(x.l, x.m) > 1:
        tekstbox.insert(END, "\n\nSkróć pierwszy ułamek\n\n")
        petla()
        x = Ulamek.skrocUlamek(x)
        t = "... = %s : %s =" % (x, y)
        tekstbox.insert(END, t)
    if nwd(y.l, y.m) > 1:
        tekstbox.insert(END, "\n\nSkróć drugi ułamek\n\n")
        petla()
        y = Ulamek.skrocUlamek(y)
        t = "... = %s : %s =" % (x, y)
        tekstbox.insert(END, t)

    if x.l == 0 and y.l == 0 and y.c != 0:
        tekstbox.insert(END,
                        "\n\nW tym przypadku wynikiem dzielenia jest ułamek,\nktórego licznikiem jest pierwsza liczba, a mianownikiem druga\n\n")
        petla()
        wynik_c = 0
        wynik_l = x.c
        wynik_m = y.c
        wynik = Ulamek(wynik_c, wynik_l, wynik_m)
        return (wynik)
    elif x.c == 0 and y.c == 0 and y.l != 0:
        tekstbox.insert(END, "\n\nW tym przypadku zamień dzielenie na mnożenie:\n ")
        tekstbox.insert(END, "Ułamek pierwszy przepisz bez zmian, poten napisz znak mnożenia i odwrócony drugi ułamek")
        petla()
        y.l, y.m = y.m, y.l
        t = "\n... = %s * %s =" % (x, y)
        tekstbox.insert(END, t)
        return (mnozenie(x, y))
    else:
        tekstbox.insert(END,
                        "\n\nW tym przypadku zamień obydwa ułamki na niewłaściwe, a następnie przepisz\npierwszy ułamek, napisz znak mnożenia i odwrotność drugiego ułameka\n")
        x = Ulamek(0, x.m * x.c + x.l, x.m)
        y = Ulamek(0, y.m * y.c + y.l, y.m)
        t = "\n... = %s : %s =" % (x, y)
        petla()
        tekstbox.insert(END, t)
        y = Ulamek(0, y.m, y.l)
        t = " %s * %s =\n" % (x, y)
        petla()
        tekstbox.insert(END, t)
        return (mnozenie(x, y))


def odejmowanie(x, y):
    if x.m != y.m:
        if nwd(x.l, x.m) > 1:
            tekstbox.insert(END, "\n\nSkróć pierwszy ułamek\n\n")
            petla()
            x = Ulamek.skrocUlamek(x)
            t = "... = %s - %s =" % (x, y)
            tekstbox.insert(END, t)
        if nwd(y.l, y.m) > 1:
            tekstbox.insert(END, "\n\nSkróć drugi ułamek\n\n")
            petla()
            y = Ulamek.skrocUlamek(y)
            t = "... = %s - %s =" % (x, y)
            tekstbox.insert(END, t)
        if x.l >= x.m:
            tekstbox.insert(END, "\n\nWyłącz całości z pierwszego ułamka\n\n")
            x = Ulamek.wylaczCalosc(x)
            petla()
            t = "... = %s - %s =" % (x, y)
            tekstbox.insert(END, t)
        if y.l >= y.m:
            tekstbox.insert(END, "\n\nWyłącz całości z drugiego ułamka\n\n")
            y = Ulamek.wylaczCalosc(y)
            petla()
            t = "... = %s - %s =" % (x, y)
            tekstbox.insert(END, t)

    if x.l == 0 and y.l == 0:
        tekstbox.insert(END, "\n\nWykonaj odejmowanie na liczbach całkowitych\n")
        petla()
        wynik = Ulamek((x.c - y.c), 0, 1)
        t = "\n... = %s\n" % wynik
        tekstbox.insert(END, t)
        return wynik

    # przypadek o różnych mianownikach
    x1 = Ulamek(x.c, x.l, x.m)
    y1 = Ulamek(y.c, y.l, y.m)
    x1.l = x1.m * x1.c + x1.l
    y1.l = y1.m * y1.c + y1.l
    x1.c = 0
    y1.c = 0
    k = nww(x1.m, y1.m)
    x1.l = k // x1.m * x1.l
    y1.l = k // y1.m * y1.l
    x1 = Ulamek(0, x1.l, k)
    y1 = Ulamek(0, y1.l, k)
    if x.l == 0 or y.l == 0:
        if x1.l < y1.l:
            tekstbox.insert(END,
                            "\n\nPonieważ druga liczba jest większa niż pierwsza,\ndlatego wynik będzie ujemny i od drugiej liczby trzeba odjąć pierwszą")
            petla()
            x, y = y, x
            t = "\n\n... = - (%s - %s) =\n\n" % (x, y)
            tekstbox.insert(END, t)

            if x.l != 0:
                tekstbox.insert(END,
                                "\nOdejmij teraz od pierwszej liczby całkowitej drugą i dopisz ułamek po wyniku odejmowania. Pamiętaj o ujemnym wyniku.")
                wynik = Ulamek(x.c - y.c, x.l, x.m)
                petla()
                t = "\n\n... = - %s" % wynik
                tekstbox.insert(END, t)
                return wynik
            if y.l != 0:
                tekstbox.insert(END,
                                "Zamień jedną całość z pierwszej liczby na ułamek o takim samym mianowniku jaki jest\nw drugim ułamku, czyli 1 = ")
                t = " %s/%s." % (y.m, y.m)
                tekstbox.insert(END, t)
                x = Ulamek(x.c - 1, y.m, y.m)
                tekstbox.insert(END, " Teraz możesz zapisać pierwszy ułamek jako:  ")
                petla()
                t = "%s \nZatem teraz masz tak:\n\n" % x
                tekstbox.insert(END, t)
                t = "... = - (%s - %s) =" % (x, y)
                tekstbox.insert(END, t)
                tekstbox.insert(END, "\n\nMozesz odjąć: najpierw całości, potem ułamki. Nie zapomnij o minusie.\n")
                petla()
                wynik = Ulamek(x.c - y.c, x.l - y.l, y.m)
                t = "\n... = - %s" % wynik
                tekstbox.insert(END, t)
                return (wynik)
        if x1.l == y1.l:
            tekstbox.insert(END, "\n Chyba wiesz jaki jest wynik ;\)")
            petla()
            wynik = Ulamek(0, 0, 1)
            t = "... = %s" % wynik
            tekstbox.insert(END, t)
            return wynik
        else:
            if x.l != 0:
                tekstbox.insert(END,
                                "\nOdejmij teraz od pierwszej liczby całkowitej drugą i dopisz ułamek po wyniku odejmowania.\n")
                wynik = Ulamek(x.c - y.c, x.l, x.m)
                petla()
                t = "\n... = %s" % wynik
                tekstbox.insert(END, t)
                return wynik
            if y.l != 0:
                tekstbox.insert(END,
                                "\nZamień jedną całość z pierwszej liczby na ułamek o takim samym mianowniku jak jest\nw drugim ułamku,czyli 1 = ")
                t = "%s/%s" % (y.m, y.m)
                x = Ulamek(x.c - 1, x.l + x.m, x.m)
                t = "Czyli teraz możesz zapisać pierwszy ułamek jako %s Zatem masz teraz tak:" % x
                tekstbox.insert(END, t)
                t = "\n\n... = %s - %s =" % (x, y)
                tekstbox.insert(END, t)
                t = "\n\nTeraz mozesz odjąć: najpierw całości, potem ułamki."
                tekstbox.insert(END, t)
                petla()
                wynik = Ulamek(x.c - y.c, x.l - y.l, y.m)
                t = "\n ... = %s" % wynik
                tekstbox.insert(END, t)
                return (wynik)
    elif x.m != y.m:  # przypadek gdy obie liczby mają liczniki różne od 0
        tekstbox.insert(END, "\n\nSprowadź ułamki do wspólnego mianownika\n")
        k = nww(x.m, y.m)
        x = Ulamek(x.c, k // x.m * x.l, k)
        y = Ulamek(y.c, k // y.m * y.l, k)
        petla()
        t = "\n ... = %s - %s = " % (x, y)
        tekstbox.insert(END, t)

    if x1.l < y1.l:
        tekstbox.insert(END,
                        "\n\nPonieważ druga liczba jest większa niż pierwsza,\ndlatego wynik będzie ujemny i od drugiej liczby trzeba odjąć pierwszą\n")
        petla()
        x, y = y, x
        t = "\n ... = - (%s - %s) =" % (x, y)
        tekstbox.insert(END, t)

        if x.l < y.l:
            tekstbox.insert(END, "\n\nZamień jedną całość z pierwszej liczby na ułamek o liczniku i mianowniku ")
            t = "równym %s, \nczyli 1 = %s / %s. " % (x.m, y.m, y.m)
            tekstbox.insert(END, t)
            x = Ulamek(x.c - 1, x.l + y.m, y.m)
            petla()
            t = "Teraz możesz zapisać pierwszy ułamek jako %s. \nZatem masz teraz tak:" % x
            tekstbox.insert(END, t)
            t = "\n\n... = - (%s - %s) =" % (x, y)
            tekstbox.insert(END, t)
        t = "\n\nWykonaj odejmowanie: najpierw całości, potem ułamki. Nie zapomnij o minusie.\n"
        tekstbox.insert(END, t)
        petla()
        wynik = Ulamek(x.c - y.c, x.l - y.l, y.m)
        t = "\n... = - %s" % wynik
        tekstbox.insert(END, t)
        wynik = Ulamek.czy_da_skr(wynik, znak="-")
        wynik = Ulamek.czy_da_wyl(wynik, znak="-")
        return (wynik)

    if x1.l == y1.l:
        tekstbox.insert(END, "\nChyba wiesz jaki jest wynik ;\)")
        petla()
        wynik = Ulamek(0, 0, 1)
        t = "... = %s" % wynik
        tekstbox.insert(END, t)
        return wynik
    else:
        if x.l < y.l:
            tekstbox.insert(END, "\n\nZamień jedną całość z pierwszej liczby na ułamek o mianowniku ")
            t = "%s , czyli 1 = %s/%s" % (y.m, y.m, y.m)
            tekstbox.insert(END, t)
            x = Ulamek(x.c - 1, x.l + x.m, x.m)
            petla()
            t = "\nTeraz możesz zapisać pierwszy ułamek jako %s \nZatem masz teraz tak:\n" % x
            tekstbox.insert(END, t)
            t = "\n... = %s - %s = " % (x, y)
            tekstbox.insert(END, t)
        t = "\n\nWykonaj odejmowanie: najpierw odejmij całości, potem ułamki.\n"
        tekstbox.insert(END, t)
        petla()
        wynik = Ulamek(x.c - y.c, x.l - y.l, y.m)
        t = "\n... = %s" % wynik
        tekstbox.insert(END, t)
        return (wynik)


def sprawdz():
    kto = rb_kto.get()
    jakie = rb_jakie.get()
    if jakie == "S" and kto == "K":
        var1c = str(random.randint(1, 10))
        ulamek_1c.insert(0, var1c)
        var1m = str(random.randint(2, 10))
        ulamek_1m.insert(0, var1m)
        var1l = str(random.randint(1, int(var1m) - 1))
        ulamek_1l.insert(0, var1l)
        var2c = str(random.randint(1, 10))
        ulamek_2c.insert(0, var2c)
        var2m = str(random.randint(2, 10))
        ulamek_2m.insert(0, var2m)
        var2l = str(random.randint(1, int(var2m) - 1))
        ulamek_2l.insert(0, var2l)

    if jakie == "D" and kto == "K":
        var1c = str(random.randint(1, 20))
        ulamek_1c.insert(0, var1c)
        var1m = str(random.randint(2, 20))
        ulamek_1m.insert(0, var1m)
        var1l = str(random.randint(1, int(var1m) - 1))
        ulamek_1l.insert(0, var1l)
        var2c = str(random.randint(1, 20))
        ulamek_2c.insert(0, var2c)
        var2m = str(random.randint(2, 20))
        ulamek_2m.insert(0, var2m)
        var2l = str(random.randint(1, int(var2m) - 1))
        ulamek_2l.insert(0, var2l)

    if kto == "H":
        var1c = ulamek_1c.get()
        var1l = ulamek_1l.get()
        var1m = ulamek_1m.get()
        var2c = ulamek_2c.get()
        var2l = ulamek_2l.get()
        var2m = ulamek_2m.get()

    c1 = ""
    if var1c != "":
        for c in var1c:
            c1 += c
            if c not in CYFRY:
                # ulamek_1c.delete(0, len(var1c))
                tekst.set("Niepoprawny znak w całościach pierwszego ułamka")
                return False
    else:
        c1 = "0"

    l1 = ""
    if var1l != "":
        for c in var1l:
            l1 += c
            if c not in CYFRY:
                # ulamek_1l.delete(0, len(var1l))
                tekst.set("Niepoprawny znak w liczniku pierwszego ułamka")
                return False
    else:
        l1 = "0"

    if var1m != "":
        m1 = ""
        for c in var1m:
            m1 += c
            if c not in CYFRY:
                # ulamek_1m.delete(0, len(var1m))
                tekst.set("Niepoprawny znak w mianowniku pierwszego ułamka")
                return False
    elif l1 != "0" and (var1m == "" or int(var1m) == 0):
        tekst.set("Mianownik pierwszego ułamka nie może być równy 0")
        m1 = "1"
    else:
        m1 = "1"

    if var2c != "":
        c2 = ""
        for c in var2c:
            c2 += c
            if c not in CYFRY:
                # ulamek_2c.delete(0, len(var2c))
                tekst.set("Niepoprawny znak w całościach drugiego ułamka")
                return False
    else:
        c2 = "0"

    if var2l != "":
        l2 = ""
        for c in var2l:
            l2 += c
            if c not in CYFRY:
                # ulamek_2l.delete(0, len(var2l))
                tekst.set("Niepoprawny znak w liczniku drugiego ułamka")
                return False
    else:
        l2 = "0"

    if var2m != "":
        m2 = ""
        for c in var2m:
            m2 += c
            if c not in CYFRY:
                # ulamek_2m.delete(0, len(var2m))
                tekst.set("Niepoprawny znak w mianowniku drugiego ułamka")
                return False
    elif l2 != "0" and (var2m == "" or int(var2m) == 0):
        tekst.set("Mianownik drugiego ułamka nie może być równy 0")
        m2 = "1"
    else:
        m2 = "1"

    tekst.set("")

    cu1 = int(c1)
    lu1 = int(l1)
    mu1 = int(m1)
    cu2 = int(c2)
    lu2 = int(l2)
    mu2 = int(m2)

    x = Ulamek(cu1, lu1, mu1)
    y = Ulamek(cu2, lu2, mu2)

    vr = rb_var.get()
    tekstbox.delete(0.0, END)

    if vr == "+":
        t = "%s + %s =..." % (x, y)
        tekstbox.insert(END, t)
        wynik = dodawanie(x, y)
        podajwynik(wynik)
    elif vr == "*":
        t = "%s * %s =..." % (x, y)
        tekstbox.insert(END, t)
        wynik = mnozenie(x, y)
        podajwynik(wynik)
    elif vr == ":":
        t = "%s : %s =..." % (x, y)
        tekstbox.insert(END, t)
        if y.c == 0 and y.l == 0:
            tekstbox.insert(END, "\n\nDzielenie przez 0 jest niedozwolne!!!")
        else:
            wynik = dzielenie(x, y)
            podajwynik(wynik)
    elif vr == "-":
        t = "%s - %s = ..." % (x, y)
        tekstbox.insert(END, t)
        wynik = odejmowanie(x, y)
        t = "\n\n           GOTOWE !!!\n"
        tekstbox.insert(END, t)
    m = messagebox.showinfo("KONIEC", "PRZYKŁAD ZOSTAŁ WYLICZONY")
    ulamek_1c.delete(0, END)
    ulamek_1l.delete(0, END)
    ulamek_1m.delete(0, END)
    ulamek_2c.delete(0, END)
    ulamek_2l.delete(0, END)
    ulamek_2m.delete(0, END)


def dodajkontrolki():
    rb_latwe = Radiobutton(window, variable=rb_jakie, value="S", text="ŁATWE (mianownik <= 10)",
                           font=("Arial", 12, "bold"))
    rb_trudne = Radiobutton(window, variable=rb_jakie, value="D", text="TRUDNE (mianownik <= 20)",
                            font=("Arial", 12, "bold"))
    rb_jakie.set("S")  # ustawiam zaznaczenie na kontrolkę dla opcji TY

    rb_latwe.pack()
    rb_latwe.place(x=630, y=100)
    rb_trudne.pack()
    rb_trudne.place(x=630, y=120)
    kto = rb_kto.get()
    jakie = rb_jakie.get()

    if kto == "H":
        rb_jakie.set("1")
        return


CYFRY = "0123456789"

window = Tk()
# szerokosc = window.winfo_screenwidth()
# wysokosc = window.winfo_screenheight()
window.title("Nauka działań na ułamkach zwykłych")
# wymiary = str(int(0.9 * szerokosc)) + "x" + str(int(0.9 * wysokosc))
window.geometry("900x750")
global rb_jakie
var1c = StringVar()
var1l = StringVar()
var1m = StringVar()
var2c = StringVar()
var2l = StringVar()
var2m = StringVar()
tekst = StringVar()
tekst1 = StringVar()
rb_jakie = StringVar()

canvas = Canvas(window, width=180, heigh=3)
canvas.pack()
canvas.place(x=90, y=109)
line_id = canvas.create_line((6, 2, 37, 2), fill="black", width=3)
line_id1 = canvas.create_line((137, 2, 168, 2), fill="black", width=3)

instrukcja1 = Label(window, text="Wprowadź dwa ułamki zwykłe i wybierz działanie do wykonania",
                    font=("Arial", 14, "bold"))
instrukcja1.pack()
instrukcja2 = Label(window, font=("Arial", 14), textvariable=tekst, fg="RED")
tekst.set("")
instrukcja2.pack()
instrukcja2.place(x=10, y=160)

instrukcja3 = Label(window, font=("Arial", 12), text="ułamek 1", fg="GREEN")
instrukcja3.pack()
instrukcja3.place(x=50, y=50)
instrukcja4 = Label(window, font=("Arial", 12), text="ułamek 2", fg="GREEN")
instrukcja4.pack()
instrukcja4.place(x=185, y=50)

ulamek_1c = Entry(window, bg="#009688", font=("Arial", 18, "bold"), width=3, validatecommand=sprawdz,
                  textvariable=var1c, justify=RIGHT)
ulamek_1c.pack()
ulamek_1c.place(x=50, y=100)
ulamek_1l = Entry(window, bg="#009688", font=("Arial", 14, "bold"), width=2, justify=LEFT)
ulamek_1l.pack()
ulamek_1l.place(x=100, y=84)
ulamek_1m = Entry(window, bg="#009688", font=("Arial", 14, "bold"), width=2, justify=LEFT)
ulamek_1m.pack()
ulamek_1m.place(x=100, y=116)
ulamek_2c = Entry(window, bg="#009688", font=("Arial", 18, "bold"), width=3, validatecommand=sprawdz,
                  textvariable=var2c, justify=RIGHT)
ulamek_2c.pack()
ulamek_2c.place(x=180, y=100)
ulamek_2l = Entry(window, bg="#009688", font=("Arial", 14, "bold"), width=2, justify=LEFT)
ulamek_2l.pack()
ulamek_2l.place(x=230, y=84)
ulamek_2m = Entry(window, bg="#009688", font=("Arial", 14, "bold"), width=2, justify=LEFT)
ulamek_2m.pack()
ulamek_2m.place(x=230, y=116)

dalej = Button(window, font=("Arial", 16, "bold"), text=" = DALEJ ", command=sprawdz, borderwidth=3)
dalej.pack()
dalej.place(x=260, y=93)

rb_var = StringVar()  # zmienna sterująca zaznaczeniem kontrolki
rb_plus = Radiobutton(window, variable=rb_var, value="+", text=" + dodawanie", font=("Arial", 12, "bold"))
rb_minus = Radiobutton(window, variable=rb_var, value="-", text=" - odejmowanie", font=("Arial", 12, "bold"))
rb_razy = Radiobutton(window, variable=rb_var, value="*", text=" * mnożenie", font=("Arial", 12, "bold"))
rb_dziel = Radiobutton(window, variable=rb_var, value=":", text=" : dzielenie", font=("Arial", 12, "bold"))

rb_var.set("+")  # ustawiam zaznaczenie na kontrolkę dla opcji +
rb_plus.pack()
rb_plus.place(x=400, y=50)
rb_minus.pack()
rb_minus.place(x=400, y=80)
rb_razy.pack()
rb_razy.place(x=400, y=110)
rb_dziel.pack()
rb_dziel.place(x=400, y=140)

rb_kto = StringVar()  # zmienna sterująca zaznaczeniem kontrolki
rb_ty = Radiobutton(window, variable=rb_kto, command=dodajkontrolki, value="H", text="- Ty podajesz liczby ",
                    font=("Arial", 12, "bold"))
rb_komp = Radiobutton(window, variable=rb_kto, command=dodajkontrolki, value="K", text="- Komputer podaje liczby",
                      font=("Arial", 12, "bold"))
rb_kto.set("H")  # ustawiam zaznaczenie na kontrolkę dla opcji TY
rb_ty.pack()
rb_ty.place(x=600, y=45)
rb_komp.pack()
rb_komp.place(x=600, y=75)


znakdz = Entry(window, bg="#009688", font=("Arial", 16, "bold"), width=2, justify=CENTER, text=rb_var)
znakdz.pack()
znakdz.place(x=137, y=99)
sb_textbox = Scrollbar(window)
tekstbox = Text(window, font=("Arial", 13, "bold"), height=30, width=96, yscrollcommand=sb_textbox.set)
sb_textbox.place(in_=tekstbox, relx=1., rely=0, relheight=1.)
tekstbox.pack()
tekstbox.place(x=10, y=190)
tekstbox.insert(END, "Gdy wypełnisz wszystkie pola naciśnij DALEJ")
sb_textbox.config(command=tekstbox.yview)


ulamek_1c.focus_set()

window.mainloop()
