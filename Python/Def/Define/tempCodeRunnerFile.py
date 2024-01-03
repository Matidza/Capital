def weight(mass, gravity):
    weight = float(str(mass * gravity))
    return print(f"{weight:.2f}", "N")
weight(56, 9.82)