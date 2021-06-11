from graphs import NodePair


cities = [
    "Wrocław",
    "Katowice",
    "Gliwice",
    "Zawiercie",
    "Oświęcim",
    "Kraków",
    "Miechów",
    "Kielce",
    "Radom",
    "Warszawa",
    "Wieliczka",
    "Rabka-Zdrój",
    "Zakopane",
    "Nowy Sącz",
    "Nowy Targ",
    "Tarnów",
    "Dębica",
    "Rzeszów",
    "Przeworsk",
    "Przemyśl"
]
"""
List of available cities
"""

initial_connections = [
    NodePair("Wrocław", "Gliwice"),
    NodePair("Katowice", "Gliwice"),
    NodePair("Katowice", "Zawiercie"),
    NodePair("Katowice", "Kraków"),
    NodePair("Kraków", "Oświęcim"),
    NodePair("Kraków", "Miechów"),
    NodePair("Miechów", "Kielce"),
    NodePair("Kielce", "Radom"),
    NodePair("Miechów", "Warszawa"),
    NodePair("Kraków", "Wieliczka"),
    NodePair("Kraków", "Rabka-Zdrój"),
    NodePair("Rabka-Zdrój", "Nowy Targ"),
    NodePair("Nowy Targ", "Zakopane"),
    NodePair("Rabka-Zdrój", "Nowy Sącz"),
    NodePair("Nowy Sącz", "Tarnów"),
    NodePair("Kraków", "Tarnów"),
    NodePair("Tarnów", "Dębica"),
    NodePair("Dębica", "Rzeszów"),
    NodePair("Rzeszów", "Przeworsk"),
    NodePair("Przeworsk", "Przemyśl")
]