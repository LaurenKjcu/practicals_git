COLOUR_TO_HEX = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "black": "#000000", "CadetBlue": "#5f9ea0",
                 "CornflowerBlue": "#6495ed", "coral": "#ff7f50", "DarkGoldenrod": "#b8860b", "DarkGreen": "#006400",
                 "DarkOrchid": "#9932cc", "DarkSeaGreen": "#8fbc8f0000"}
colour_name = input("colour name:")
while colour_name != "":
    try:
        colour_hex = COLOUR_TO_HEX[colour_name]
        print(colour_hex)
        colour_name = input("colour name:")
    except KeyError:
        print("not an available colour")
        colour_name = input("colour name:")