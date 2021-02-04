# Given a string of words, return the length of the shortest word(s)

# Two solutions

def csShortestWord(input_str):
    # 1
    # Create a list to contain the words
    results = []
    # loop through string and split them into individual words
    for word in input_str.split():
        # append words to results
        results.append(word)
    # key (optional) - key function where the interables are 
    # passed and comparions is performed based on its
    # return value
    return len(min(results, key = len))

    # to get the word instead of the length
    return max(results, key = len)


    # 2
    test = min(len(word) for word in input_str.split())
    return test


input_str = "two ducks in a pond"
print(csShortestWord(input_str))