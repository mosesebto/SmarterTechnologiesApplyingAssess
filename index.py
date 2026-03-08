def sort(width, height, length, mass):
    volume = width * height * length

    bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


if __name__ == "__main__":
    # Example runs
    print(sort(10, 10, 10, 5))       # STANDARD
    print(sort(200, 10, 10, 5))      # SPECIAL
    print(sort(200, 200, 200, 25))   # REJECTED