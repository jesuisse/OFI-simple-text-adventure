"""
Textabenteuer für den Unterricht (c) 2024 Pascal Schuppli 

Der Programmcode verzichtet aus didaktischen Gründen vollständig auf die
Verwendung von komplexen Datenstrukturen. Ziel ist das Nachvollziehen des
Programmflusses durch Funktionsaufrufe und if-elif-else-Kontrollstrukturen.
"""

ANLEITUNG_TEXT = """
Die Suche nach dem verlorenen Schatz
=====================================

Hallo Abenteurer*in! Erkunde die Welt, indem du 'gehe nach westen', 'osten' usw
eintippst. Du kannst auch Dinge anschauen, nehmen, Türen und Truhen öffnen usw.
Viel Erfolg bei der Suche nach dem Schatz deiner Vorfahren! 

Drücke Enter, um das Abenteuer zu beginnen."""

OLIVENHAIN_TEXT = """
Du stehst auf einem schmalen Weg, der sich durch einen Olivenhain schlängelt.
Die Sonne brennt auf dich nieder und Grillen zirpen rund um dich herum um die
Wette. Im Norden siehst du durch die Olivenbäume die roten Dachziegel eines
Hauses. Hinter dir im Süden führt ein steiler Weg die Klippen hinunter zur Küste.
Im Osten bietet sich dir eine fantastische Aussicht über das tiefblaue Meer."""

KLIPPENPFAD_TEXT = """
Du stehst am Rand einer Klippe. Ein steiler Pfad windet sich im Zickzack hinunter
zum Strand im Süden. Er muss in mühsehliger Handarbeit dem Fels abgetrotzt worden
sein. Im Norden liegt ein Olivenhain.""" 

STEINHAUS_TEXT = """
Vor dir steht ein altes Haus. Seine Mauern sind aus aus aufgeschichteten Steinen
gebaut und geweisselt, sein Dach mit den braunroten Ziegeln gedeckt, die typisch
sind für die Gegend. Die wenigen Fenster sind mit blauen Läden verschlossen; die
Tür sieht aus, als könnte sie einem Panzer standhalten.

Im Süden liegt ein Olivenhain. Im Westen hat jemand einen kleinen Garten angelegt."""

IMHAUS_TEXT = """
Im Haus ist es schummrig. Es riecht nach Zedernholz und Thymian, der draussen in den
Mauerritzen ein neues zuhause gefunden hat. Das Haus ist leer bis auf eine grosse alte
Truhe aus Holz mit Eisenbeschlägen."""

GARTEN_TEXT="""
Der Garten benötigt dringend Hilfe von jemandem mit einem grünen Daumen. Überall
wuchern Pflanzen; dir ist nicht klar, was Unkraut ist und was nicht. Mitten im
Garten wachsen riesige Bohnenstauden, so hoch, wie du sie noch nie gesehen hast.
Dahinter gab es wohl einmal Kartoffeln, aber das muss schon lange her sein. Und
sind das Tomaten dort hinten neben dem halb umgefallenen Holzschild?"""

STRAND_TEXT="""
Du stehst in auf dem Sandstrand einer kleinen Bucht. Die Wellen donnern gegen die
Felsen, schwimmen will hier keiner, der bei Verstand ist. Rundherum ragen steile
Klippen in den Himmel. Im Norden liegt der verschüttete Pfad nach oben."""

SCHUTTKEGEL_TEXT = """
Der Klippenpfad ist auf halber Höhe abgebrochen; tonnenweise Geröll ist hier auf
den Strand gestürzt. Hier kommst du auf jeden Fall nicht mehr wieder zurück nach
oben. Immerhin: Neben dem Geröll ist auch eine ansehliche Menge weiche Erde auf
den Strand gestürzt. Wenn du hier unten stirbst, besteht die Chance, dass irgendwann
Gras über die Sache wächst..."""

STEINSCHLAG_TEXT = """
Während du auf dem Pfad nach unten steigst, hörst du ein beunruhigendes Grollen.
Plötzlich bricht ein riesiger Felsbrocken hinter dir aus der Felswand und stürzt
tosend in die Tiefe! Er schlägt weitere Felsbrocken aus der Wand, und ein gewaltiger
Steinschlag reisst den Pfad hinter dir in die Tiefe. Mit zitternden Knien steigst du
die letzten paar Dutzend Meter nach unten und stehst schliesslich schwer atmend auf
dem weichen Sand der Bucht."""

spieler_hat_spaten = False
spieler_hat_brecheisen = False
spieler_hat_bohne = False
spieler_hat_tomate = False
spieler_hat_schlüssel = False
bohne_ist_gewachsen = False
tür_ist_offen = False
truhe_ist_offen = False
erstes_mal_truhe_öffnen=True
steinschlag=False


def finde_richtung(eingabe):
    if eingabe == "n" or "norden" in eingabe:
        return "n"
    elif eingabe == "w" or "westen" in eingabe:
        return "w"
    elif eingabe == "s" or "süden" in eingabe:
        return "s"
    elif eingabe == "o" or "osten" in eingabe:
        return "o"
    elif "hinein" in eingabe or "herein" in eingabe:
        return "hinein"
    elif "heraus" in eingabe or "hinaus" in eingabe:
        return "hinaus"
    else:
        return ""

def beschreibung(raum):
    if raum == "Olivenhain":
        return OLIVENHAIN_TEXT
    elif raum == "Klippenpfad":
        return KLIPPENPFAD_TEXT
    elif raum == "Steinhaus":
        return STEINHAUS_TEXT
    elif raum == "Im Steinhaus":
        return IMHAUS_TEXT
    elif raum == "Garten":
        return GARTEN_TEXT
    elif raum == "Steinschlag":
        return STEINSCHLAG_TEXT
    elif raum == "Schuttkegel":
        return SCHUTTKEGEL_TEXT
    elif raum == "Strand":
        return STRAND_TEXT
    return "Du stehst mitten in einer Ansammlung nicht erwähnenswerter Szenerie."


def objekte_in_raum(raum):
    if raum == "Steinhaus":
        if not spieler_hat_schlüssel:
            return "Ein rostiger Schlüssel hängt an einem Nagel über dem Türbalken."
    if raum == "Garten":
        if not spieler_hat_spaten:
            return "Ein alter Holzspaten liegt achtlos weggeworfen neben den Tomaten."
    if raum == "Strand":
        if not spieler_hat_brecheisen:
            return "Seltsam. Eine verrostete Brechstange liegt halb vergraben im Sand."
    if raum == "Klippenpfad":
        if steinschlag:
            return "Der Pfad ist in der Mitte der Klippe abgebrochen und unpassierbar."
    
    return ""

def finde_raum_in_richtung(raum, richtung):
    global steinschlag
    if raum == "Olivenhain":
        if richtung == "n":
            return "Steinhaus"
        elif richtung == "s":
            return "Klippenpfad"
    elif raum == "Steinhaus":
        if richtung == "s":
            return "Olivenhain"
        elif (richtung == "n" or richtung=="hinein") and tür_ist_offen:
            return "Im Steinhaus"
        elif richtung == "w":
            return "Garten"
    elif raum == "Im Steinhaus":
        if richtung == "s" or richtung == "hinaus":
            return "Steinhaus"
    elif raum == "Klippenpfad":
        if richtung == "n":
            return "Olivenhain"
        elif richtung == "s" and not steinschlag:
            steinschlag=True
            return "Steinschlag"
    elif raum == "Garten":
        if richtung == "o":
            return "Steinhaus"
    elif raum == "Strand":
        if richtung == "w" and bohne_ist_gewachsen:
            return "Klippenpfad"
        if richtung == "n":
            return "Schuttkegel"
    elif raum == "Schuttkegel":
        if richtung == "s":
            return "Strand"
    elif raum == "Steinschlag":
        return "Strand"
    return ""  

def nimm(objekt):
    global spieler_hat_tomate, spieler_hat_bohne, spieler_hat_spaten, spieler_hat_brecheisen
    global spieler_hat_schlüssel
    if objekt == "tomate" and raum=="Garten":
        if spieler_hat_tomate:
            print("Sei nicht gierig. Eine reicht.")
        else:
            print("Du steckst die Tomate in deine Tasche.")
            spieler_hat_tomate=True
    elif objekt == "bohne" and raum=="Garten":
        if spieler_hat_bohne:
            print("Du hast schon eine.")
        else:
            print("Du nimmst eine Bohne. Klein, aber du solltest Dinge nicht nur nach ihrem Äusseren beurteilen. Kleines vermag grosses zu leisten.")
            spieler_hat_bohne=True
    elif objekt == "spaten" and raum=="Garten":
        if spieler_hat_spaten:
            print("Du hast ihn schon, okay?")
        else:
            print("Du bist jetzt stolzer Besitzer eines panzerbrechenden Holzspatens.")
            spieler_hat_spaten=True
    elif objekt == "brecheisen" and raum=="Strand":
        if spieler_hat_brecheisen:
            print("Da war nur eins. Die liegen hier nicht rum wie Sand am Meer.")
        else:
            spieler_hat_brecheisen=True
            print("Bewaffnet mit einem Brecheisen fühlst du dich, als gehöre dir die Welt.")
    elif objekt == "schlüssel" and raum=="Steinhaus":
        if spieler_hat_schlüssel:
            print("Du hängst den Schlüssel zurück an den Haken und nimmst ihn nochmal.")
            print("Du fühlst dich jetzt viel besser.")
        else:
            spieler_hat_schlüssel=True
            print("Du nimmst den Schlüssel. Wo der wohl passen könnte?")
    elif objekt == "sand" and (raum=="Strand" or raum=="Steinschlag"):
            print("Was willst du mit einer handvoll Sand anfangen? Das ist hier nicht nützlich.")
    else:
        print("Das kannst du nicht nehmen.")

def öffne(objekt):
    global tür_ist_offen, truhe_ist_offen, spieler_hat_spaten, spieler_hat_brecheisen, erstes_mal_truhe_öffnen
    if objekt == "tür":
        if raum == "Steinhaus":
            if tür_ist_offen:
                print("Jetzt ist sie noch offener als vorher.")
            elif spieler_hat_schlüssel:
                print("Der Schlüssel passt. Du öffnest die Tür.")
                tür_ist_offen=True            
            elif spieler_hat_brecheisen:
                print("Womit? Mit dem Brecheisen? Das wird nicht funktionieren. Und hat dir nie jemand gesagt, dass Gewalt keine Lösung ist?")
            elif spieler_hat_spaten:
                print("Du probierst die Tür mit dem Spaten aufzubrechen. Ohne Erfolg. Der Spaten zerbricht.")
                spieler_hat_spaten = False
            elif spieler_hat_tomate:
                print("Womit? Die Tomate wird dir jedenfalls dabei nicht helfen.")
            else:
                print("Die Tür ist verschlossen.")
        else:
            print("Kleiner Tipp: Um eine Tür zu öffnen, muss eine in der Nähe sein...")
    elif objekt == "truhe" and raum == "Im Steinhaus":
        if spieler_hat_spaten:
            print("Du versuchst es mit dem Holzspaten. Er zerbricht.")
            spieler_hat_spaten=False
            print("Vielleicht probierst du es nochmal mit einem anderen Werkzeug.")
        elif spieler_hat_brecheisen:
            print("Du versuchst es mit dem Brecheisen, aber das Brecheisen bricht.")
            print("War ja sooo klar. Weshalb sonst heisst das Ding auch Brecheisen?")
            spieler_hat_brecheisen=False
            print("Mit blossen Händen hättest du wahrscheinlich mehr Erfolg als mit einem verrosteten Brecheisen.")
        else:
            print("Wie willst du die Truhe ohne Werkzeug und ohne Schlüssel öffnen?")
            print("Etwa mit blossen Händen?")
            if erstes_mal_truhe_öffnen:
                print("Ich erkläre dir das Konzept eines Abenteuerspiels:")
                print("Du machst dich auf die Suche nach nützlichen Gegenstände und kommst")
                print("zurück, wenn du was brauchbares gefunden hast. Aber was weiss ich schon?")
                print("Ich bin ja nur ein dummer Computer, der mit dir dieses Spiel spielt.")
                erstes_mal_truhe_öffnen = False
    elif objekt == "hände" and raum=="Im Steinhaus":
        print("Du hämmerst mit deinen blossen Händen gegen die Truhe.")
        print("Es scheppert, die verrosteten Eisenbeschläge zerfallen unter deinem Ansturm und geben die True frei.")
        print("Verwundert öffnest du die Truhe.")
        truhe_ist_offen=True
    else:
        print("Das kannst du nicht öffnen.")
                    
            
def betrachte(objekt):
    global spiel_zu_ende
    
    if objekt == "tomate":
        if spieler_hat_tomate or raum=="Garten":
            print("Eine überreife Tomate, die unglaublich verlockend aussieht.")
        else:
            print("Hast du Tomaten auf den Augen? Hier sind weit und breit keine.")
    elif objekt == "bohne":
        if raum=="Garten":
            print("Die Bohnenstauden ragen in den Himmel, als möchten sie den Wolken einen Besuch abstatten. Unglaublich,")
            print("dass aus einer so kleinen Bohne etwas so gewaltiges wachsen kann.")
        elif spieler_hat_bohne:
            print("Eine kleine unscheinbare Bohne, die nur darauf wartet, ein neues Zuhause in weicher Erde zu finden.")
        else:
            print("Hier gibt es keine Bohnen.")
    elif objekt == "spaten":
        if raum=="Garten" or spieler_hat_spaten:
            print("Ein alter Spaten aus Holz, der aussieht, als könnte er es mit einem Panzer aufnehmen.")
        else:
            print("Irgendwo liegt immer ein Spaten rum. Nur wo?")
    elif objekt == "schild":
        if raum =="Garten":
            print("Kaum leserlich, aber da steht: 'Achtung, der Garten ist mit Schwermetallrückständen verseucht!'")
            print("Ob die Bohnenstauden deshalb so riesig gewachsen sind?")
    elif objekt == "schlüssel":
        if raum=="Steinhaus" or spieler_hat_schlüssel:
            print("Ein rostiger Schlüssel. Könnte zu einer Tür gehören.")
        else:
            print("Such den Schlüssel sonstwo. Hier ist keiner.")
    elif objekt == "brecheisen":
        if raum=="Strand":
            print("Ein Brecheisen mit ein, zwei Rostflecken. Wie die wohl hierher gekommen sein mag? Angeschwemmt wurde sie wohl kaum.")
        elif spieler_hat_brecheisen:
            print("Eine Brechstange aus erstklassig verrostetem Eisen.")
    elif objekt == "tür":
        if raum=="Strand":
            print("Schön wärs. Leider gibt's hier keine. Das ist kein Stephen King-Roman.")
        elif raum == "Steinhaus":
            print("Eine schwere Holztür aus Eiche, die aussieht, als könnte sie einen Panzerangriff überleben.")
    elif raum=="Im Steinhaus" and (objekt == "hinein" or objekt=="truhe"):
        if truhe_ist_offen:
            print("**************************************************************************************")
            print("Hurrah! Du hast den Schatz gefunden! Edelsteine, Perlen und dein persönlicher Favorit,")
            print("das Gebiss deiner Urgrossmutter. Liebevoll packst du es in ein Samtsäckchen, schaust")
            print("dir nochmal die vielen Klunker an und machst dich dann als Held auf nach Hause.")
            print("Niemand wird je vergessen, wie du nach jahrelanger Suche unter Lebensgefahr das")
            print("Gebiss deiner Urgrossmutter gerettet hast.")
            print("ENDE")
            print("**************************************************************************************")
            spiel_zu_ende = True
        else:                
            return print("Eine alte Holztruhe mit extrem solide aussehenden Eisenbeschlägen. Leider verschlossen.")
    elif objekt=="sand" and (raum=="Strand" or raum=="Steinschlag"):
        print("Sand eben. Der an einem Strand rumliegt. Kennst du, oder?")
    else:
        print("Ich sehe daran nichts besonderes.")

def pflanze(objekt):
    global spieler_hat_bohne, raum, spieler_hat_schlüssel
    if objekt=="bohne" and spieler_hat_bohne:
        if raum=="Garten":
            print("Hervorragende Idee. Es hatte hier ja vorher noch fast keine Bohnen.")
            spieler_hat_bohne=False
        elif raum=="Schuttkegel":
            print("Ohne grosse Hoffnung pflanzt du die Bohne in die frische Erde.")
            print("Da passiert ein Wunder. Mit grossem Tempo wächst eine riesige")
            print("Bohnenstaude die Klippen hoch. Du beginnst zu klettern und stehst")
            print("bald wieder am oberen Rand der Klippe.")
            raum="Klippenpfad"
            gehe_zu(raum)
        elif raum=="Im Steinhaus":
            print("Hier? Im Haus? Ist bei dir alles ok im Oberstübchen?")
        else:
            print("Hier wird sie nicht wachsen.")
    elif objekt=="tomate" and spieler_hat_tomate:
        print("Warum um alles in der Welt willst du eine Tomate pflanzen? Bist du Gärtner?")
        print("Hast du in diesem Spiel nichts besseres zu tun?")
    elif objekt=="schlüssel" and spieler_hat_schlüssel:
        print("Ja. vergraben wir den Schlüssel hier.")
        spieler_hat_schlüssel=False
        if tür_ist_offen:
            print("Zum Glück ist die Tür zum Haus schon offen.")
        else:
            print("Wahrscheinlich ist das Spiel nun hoffnungslos, weil du deine einzige")
            print("Möglichkeit, die Tür zu öffnen, gerade in den Sand gesetzt hast.")
    elif objekt=="brecheisen" and spieler_hat_brecheisen:
        print("Das kannst du vielleicht besser gebrauchen, wenn du es nicht vergräbst.")
    elif objekt=="spaten" and spieler_hat_spaten:
        print("Du willst einen Spaten vergraben??? Mit dem Spaten? Oder mit blossen Händen?")
    else:
        print("Das kannst du nicht vergraben.")

def iss(objekt):
    global spieler_hat_bohne, spiel_zu_ende
    if objekt=="tomate" and (spieler_hat_tomate or raum=="Garten"):
        print("Du isst die Tomate. Sie schmeckt phantastisch.")
        print("Bis zum Moment, wo du an einer akuten Rostvergiftung stirbst.")
        print("Offenbar war der Garten mit Schwermetall belastet.")
        print("Mehr Glück beim nächsten Mal.")
        print("*****")
        print("ENDE.")
        print("*****")
        spiel_zu_ende=True
    elif objekt=="bohne" and spieler_hat_bohne:
        spieler_hat_bohne=False
        print("Dein Heisshunger wurde von dieser Bohne leider nicht gestillt.")
        print("Ausserdem sind rohe Bohnen giftig. Zum Glück kriegst du nur")
        print("Dünnpfiff und erholst dich nach ein paar Stunden vollständig.")
    elif objekt=="spaten" and spieler_hat_spaten:
        print("Das würde dir nicht bekommen. Du willst doch nicht sterben?")
    elif objekt=="brecheisen" and spieler_hat_brecheisen:
        print("Das wäre mir zuviel Eisen. Iss lieber Spinat.")
    elif objekt=="schlüssel" and (spieler_hat_schlüssel or raum=="Steinhaus"):
        print("Du isst den Schlüssel. Keine Ahnung, warum du das machst.")
        print("Besonders gut schmeckt er nicht. Du stirbst noch am selben")
        print("an den Folgen deiner eigenen Dummheit.")
        print("*****")
        print("ENDE!")
        print("*****")
        spiel_zu_ende = True
    else:
        print("Das kannst du nicht essen.")

def gehe_zu(ziel):
    global raum
    raum=ziel    
    print(raum)
    text = beschreibung(raum)
    if text:
        print(text)
    objekte=objekte_in_raum(raum)
    if objekte:
        print(objekte)

def objekt_in_eingabe(eingabe):
    if "tomate" in eingabe:
        return "tomate"
    elif "tür" in eingabe:
        return "tür"
    elif "schlüssel" in eingabe:
        return "schlüssel"
    elif "spaten" in eingabe or "schaufel" in eingabe:
        return "spaten"
    elif "brecheisen" in eingabe or "brechstange" in eingabe:
        return "brecheisen"
    elif "bohne" in eingabe:
        return "bohne"
    elif "hände" in eingabe or "händen" in eingabe or "hand" in eingabe:
        return "hände"
    elif "truhe" in eingabe or "schatz" in eingabe:
        return "truhe"
    elif "sand" in eingabe:
        return "sand"
    elif "schild" in eingabe:
        return "schild"
    elif "hinein" in eingabe and raum == "Im Steinhaus":
        return "hinein"
    else:
        return ""

def ist_kommando_ende(eingabe):
    return eingabe == "ende" or eingabe == "quit" or eingabe == "exit"

def ist_kommando_betrachte(eingabe):
    return "schaue" in eingabe or "betrachte" in eingabe or "untersuche" in eingabe or "lies" in eingabe or "lese" in eingabe

def ist_kommando_öffne(eingabe):
    return "öffne" in eingabe

def ist_kommando_nimm(eingabe):
    return "nimm" in eingabe or "hole" in eingabe or "nehme" in eingabe

def ist_kommando_pflanze(eingabe):
    return "pflanze" in eingabe or "vergrabe" in eingabe or "verbuddle" in eingabe
    
def ist_kommando_iss(eingabe):
    return "iss" in eingabe or "esse" in eingabe or "verspeise" in eingabe

def mache_aktion(eingabe):
    objekt=objekt_in_eingabe(eingabe)
    if ist_kommando_betrachte(eingabe):
        if objekt:
            betrachte(objekt)            
        else:
            print("Das sehe ich hier nicht.")
    elif ist_kommando_nimm(eingabe):
        if objekt:
            nimm(objekt)
        else:
            print("Das geht nicht.")
    elif ist_kommando_öffne(eingabe):
        if objekt:
            öffne(objekt)
        else:
            print("Das geht nicht.")
    elif ist_kommando_pflanze(eingabe):
        if objekt:
            pflanze(objekt)
        else:
            print("Das geht nicht.")
    elif ist_kommando_iss(eingabe):
        if objekt:
            iss(objekt)
        else:
            print("Das würde ich nicht essen wollen.")
    else:
        print("Das verstehe ich nicht.")

def shell():    
    gehe_zu("Olivenhain")
    spiel_zu_ende = False
    while not spiel_zu_ende:
        eingabe = input(">")
        eingabe = eingabe.lower()
        if ist_kommando_ende(eingabe):
            return
        richtung = finde_richtung(eingabe)
        if richtung != "":
            ziel = finde_raum_in_richtung(raum, richtung)
            if ziel == "":
                print("In diese Richtung kannst du nicht gehen.")
            else:                
                gehe_zu(ziel)
        else:
            mache_aktion(eingabe)


print(ANLEITUNG_TEXT)
input()
shell()

