def sort(width, height, length, mass):
    volume = width * height * length

    bulky = volume >= 1000000 or max(width, height, length) >= 150
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"