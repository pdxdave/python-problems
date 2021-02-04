# Only letters and no numbers
# Only numbers and no letters

# objective 9 - conditional expressions section
def csAlphanumericRestriction(input_str):

    if input_str.isalpha():
        return True 
    if input_str.isdigit():
        return True
    else:
        return False


input_str = "Bold"
input_str = "123456"
input_str = "H3LLO"
print(csAlphanumericRestriction(input_str))