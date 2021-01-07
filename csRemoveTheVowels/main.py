def csRemoveTheVowels(input_str):

    # make a list of vowels
    vowels = ['a','e','i','o','u','A','E','I','O','U']

    for i in input_str:
        # if a character is in the vowels
        if i in vowels:
            # replace the vowel in the string with and empty space
            input_str = input_str.replace(i, "")
    return input_str

input_str = "funny dogs in the park"
print(csRemoveTheVowels(input_str))