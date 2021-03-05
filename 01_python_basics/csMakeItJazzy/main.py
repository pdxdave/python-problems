""" 
Create a function that concatenates the number 7 to the end 
of every chord in the list.  If a chord already ends 
with a 7, ignore that chord

The append() method adds an item to the end of the list.

append is twice as fast. In general case append will add 
one item to the list, while += will copy all elements 
of right-hand-side list into the left-hand-side list.

"""

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


# 2
def csMakeItJazzy(chords):

    # put the result in a list
    result = []

    # loop through the chords
    for chord in chords:
        # slice the last index off the string
        if chord[-1] == "7":
            # result += [chord]
            result.append(chord)
        else:
            # result += [chord + "7"]
            result.append(chord + "7")
    return result


chords = ["G", "F", "C", "Dm", "G7"]
print(csMakeItJazzy(chords))
