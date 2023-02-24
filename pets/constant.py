import datetime

# model choices
OPTIONS_SPECIES: list[str, str] = [(x, x) for x in ["Cat", "Dog", "Hamster"]]
OPTIONS_YEARS: list[int, int] = [(r, r) for r in range(datetime.datetime.now().year, 1950, -1)]
