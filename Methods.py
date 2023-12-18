#Methods are functions called from values

#ask user to input name
name = input("What is your name?")

# strip white space
name = name.strip().title()

# split the string
first , last = name.split(" ")

# say hello to user
print(f"Hello {first}")
