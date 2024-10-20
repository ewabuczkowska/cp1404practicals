"""
CP1404 - Practical 5 - 2. Hex Colours
"""

COLOUR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "Coral": "#ff7f50",
    "DarkSlateBlue": "#483d8b",
    "Gold": "#ffd700",
    "HotPink": "#ff69b4",
    "Lavender": "#e6e6fa",
    "MediumSeaGreen": "#3cb371",
    "Orchid": "#da70d6",
    "SteelBlue": "#4682b4",
    "Tomato": "#ff6347"
}

max_length = max(len(colour) for colour in list(COLOUR_TO_HEX.keys()))

for colour in COLOUR_TO_HEX:
    print(f"{colour:{max_length}} - {COLOUR_TO_HEX[colour]}")

colour_name = input("Colour: ").title()
while colour_name != "":
    try:
        print(f"{colour_name} is {COLOUR_TO_HEX[colour_name]}")
    except KeyError:
        print(f"'{colour_name}' is not a valid colour name")
    colour_name = input("Colour: ").title()
