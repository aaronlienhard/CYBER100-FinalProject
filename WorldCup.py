year = int(input("What year do you want to check? "))
print("")

if year < 1927:
    print("Year must be above 1927")
    
if year > 1927:
    first = 1930
    dif = year - first
    mult = float(dif / 4)
    x = mult % 1
    winner = winner = {1930: "Uruguay", 1934: "Italy", 1938:"Italy", 1942: "No Team",
                       1946: "No Team", 1950: "Uruguay", 1954: "West Germany", 1958: "Brazil", 1962: "Brazil",
                       1966: "England", 1970: "Brazil", 1974: "Germany", 1978: "Argentina", 1982: "Italy",
                       1986: "Argentina", 1990: "West Germany", 1994: "Brazil", 1998: "France", 2002: "Brazil",
                       2006: "Italy", 2010: "Spain", 2014: "Germany", 2018: "France",  2022: "No team has"}
    if year == 1930:
        print("This was the first world cup.")
        print(winner[year] + " won that year.")
    elif (dif % 4 == 0) and (dif % 100 != 0) and (dif > 0):
        print("{0} is a world cup year, the next world cup is in four years".format(year))
        if mult < 24:
            print(winner[year] + " won that year.")
        else:
            print("Games have not been played yet")
    elif x == .5:
        print("{0} is not a world cup year.".format(year))
        print("The next world cup is in 2 years.")
    elif x == .25:
        print("{0} is not a world cup year.".format(year))
        print("The next world cup is in 3 years.")
    elif x == .75:
        print("{0} is not a world cup year.".format(year))
        print("The next world cup is in 1 year.")
