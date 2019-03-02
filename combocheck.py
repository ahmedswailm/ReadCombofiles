#our first python script
#AhmedSwailm
#https://www.youtube.com/ahmedswailm
#http://facebook.com/ahmedswailm2

filepath = "combofile.txt"  #the combo file path (text file we need test it)
combo = open(filepath,"r") #open our file + read it so we can do our work on it
line = list(filepath) #we make our coombo as list so we can split it and use it
for line in combo :# for loop to test every line in our comboaslist
    temp = line.strip().split(":") #we split every line with : so we can take the email or the password or both
    email = temp[0] #the first part of line is the email
    password = temp[1] #the secound is the password
#    print(password) #let's test our work
    #now let's save password and email only
    with open("emails.txt","a",errors="ignore") as emails,open("passwords.txt","a",errors="ignore") as passwords:
        emails.write(email +"\n") #now we save the email in emails.txt file and the "\n" for take new line
        passwords.write(password +"\n") #as the same with emails
        print(email)
        print(password)
print(input("Done !,Hit enter to Exit!"))
#the end of the first part
#thanks
#ahmedswailm
