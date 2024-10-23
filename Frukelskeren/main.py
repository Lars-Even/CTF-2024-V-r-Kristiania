from itertools import permutations


fruits = [
    "Açai", "Amarillosapote", "Ananas", "Aprikos", "Avokado",
    "Balanitesaegyptiaca", "Banan", "Barbadoslykt", "Brødfrukt",
    "Cherimoya",
    "Daddelpalme", "Daddelplomme", "Drue", "Durian",
    "Eikerplomme", "Ekte fiken", "Ekte mispel",
    "Fersken",
    "Granateple", "Graviola", "Gresskar", "Guava",
    "Indiajujube",
    "Jackfrukt", "Japansk mispel",
    "Kakiplomme", "Kaktusfiken", "Kalebasstre", "Kasjutre", "Kinajujube", "Kirsebær", "Kirsebærplomme", "Kiwano", "Kiwi (frukt)", "Klatrefiken", "Kokebanan", "Kreke", "Krekling", "Kvede",
    "Laurbærhegg", "Litchi", "Longan",
    "Mahaleb", "Mango", "Morbærfiken", "Morell", "Morinda citrifolia",
    "Nektarin",
    "Obstler",
    "Papaya", "Pasjonsfrukt", "Pitahaya", "Plomme", "Pære",
    "Rabarbra", "Rambutan", "Romhegg",
    "Sapodilletre", "Sapote", "Skall", "Smalsølvbusk", "Solanum quitoense", "Solbær", "Steinfrukt", "Stjerneeple", "Stjernefrukt", "Storsapote", "Sviske",
    "Tamarind", "Tyttebær", "Tørket frukt",
    "Virginiahegg"]

combinations = permutations(fruits, 3)

wordlist = ["".join(combo) for combo in combinations]

with open('fruit_wordlist.txt', 'w', encoding='utf-8') as file:
    for combination in wordlist:
        file.write(f"{combination}\n")