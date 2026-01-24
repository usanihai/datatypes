Airline = ["Etihad", "Delta", "British","Unites"]
Airline_prices = {
    "Etihad": 1000,
    "Delta": 2000,
    "British": 3000,
    "Unites": 4000
    }
Family_Members = {
    "Niha" : 6,
    "Naimath" : 5

}
Airline_name = input("Enter airline name: ")
family_name= input("Enter family name 'Niha or Naimath': ")

if Airline_name in Airline:

    if Airline_name == Airline[0] or Airline[1] or Airline[2] or Airline[3]:
        #print(Airline)
        price_per_seat = Airline_prices[Airline_name]

        if family_name in Family_Members:

            total_family_member= Family_Members[family_name]

            Total_price_for_all= price_per_seat * total_family_member

            print(f"{family_name}'s family ticket cost for {Airline_name} is ${Total_price_for_all} ")