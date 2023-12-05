embassycount = 0 
totalcost = 0
costover50embassiess = 0

while True:
    country = input("Enter the country(or ZZZ to finish)")
    if country == "ZZZ":
        break
    TotalMonthlySalary = float(input("enter total salary of all staff: "))
    Totalelectric= float(input("enter total Electric bill: "))
    weeklyentertainmentallow = float(input("enter total Allowance: "))
    annualmaintainance = float(input("enter annual maintainance: "))
    annualseccost = float(input("enter annual security cost: "))

    annualcost = (TotalMonthlySalary * 12) + (Totalelectric * 12) + (weeklyentertainmentallow * 52) + annualmaintainance + annualseccost
    totalcost += annualcost
    embassycount += 1

    if annualcost >= 500000:
        print(f"The embassy in {country} cost over R50 000.00 per year.")
        costover50embassiess += 1

    averagecost = totalcost/embassycount

    print (f"\n The Total cost of running an embassy is equal to R{totalcost}")
    print (f"\n The Average cost of running an embassy is equal to R{averagecost:.2f}")
    print (f"\nThe Number of embassies costing more than R50 000.00 are {costover50embassiess}")