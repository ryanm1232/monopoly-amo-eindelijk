# De READ ME van Monopoly Amersfoort!
# Hierin bevind je spelregels en de codes die je kunt aanpassen om de spelregels te wijzigen.
# LET OP! Na het uitleg van ieder spelregel, zie je eronder de codes die je kunt wijzigen om een spelregel te wijzigen.
# (Met voorbeeld)

# Voordat we beginnen, het codebestand compleet.py moet niet gewijzigd of veranderd worden. Zonder werkt de main en de branches bestanden niet.

# BELANGRIJK!!! 
# Om het spel via main te runnen, moet je het compleet branch open hebben staan. Het is ons niet gelukt om te achterhalen waarom. 
# Wel zijn we achter gekomen dat het hierdoor werkt.


# Spelregels

"""Welkom, dit is Monopoly Amersfoort! Je kent vast de basis principes van Monopoly, zo niet? Geen probleem! 
Gelukkig hebben we spelregels! Laten we eerst beginnen met de spelers """

#1 Spelers (zie branch)
"""Aantal Spelers:
Je speelt met 2 tot 6 spelers Monopoly, dat is het gepaste hoeveelheid voor een normaal potje Monopoly.
Maar indien er toch meerdere spelers willen meedoen, bijvoorbeeld 8, dan kun je dit wijzigen in line 14. 
Zie code onder, door 6 te veranderen naar 8 zal dit lukken."""
# Line 14 -  aantal = int(input("Aantal spelers (2-6): ")) 

"""Start kapitaal:
Ieder speler begint met 1500 euro, wellicht vind je dit niet genoeg en wil je het verhogen naar 2000. 
Dit kun je in line 4 doen. Zie code onder. Je kunt 1500 veranderen naar 2000, hierdoor zullen alle spelers beginnen 2000 euro."""
#Line 4 - self.geld = 1500


#2 Kanskaarten (zie branch)
""" Ieder keer dat een speler landt op Jack's Casino, krijgt diegene een kanskaart!
Had je gewenst om de tekst te wijzigen of een kanskaart toe te voegen? Je kunt dit doen als volgt zie code hieronder.
In principe behou je 3 structuren. Zie codes onder.
Je kunt bij tekst, de beschrijving geven van je kanskaart. 
Actie zal altijd gevolgt moeten worden met geld/jilla/verplaats.

- Geld, moet gevolgt worden met bedrag. Deze zorgt ervoor dat er geld erbij of eraf wordt gehaaldt. Zie voorbeeld 1 en 2.

- Jilla, is een directe actie dat je naar de gevangenis moet. Zie voorbeeld 3.

- Verplaats, moet gevolgt worden stappen. Deze zorgt ervoor dat je stappen vooruit gaat of achteruit, zie voorbeeld 4. """

# Je kunt eigen kanskaarten toevoegen zolang het binnen deze vakjes zitten '[]' bij self.kaarten = [...]
# class KansStapel:
#     def __init__(self, jail_index, bord):
#         self.jail_index = jail_index
#         self.bord = bord
#         self.kaarten = [
#             Kanskaart("Je krijgt €200 subsidie", "geld", 200),
#             Kanskaart("Je betaalt €150 boete", "geld", -150),
#             Kanskaart("Je gaat direct naar Jilla", "jilla"),
#             Kanskaart("Je loopt 3 vakjes vooruit", "verplaats", stappen=3),
#         ]


#3 Bord (zie branch)

"""Je vindt in bestand bord.py alle gegevens van de straat vakken, aldus zie je de prijzen, huur en bouwkosten voor huizen. 
Zie line 21, hierbij hebben we de type straten vaste waardes gegeven. De bouwprijzen, house_cost kun je verlagen of verhogen.
Hetzelfde geldt voor huur die gebonden is aan rent alle int binnen [] zijn voor de huurprijzen."""

# SET_RULES = {
#     "Liendert":       {"house_cost": 50,  "rent": [2, 10, 30, 90, 160, 250]},
#     "Kruiskamp":      {"house_cost": 50,  "rent": [4, 20, 60, 180, 320, 450]},
#     "Soesterkwartier":{"house_cost": 100, "rent": [6, 30, 90, 270, 400, 550]},
#     "Stad":           {"house_cost": 100, "rent": [8, 40, 100, 300, 450, 600]},
#     "Hooglanderveen": {"house_cost": 150, "rent": [10, 50, 150, 450, 625, 750]},
#     "Hoogland":       {"house_cost": 150, "rent": [12, 60, 180, 500, 700, 900]},
#     "Vathorst":       {"house_cost": 200, "rent": [14, 70, 200, 550, 750, 950]},
#     "Berg":           {"house_cost": 200, "rent": [16, 80, 220, 600, 800, 1000]},
# }


"""Indien je een eigen Monopoly van je eigen stad wilt hebben, kun je in line 35 de bord gegevens per vak wijzigen
Je zou de types kunnen wijzigen deze stellen wijken voor, en "naam" kun je erachter veranderen voor de straat die je wilt hebben."""
# bord = [
#     {"naam": "Start", "type": "start"},
#     {"naam": "Arendshorst", "type": "Liendert", "prijs": 60, "eigenaar": None, "huizen": 0},
#     {"naam": "Jack's Casino", "type": "kans"},
#     {"naam": "Havikshorst", "type": "Liendert", "prijs": 60, "eigenaar": None, "huizen": 0},
#     {"naam": "Gemeentebelasting", "type": "belasting", "bedrag": 200},
#     {"naam": "Take a Break", "type": "station", "prijs": 200, "eigenaar": None},
#     {"naam": "Neptunesplein", "type": "Kruiskamp", "prijs": 100, "eigenaar": None, "huizen": 0},
#     {"naam": "Jack's Casino", "type": "kans"},
#     {"naam": "De Stier", "type": "Kruiskamp", "prijs": 100, "eigenaar": None, "huizen": 0},

# De rest van de functie codes wordt afgeraden om te wijzigen. Dit zijn hulpfuncties die helpen bij herkennen en bereken bij de vakken.

# 4 Leaderboard (zie branch)
""" Het doel van deze bestand is om een compact leaderboard te weergeven met:

- Rang, naam, aantal straten, geld, huizen

- Eigendommen per speler in een blokweergave

- Vakkenoverzicht in twee kolommen"""

# Er bevalt niet veel te wijzigen in het bestand, het is een extra visuele toevoeging voor het spel.


# 5 Spel 
""" Dit bestand doet de volgende;
- Start een Monopolyspel met spelers, dobbelstenen en een bord.

- Verplaatst spelers over het bord, toont naam van het vak en verwerkt kanskaarten.

- Laat na elke beurt een leaderboard zien met rangorde op basis van bezittingen"""

""" Iedere def functies heeft een eigen rol in het spel."""
# def maak_spelers() is voor het aantal spelers en namen
# def gooi_dobbelstenen(speler) verwerkt de spelbeurt en verplaatsen van spelers
# def handel_vak_actie(self, speler, vak) dit vewerkt welke acties uitgevoerd kunnen worden door spelers. 
# def start_spel(self) hiermee gaat het spel beginnen en verloopt de while lus tot het eindigt. 