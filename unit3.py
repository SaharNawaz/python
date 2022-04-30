#ec 3.1
list= ['Hamna', 'Saba', 'Sidra', 'Sana', 'Maryam']
print(list)

#ex 3.2
list = ['Alia', 'Rubia', 'Sobia', 'Asma', 'Waheeda']
print("Hey how are you "+list[0].title()+'.')
print("Hey how are you "+list[1].title()+'.')
print("Hey how are you "+list[2].title()+'.')
print("Hey how are you "+list[3].title()+'.')
print("Hey how are you "+list[4].title()+'.')

#ex 3.3
Car=['Civic','Mark X','City','Alisvan']
print ("I Would like to own "+ Car[0]+'.')
print ("I Would like to own "+ Car[1]+'.')
print ("I Would like to own "+ Car[2]+'.')
print ("I Would like to own "+ Car[3]+'.')

#ex 3.4
Guests=['Abida','Waleeda','Asia','Rimsha']
print(Guests)
print ("hey dear you are invited for a dinner " +Guests[0].title()+ '.')
print ("hey dear you are invited for a dinner " +Guests[1].title()+ '.')
print ("hey dear you are invited for a dinner " +Guests[2].title()+ '.')

#ex 3.5
Guests=['Anam','Iram','Ayesha','Anisa']
print(Guests)
print ("hey dear you are invited for a dinner " +Guests[0].title()+ '.')
print ("hey dear you are invited for a dinner " +Guests[1].title()+ '.')
print ("hey dear you are invited for a dinner " +Guests[2].title()+ '.')
print ("Sorry "+ Guests[0].title()+ "Cant make it to dinner" )
del Guests[0]
Guests.insert(0,'Rozina')
print (Guests)
print ("hey dear you are invited for a dinner " + Guests[0].title()+ '.')


#ex 3.6
Guests=['Asma','Wajida','Abida','Asifa']
print(Guests)
print ("hey dear you are invited for a dinner " +Guests[0].title()+ '.')
print ("hey dear you are invited for a dinner " +Guests[1].title()+ '.')
print ("hey dear you are invited for a dinner " +Guests[2].title()+ '.')
print("cant make a dinner")
Guests=['Asma','Wajida','Abida','Asifa']
print(Guests)
print ("hey dear you are invited for a dinner " +Guests[0].title()+ '.')
print ("hey dear you are invited for a dinner " +Guests[1].title()+ '.')
print ("hey dear you are invited for a dinner " +Guests[2].title()+ '.')
print ("Sorry "+ Guests[0].title()+ "Cant make it to dinner" )
del Guests[0]
Guests.insert(0,'Rehana')
print (Guests)
print ("hey dear you are invited for a dinner " + Guests[0].title()+ '.')
print ("Found Bigger Table")
print(Guests)
Guests.insert(4,"ibrahim")
print ("hey dear you are invited for a dinner " + Guests[4].title()+ '.')
Guests.insert(5,"Ali")
print ("hey dear you are invited for a dinner " + Guests[5].title()+ '.')
print(Guests)


#ex 3.7
Guests=['Alia','Waleeda','Asifa','Anisa']
print(Guests)
print ("hey dear you are invited for a dinner " +Guests[0].title()+ '.')
print ("hey dear you are invited for a dinner " +Guests[1].title()+ '.')
print ("hey dear you are invited for a dinner " +Guests[2].title()+ '.')
print("cant make a dinner")
Guests=['Alia','Waleeda','Asifa','Anisa']
print(Guests)
print ("hey dear you are invited for a dinner " +Guests[0].title()+ '.')
print ("hey dear you are invited for a dinner " +Guests[1].title()+ '.')
print ("hey dear you are invited for a dinner " +Guests[2].title()+ '.')
print ("Sorry "+ Guests[0].title()+ "Cant make it to dinner" )
del Guests[0]
Guests.insert(0,'Rehana')
print (Guests)
print ("hey dear you are invited for a dinner " + Guests[0].title()+ '.')
print ("Found Bigger Table")
Guests.insert(4,'Iqra')
print ("hey dear you are invited for a dinner " + Guests[4].title()+ '.')
Guests.insert(5,'Iram')
print ("hey dear you are invited for a dinner " + Guests[5].title()+ '.')
print(Guests)
print ("sorry you cant invite them to dinner " + Guests[0].title()+ '.')
print ("sorry you cant invite them to dinner " + Guests[1].title()+ '.')
print ("sorry you cant invite them to dinner " + Guests[2].title()+ '.')
print ("sorry you cant invite them to dinner " + Guests[3].title()+ '.')
print ("You are invited for dinner " + Guests[4].title()+ '.')
print ("You are invited for dinner " + Guests[5].title()+ '.')
#Guests.pop(0)
#Guests.pop(1)
#Guests.pop(2)
#Guests.pop(4)


#ex 3.8
Places=['Lahore','Multan','Okara','sahiwal','Khanewal']
print(Places)
print ("Sourted List")
Places.sort()
print(Places)
Places=['Lahore','Multan','Okara','sahiwal','Ali Pur']
print(sorted(Places))
print(Places)
print(sorted(Places, reverse=True))
print(Places)
print(sorted(Places, reverse=True))
print(Places)
Places.sort()
print(Places)


#ex 3.9
Guests=['sahar','sana','saba','iqra']
print(Guests)
print("sorry you are not invited "+Guests[0]+'.')
del Guests[0]
print(Guests)
print("sorry you are not invited "+Guests[1]+'.')
del Guests[1]
print("sorry you are  invited "+Guests[0]+'.')
print("sorry you are  invited "+Guests[1]+'.')
len(Guests)

#ex 3.10
fruit=['Mango','Banana','Orange','apple']
print(fruit)
print("sorry you are  invited "+fruit[1]+'.')
print(fruit)
fruit.insert(4,'Apple')
fruit[0] ="Guava"
print(fruit)
fruit.append('mango')
print(fruit)
del fruit[0]
print(fruit)
fruit.sort()
print(fruit)
fruit.reverse()
print (fruit)
len(fruit)