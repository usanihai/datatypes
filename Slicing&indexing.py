neha=[{"id": 9,
       "name": "Imran",
       "add":"India",
       "place":"Malakpet",
       "speciality": "Hydrabadi_Biryani",
       "Flavour":"Mutton",
       "extra":"Raita"},
       "Dubai",
       "Maldives",
       "Thailand",
       "EMPID_4401",
       3+8j,
      False]

#use  next line character and split all the values/column
#print(*neha , sep="\n")

#print("this is indexing: ", neha[0])


#data = neha[0]
#print(data["add"])
#print(data["place"])
#print(neha[1])
#print(data["extra"])

#data = neha[0]
#print(data["speciality"] +" with extra "+ data["extra"])
#print ("speciality" * 7)


#update & print your employe_id.Hint - use pop first to delete.
#neha.pop(4)
#print(neha)
#neha.insert(4,"EMPLID_77395")
#print(neha)
#neha.insert(4,"EMPLID_7735_updated")
#print(neha[4])

# Update using Indexing & change your favourite destination


#neha[3] = "lA"
#print(neha)
# Print & extract all values in the dictionary

# Access the dictionary inside the list
my_dict = neha[0]

values = neha[0].values()
print(*values,sep="\n")


#for v in neha[0].values(): print(v)


