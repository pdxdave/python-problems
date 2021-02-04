# Create a function that concatenates the number 7 to the end of every chord in the list.  If a chord already ends with a 7, ignore that chord

def csMakeItJazzy(chords):

    # put the result in a list
    result = []

    # loop through the chords
    for chord in chords:
        if chord.endswith("7"):
            result += [chord]
        else:
            # append the chord with the number 7
            result += [chord + "7"]

    return result


chords = ["G", "F", "C", "Dm", "G7"]
print(csMakeItJazzy(chords))