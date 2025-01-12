print("Please enter the following:\n")
    
# Prompting the user for words
adjective = input("Adjective: ")
animal = input("Animal: ")
verb1 = input("Verb: ")
exclamation = input("Exclamation: ").capitalize()  # Automatically capitalizes the first letter
verb2 = input("Verb: ")
verb3 = input("Verb: ")
place = input("Place: ")  # New input for creativity
food = input("Food: ")    # New input for creativity
    
# Building the story
story = (
    f"The other day, I was really in trouble. It all started when I saw a very\n"
    f"{adjective} {animal} {verb1} down the hallway. \"{exclamation}!\" I yelled. But all\n"
    f"I could think to do was to {verb2} over and over. Miraculously,\n"
    f"that caused it to stop, but not before it tried to {verb3}\n"
    f"right in front of my family. Later, I told the story to my friends at the {place},\n"
    f"while enjoying some delicious {food}."
)
    
# Displaying the story
print("\nYour story is:\n")
print(story) 