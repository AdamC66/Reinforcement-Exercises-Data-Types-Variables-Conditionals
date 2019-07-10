#Think of a documentary, a drama, a comedy, and a dramedy. 
# Store the titles of these films in variables. 
# Ask the user if they enjoy 1. documentaries 2. dramas 3. comedies. 
# If they answer yes to documentaries, display a message recommending the documentary to them. 
# If they answer no to documentaries but yes to dramas and comedies, recommend the dramedy. 
# If they answer yes to only dramas, recommend the drama. If they say yes to only comedies, recommend the comedy. 
# If they answer no to all three, recommend a good book instead.

documentary = "Planet Earth"
comedy = "White Chicks"
drama = "Schindler\'s List"
dramedy = "Silver Linings Playbook"

getinput = True
likes_comedy = False
likes_dramas = False
likes_documentaries = False

print("Hello user, this is a movie reccomendation program. please answer \"Yes\" or \"No\" (Y/N) to the following:")

print("Do you like documentaries?")
while getinput == True:
    usrinput = input().lower()
    if usrinput == "yes" or usrinput =="y" or usrinput == "no" or usrinput =="n":
        getinput = False
        if usrinput == "yes" or usrinput =="y":
            likes_documentaries=True
    else: 
        print("your answer is invalid, please enter \"Yes\" or \"No\" (Y/N)")



print("Do you like dramas?")
getinput = True
while getinput == True:
    usrinput = input().lower()
    if usrinput == "yes" or usrinput =="y" or usrinput == "no" or usrinput =="n":
        getinput = False
        if usrinput == "yes" or usrinput =="y":
            likes_dramas=True
    else: 
        print("your answer is invalid, please enter \"Yes\" or \"No\" (Y/N)")


print("Do you like comedies?")
getinput = True
while getinput == True:
    usrinput = input().lower()
    if usrinput == "yes" or usrinput =="y" or usrinput == "no" or usrinput =="n":
        getinput = False
        if usrinput == "yes" or usrinput =="y":
            likes_comedy=True
    else: 
        print("your answer is invalid, please enter \"Yes\" or \"No\" (Y/N)")

# If they answer yes to documentaries, display a message recommending the documentary to them.

if likes_documentaries == True and likes_comedy == False and likes_dramas == False:
    print("we reccomend a good documentary, try {}".format(documentary))
elif likes_documentaries == False and likes_comedy == True and likes_dramas == True:
    print("we reccoment a good dramedy, how about {}".format(dramedy))
elif likes_comedy == True and likes_documentaries == False and likes_dramas == False:
    print("Looks like you like comedy, you should check out {}".format(comedy))
elif likes_dramas == True and likes_comedy == False and likes_documentaries == False:
    print("okay, you like dramas, have you seen {}".format(drama))
else:
    print("I dunno, maybe read a book or something")


