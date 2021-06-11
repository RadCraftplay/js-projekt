
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
    ("Wrocław", "Gliwice"),
    ("Katowice", "Gliwice"),
    ("Katowice", "Zawiercie"),
    ("Katowice", "Kraków"),
    ("Kraków", "Oświęcim"),
    ("Kraków", "Miechów"),
    ("Miechów", "Kielce"),
    ("Kielce", "Radom"),
    ("Miechów", "Warszawa"),
    ("Kraków", "Wieliczka"),
    ("Kraków", "Rabka-Zdrój"),
    ("Rabka-Zdrój", "Nowy Targ"),
    ("Nowy Targ", "Zakopane"),
    ("Rabka-Zdrój", "Nowy Sącz"),
    ("Nowy Sącz", "Tarnów"),
    ("Kraków", "Tarnów"),
    ("Tarnów", "Dębica"),
    ("Dębica", "Rzeszów"),
    ("Rzeszów", "Przeworsk"),
    ("Przeworsk", "Przemyśl")
]
"""
List of initial connections
"""