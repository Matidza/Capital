def weight(mass, gravity = 9.82):
    weight = float(str(mass * gravity))
    return print(f"{weight:.2f}", "N")
weight(56)

def age( birth_year, current_year = 2023):
    calculate = current_year - birth_year
    return print(calculate)
age(1997)