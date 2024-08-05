#string concatenation (aka how to put strings together)
#suppose we want to create a string that says "subscribe to _____"
# youtuber = "Joshua Allen"


#few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")


# learning how to get input from the user, work with f strings and see results printed to the console.
noun1 = input("Persons Name: ")
noun2 = input("Noun: ")
noun3 = input("Noun: ")
adj1 = input("Feeling: ")
adj2 = input("Feeling: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
verb3 = input("Verb ending in ing: ")
animal = input("Animal: ")
color = input("Color: ")
color2 = input("Color: ")
adverb = input("Adverb ending with ly: ")
number = input("Number: ")
number2 = input("Number: ")
measureOfTime = input("Time (ex. secs, mins hours): ")
animal2 = input("Animal: ")
sillyWord = input("Something silly: ")





madlib = f"This weekend I am going camping with {noun1}. I packed my lantern, sleeping bag, and {noun2}. I am so {adj1} to {verb1} in a tent. I am {adj2} we might see a {animal} they are kind of dangerous. We are going to hike, fish, and {verb2}. I have heard that the {color} lake is great for {verb3}. Then we will {adverb} hike through the forest for {number} {measureOfTime}. If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet! At night we will tell {number2} {sillyWord} stories and roast {noun3} around the campfire!!"

print(madlib)