def diamond(width: int, char="*"):
    if width % 2 == 0 or width < 1:
        raise ValueError("Šírka musí byť kladné nepárne číslo (1, 3, 5, ...).")

    # horná polovica (vrátane stredu)
    for stars in range(1, width + 1, 2):
        print((char * stars).center(width))

    # dolná polovica
    for stars in range(width - 2, 0, -2):
        print((char * stars).center(width))

# príklad: šírka 5
diamond(5)
