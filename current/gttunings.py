possibleTunings = {
    "E Standard": "E Standard",
    "Eb Standard": "Eb Standard",
    "D Standard": "D Standard",
    "C# Standard": "C# Standard",
    "C Standard": "C Standard",
    "B Standard": "B Standard",
    "Drop D": "Drop D",
    "Eb Drop Db": "Eb Drop Db",
    "D Drop C": "D Drop C",
    "C# Drop B": "C# Drop B"
}

def getRoot(note):
    match note:
        case "E":
            return 82.41
        case "Eb":
            return 77.78
        case "D":
            return 73.42
        case "Db":
            return 69.3
        case "C#":
            return 69.3
        case "C":
            return 65.41
        case "B":
            return 61.74