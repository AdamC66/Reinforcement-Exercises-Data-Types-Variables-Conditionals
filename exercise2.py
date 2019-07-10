#Let's take a different approach to film recommendations: create the same variables containing your potential film recommendations 
# and then ask the user to rate their appreciation for 1. documentaries 2. dramas 3. comedies on a scale from one to five. 
# If they rate documentaries four or higher, recommend the documentary. 
# If they rate documentaries 3 or lower but both comedies and dramas 4 or higher, recommend the dramedy. 
# If they rate only dramas 4 or higher, recommend the drama. If they rate just comedies 4 or higher, recommend the comedy. 
# Otherwise, recommend a good book.



documentary = "Planet Earth"
comedy = "White Chicks"
drama = "Schindler\'s List"
dramedy = "Silver Linings Playbook"

getinput = True
likes_comedy = False
likes_dramas = False
likes_documentaries = False

print("Hello user, this is a movie reccomendation program. please rank the following genres on a scale from 1-5:")

print("on a scale of 1-5 how do you rank documentaries?")
while getinput == True:
    usrinput = int(input())
    if usrinput > 0 and usrinput < 6:
        getinput = False
        likes_documentaries= usrinput
    else: 
        print("your answer is invalid, please rank the following genres on a scale from 1-5:")



print("on a scale of 1-5 how do you rank dramas?")
getinput = True
while getinput == True:
    usrinput = int(input())
    if usrinput > 0 and usrinput < 6:
        getinput = False
        likes_dramas=usrinput
    else: 
        print("your answer is invalid, please rank the following genres on a scale from 1-5:")


print("on a scale of 1-5 how do you rank comedies?")
getinput = True
while getinput == True:
    usrinput = int(input())
    if usrinput > 0 and usrinput < 6:
        getinput = False
        likes_comedy=usrinput
    else: 
        print("your answer is invalid,please rank the following genres on a scale from 1-5:")

# If they rate documentaries four or higher, recommend the documentary. 
# If they rate documentaries 3 or lower but both comedies and dramas 4 or higher, recommend the dramedy. 
# If they rate only dramas 4 or higher, recommend the drama. If they rate just comedies 4 or higher, recommend the comedy. 
# Otherwise, recommend a good book.

print ("your ranks: \nDocumentaries: {} \nDramas: {} \nComedies: {}\n".format(likes_documentaries,likes_dramas,likes_comedy))

if likes_documentaries >= 4 and likes_comedy < 4 and likes_dramas < 4:
    print("we reccomend a good documentary, try {}".format(documentary))

elif likes_documentaries <=3 and likes_comedy >3 and likes_dramas >3:
    print("we reccoment a good dramedy, how about {}".format(dramedy))

elif likes_comedy >=4 and likes_documentaries < 4 and likes_dramas < 4:
    print("Looks like you like comedy, you should check out {}".format(comedy))

elif likes_dramas >=4 and likes_documentaries < 4 and likes_comedy < 4:
    print("okay, you like dramas, have you seen {}".format(drama))

else:
    print("I dunno, maybe read a book or something")