def getPossibleTunings(type):
    if type == "st":
        possibleTunings= ["E Standard", "Eb Standard", "D Standard", "C# Standard", "C Standard"]
    if type == "dr":
        possibleTunings= ["E Drop D", "Eb Drop Db", "D Drop C", "C# Drop B"]
    return possibleTunings

def getNotation(type, note):
    if type == "st":
        if note == "E":
            notesArray = ["E", "A", "D", "G", "B", "Eb"]
        if note == "Eb":
            notesArray = ["Eb", "Ab", "Db", "Gb", "Bb", "Eb"]
        if note == "D":
            notesArray = ["D", "G", "C", "F", "A", "D"]
        if note == "C#":
            notesArray = ["C#", "F#", "B", "E", "G#", "C#"]
        if note == "C":
            notesArray = ["C", "F", "Bb", "Eb", "G", "C"]
    if type == "dr":
        if note == "E Drop D":
            notesArray = ["D", "A", "D", "G", "B", "e"]
        if note == "Eb Drop Db":
            notesArray = ["Db", "Ab", "Db", "Gb", "Bb", "Eb"]
        if note == "D Drop C":
            notesArray = ["C", "G", "C", "F", "A", "D"]
        if note == "C# Drop B":
            notesArray = ["B", "F#", "B", "E", "G#", "C#"]
    return notesArray