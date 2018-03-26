from tkinter import *

class Ulamek:
    def __init__(self, c, l, m):
        self.c = c
        self.l = l
        self.m = m

    def __str__(self):
        if self.l == 0:
            return '%s' % self.c
        elif self.c == 0:
            return '%s/%s' % (self.l, self.m)
        else:
            return '%s %s/%s' % (self.c, self.l, self.m)

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
    if a== 0 and b == 0:
        return 1
    if a == 0 or b == 0:
        return max(a, b)
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


def uproscrownanie(r, g):
    rL, rP = r.split("=")
    x = 0
    y = 0
    warL_dla_00 = eval(rL, locals()) * g
    warP_dla_00 = eval(rP, locals()) * g
    rC = (warP_dla_00 - warL_dla_00) * g

    x = 0
    y = 1
    warL_dla_01 = eval(rL, locals()) * g
    warP_dla_01 = eval(rP, locals()) * g
    rB = (warL_dla_01 - warL_dla_00 - (warP_dla_01 - warP_dla_00)) * g

    x = 1
    y = 0
    warL_dla_10 = eval(rL, locals()) * g
    warP_dla_10 = eval(rP, locals()) * g
    rA = (warL_dla_10 - warL_dla_00 - (warP_dla_10 - warP_dla_00)) * g

    rA = int(rA)
    rB = int(rB)
    rC = int(rC)

    dz = nwd(nwd(abs(rA), abs(rB)), abs(rC))

    return (rA // dz, rB // dz, rC // dz)


def popraw(r):

    if r == "":
        tekstbox.insert(END, "WPROWADŹ 2 RÓWNANIA\n")
        tekstbox.see("end")
        return 0

    l = ""
    for i in range(len(r)):  # USUWANIE SPACJI
        if r[i] != " ":
            l += r[i]

    m = ""
    for i in range(len(l)):  # USUWANIE nawiasów kwadratowych [] ---> ()
        if l[i] == "[":
            m += "("
        elif l[i] == "]":
            m += ")"
        elif l[i] == ",":
            m += "."
        else:
            m += l[i]

    if not "=" in m:
        tekstbox.insert(END, "NIEPOPRAWNE RÓWNANIE - brak znaku '='\n")
        tekstbox.see("end")
        return 0

    for znak in m:
        if not znak in "0123456789*/+-()xy=.,":
            tekstbox.insert(END, "NIEPOPRAWNE RÓWNANIE - nie używaj innych znaków niż: x, y, cyfr 0-9, znaków działań i nawiasów\n")
            tekstbox.see("end")
            return 0

    if m[0] in ".),*/" or m[-1] in ".,*+-(=/":
        tekstbox.insert(END, "NIEPOPRAWNY ZNAK NA POCZĄTKU LUB KONCU RÓWNANIA\n")
        tekstbox.see("end")
        return 0

    for i in range(len(m)-1):
        if m[i] == "/" and (m[i+1] == "x" or m[i+1] == "y"):
            tekstbox.insert(END, "NIEPOPRAWNE RÓWNANIE - niewiadoma nie może być w mianowniku\n")
            tekstbox.see("end")
            return 0

    for i in range(len(m)-2):
        if m[i] == "/" and m[i+1] == "(":
            ko = i+2
            while m[ko] != ")":
                if m[ko] == "x" or m[ko] == "y":
                    tekstbox.insert(END, "NIEPOPRAWNE RÓWNANIE - niewiadoma nie może być w mianowniku\n")
                    tekstbox.see("end")
                    return 0
                ko += 1

    NIEDOBRE = ("()", "-)", "+)", "/)", "*)", "**", "//", "*+", "+*", "-*", "*-", "-/", "/-", "*-", "-*", "+/", "/+",
                "/*", "*/", "..", "./", "/.", ".+", "+.", ".-", "-.", ".*", "*.", "x.", "y.", ".x", ".y", "(.", ".(",
                ").", ".)", "=.", ".=", "(=", "=)")

    for zz in NIEDOBRE:
        if m.find(zz, 0, len(m)) != -1:
            tekstbox.insert(END, "NIEPOPRAWNE RÓWNANIE - niepoprawne użycie działań\n")
            tekstbox.see("end")
            return 0


    ot = []
    za = []
    row = []
    for i in range(len(m)):
        if m[i] == "(":
            ot.append(i)
        if m[i] == ")":
            za.append(i)
        if m[i] == "=":
            row.append(i)
    if len(row) != 1:
        tekstbox.insert(END, "W równaniu musi być dokładnie jeden znak '='\n")
        tekstbox.see("end")
        return 0
    if len(ot) != len(za):
        tekstbox.insert(END, "Nie zgadza się liczba nawiasów otwierających i zamykających\n")
        tekstbox.see("end")
        return 0
    if len(ot) == len(za) and len(ot) > 0:
        if ot[0] > za[0] or ot[len(ot)-1] > za[len(za)-1]:
            tekstbox.insert(END, "Niepoprawne użycie nawiasów\n")
            tekstbox.see("end")
            return 0




    k = ""
    o = m[-1]
    for i in range(len(m) - 1):  # WSTAWIANIE znaku mnozenia *
        if m[i] in "0123456789xy" and m[i + 1] in "xy(":
            k = k + m[i] + "*"
        else:
            k += m[i]
    k = k + o

    # Zamiana ulamkow z przecinkiem na ulamki zwykle:
    m = ""
    i = 0
    while i < len(k):

        if k[i] == "." and (not k[i-1] in "0123456789" or not k[i+1] in "0123456789"):
            tekstbox.insert(END, "Niepoprawnie zapisany ułamek dziesiętny\n")
            tekstbox.see("end")
            return 0
        elif k[i] == ".":
            j = i+1
            d = "/1"
            while j < len(k) and k[j] in "0123456789":
                m += k[j]
                d += "0"
                if j+1 < len(k) and k[j+1] == ".":
                    tekstbox.insert(END, "Podwójnie użyty przecinek w ułamku dziesiętnym\n")
                    tekstbox.see("end")
                    return 0
                j = j+1
            m += d
            i = j
        else:
            m += k[i]
            i += 1

    k = ""
    l = ""
    for i in range(len(m)):                 # usuwanie zer na początku liczb
        if not m[i] in "0123456789":
            if l != "":
                k = k + str(int(l)) + m[i]
                l = ""
            else:
                k += m[i]
        else:
            l += m[i]
    if l != "":
        k += l

    # Sprawdzam czy są wielokrotne dzielenia (Ulamki piętrowe


    for i in range (len(k)):
        if k[i] == "/":
            j = i+1
            c = 1
            while c == 1 and j < len(k)-1:
                if k[j] in "0123456789" and k[j+1] == "/":
                    tekstbox.insert(END, "Równanie zawiera ułamki piętrowe. Popraw, by ich nie było.\n")
                    tekstbox.see("end")
                    return 0
                elif k[j] in "0123456789" and k[j+1] in "+-=xy*":
                    c = 0
                else:
                    j += 1


    k = spr_inne_bledy(k)
    return k


def spr_inne_bledy(r):
    x = 0
    y = 0
    rL, rP = r.split("=")

    try:
        c1 = eval(rL, locals())
        d1 = eval(rP, locals())
    except:
        tekstbox.insert(END, "Błędnie podane równanie\n")
        tekstbox.see("end")
        return 0

    x = 1
    y = 1
    try:
        c2 = eval(rL, locals())
        d2 = eval(rP, locals())
    except:
        tekstbox.insert(END, "Błędnie podane równanie\n")
        tekstbox.see("end")
        return 0

    x = 2
    y = 2
    try:
        c3 = eval(rL, locals())
        d3 = eval(rP, locals())
    except:
        tekstbox.insert(END, "Błędnie podane równanie\n")
        tekstbox.see("end")
        return 0

    if round((c2 - c1),5) != round(c3 - c2,5) or round(d2 - d1,5) != round(d3 - d2,5):
        tekstbox.insert(END, "\nPodane równanie nie jest liniowe (I-ego stopnia z 2-ma niewiadomymi)\n")
        tekstbox.see("end")
        return 0
    return r


def poszukajWspMian(r):
    liczba_dzielen = 0
    indeks = []
    for i in range(1, len(r)):
        if r[i] == "/":
            indeks.append(i)
            liczba_dzielen += 1

    if liczba_dzielen > 0:
        m1 = []

        for i in indeks:
            m = ""
            k = 1
            while int(i)+k < len(r) and r[int(i) + k] in "0123456789":
                m += r[int(i) + k]
                k += 1
            m1.append(m)

        mian = 1
        i = 0
        while i <= liczba_dzielen - 1:
            nw = nwd(mian, int(m1[i]))
            mian = mian * int(m1[i]) // nw
            i += 1
    if liczba_dzielen == 0:
        mian = 1

    return mian

def main():
    r3 = ulamek_1c.get()
    r4 = ulamek_2c.get()
    tekstbox.insert(END, "\n-------------------------------------------------------------------------------------\n")
    tekstbox.insert(END, "\n                                    ZACZYNAMY \n")
    tekstbox.insert(END, "\n-------------------------------------------------------------------------------------\n")
    tekstbox.insert(END, "Twój układ równań to:\n\n")
    tekstbox.insert(END, r3 + "\n")
    tekstbox.insert(END, r4 + "\n\n")
    tekstbox.see("end")
    r5 = popraw(r3)
    if r5 == 0:
        return 0
    r6 = popraw(r4)
    if r6 == 0:
        return 0
    g = poszukajWspMian(r5)
    h = poszukajWspMian(r6)


    r1A, r1B, r1C = uproscrownanie(r5, g)
    r2A, r2B, r2C = uproscrownanie(r6, h)
    znak_r1B = "+"
    znak_r2B = "+"
    if r1B < 0:
        znak_r1B = ""
    if r2B < 0:
        znak_r2B = ""
    tekstbox.insert(END, "który po uporządkowaniu wygląda tak:\n\n")
    t = "  %sx %s %sy = %s\n" % (r1A, znak_r1B, r1B, r1C)
    tekstbox.insert(END, t)
    t = "  %sx %s %sy = %s\n" % (r2A, znak_r2B, r2B, r2C)
    tekstbox.insert(END, t)
    W = r1A * r2B - r1B * r2A
    Wx = r1C * r2B - r2C * r1B
    Wy = r1A * r2C - r1C * r2A

    t = "\nROZWIĄZANIEM UKLADU JEST:\n"
    tekstbox.insert(END, t)

    if W == 0 and Wy == 0 and Wx == 0:
        tekstbox.insert(END, "\n       UKŁAD NIEOZNACZONY\n   czyli spełnia go nieskończenie wiele par liczb (x, y)\n")
        tekstbox.see("end")
    elif W == 0 and (Wx != 0 or Wy != 0):
        tekstbox.insert(END, "\n       UKŁAD SPRZECZNY\n   czyli nie spełnia go żadna para liczb (x, y)\n")
        tekstbox.see("end")
    else:
        znak_x = ""
        znak_y = ""
        if Wx / W < 0:
            znak_x = " -"
        if Wy / W < 0:
            znak_y = " -"
        Wx = abs(Wx)
        Wy = abs(Wy)
        W = abs(W)
        #print("W  = ", W)
        #print("Wx = ", Wx)
        #print("Wy = ", Wy)
        x = Ulamek(0, Wx, W)
        y = Ulamek(0, Wy, W)
        x = Ulamek.wylaczCalosc(Ulamek.skrocUlamek(x))
        y = Ulamek.wylaczCalosc(Ulamek.skrocUlamek(y))

        t = "\n          UKLAD OZNACZONY\n  spełnia go para liczb: x =%s %s,  y =%s %s" % (znak_x, x, znak_y, y)
        tekstbox.insert(END, t)
        tekstbox.see("end")
        


global r1, r2, r1A, r1B, r1C

window = Tk()

tekst = StringVar()
r1 = StringVar()
r2 = StringVar()
# szerokosc = window.winfo_screenwidth()
# wysokosc = window.winfo_screenheight()
window.title("ROZWIĄZYWANIE UKŁADÓW RÓWNAŃ")
# wymiary = str(int(0.9 * szerokosc)) + "x" + str(int(0.9 * wysokosc))
window.geometry("900x700")



instrukcja1 = Label(window, text="Wprowadź dwa równania tworzące układ równań",
                    font=("Arial", 14, "bold"))
instrukcja1.pack()
instrukcja2 = Label(window, font=("Arial", 14), textvariable = tekst, fg="RED")
tekst.set("Gdy wprowadzisz równania naciśnij ROZWIĄŻ  ----> ")
instrukcja2.pack()
instrukcja2.place(x=10, y=200)

instrukcja3 = Label(window, font=("Arial", 12), text="równanie 1", fg="GREEN")
instrukcja3.pack()
instrukcja3.place(x=50, y=70)
ulamek_1c = Entry(window, bg="#009688", font=("Arial", 18, "bold"), width=60, validatecommand = main,
                  textvariable = r1, justify = LEFT)
ulamek_1c.pack()
ulamek_1c.place(x=50, y=90)


instrukcja4 = Label(window, font=("Arial", 12), text="równanie 2", fg="GREEN")
instrukcja4.pack()
instrukcja4.place(x=50, y=130)
ulamek_2c = Entry(window, bg="#009688", font=("Arial", 18, "bold"), width=60, validatecommand = main,
                  textvariable = r2, justify = LEFT)
ulamek_2c.pack()
ulamek_2c.place(x=50, y=150)


dalej = Button(window, font=("Arial", 16, "bold"), text=" ROZWIĄŻ ", command = main, borderwidth=3)
dalej.pack()
dalej.place(x = 470, y = 190)



sb_textbox = Scrollbar(window)
tekstbox = Text(window, font=("Arial", 13, "bold"), height=20, width=96, yscrollcommand=sb_textbox.set)
sb_textbox.place(in_=tekstbox, relx=1., rely=0, relheight=1.)
tekstbox.pack()
tekstbox.place(x=10, y=250)
tekstbox.insert(END, "KOMUNIKATY:")
sb_textbox.config(command = tekstbox.yview)

ulamek_1c.focus_set()

window.mainloop()
