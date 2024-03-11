print("Ayush Raj CC Lab Mst")
name=input(print("Enter your Name"))
  
email=input(print("Enter your Email Id"))
phone=input(print("Enter your Phone Number"))
cgpa=input(print("Enter your current cgpa"))
print("Enter your 3 Hobbies")
lst =[]
for i in range(3):
  hobby=input()
  lst.append(hobby)
print("Enter 3 Project Names")
pro = []
for i in range(3):
  proj=input()
  pro.append(proj)
company=input(print("Enter company to apply"))
print("...............RESUME................")
print(name)
print("I "+ name+ " want to join your comapny "+ company+ " for SDE position")
print("My Conatact info "+ phone+ " , "+email)
print("Current CGPA : " +cgpa )
print("My Hobbies: "+lst)
print("My projects: "+pro)


