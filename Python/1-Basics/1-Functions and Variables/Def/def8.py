def create_name(first, last):
    first = first.title()
    last = last.title()
    return first + " " + last

full_name = create_name("Zwivhuya", "Mukwevho")
print(full_name)
