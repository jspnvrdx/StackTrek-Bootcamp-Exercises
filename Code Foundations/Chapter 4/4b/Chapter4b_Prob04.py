import os
os.system('cls||clear')

#----CODE STARTS HERE------

date = int(input())
month = input()

if (date >= 22 and date <= 31 and month == "december") or (date >= 1 and date <= 19 and month == "january"):
    print("Your Astrological sign is : Capricorn")
elif (date >= 20 and date <= 31 and month == "january") or (date >= 1 and date <= 18 and month == "february"):
    print("Your Astrological sign is : Aquarius")
elif (date >= 19 and date <= 29 and month == "february") or (date >= 1 and date <= 20 and month == "march"):
    print("Your Astrological sign is : Pisces")
elif (date >= 21 and date <= 31 and month == "march") or (date >= 1 and date <= 19 and month == "april"):
    print("Your Astrological sign is : Aries")
elif (date >= 20 and date <= 30 and month == "april") or (date >= 1 and date <= 20 and month == "may"):
    print("Your Astrological sign is : Taurus")
elif (date >= 21 and date <= 31 and month == "may") or (date >= 1 and date <= 20 and month == "june"):
    print("Your Astrological sign is : Gemini")
elif (date >= 21 and date <= 30 and month == "june") or (date >= 1 and date <= 22 and month == "july"):
    print("Your Astrological sign is : Cancer")
elif (date >= 23 and date <= 31 and month == "july") or (date >= 1 and date <= 22 and month == "august"):
    print("Your Astrological sign is : Leo")
elif (date >= 23 and date <= 31 and month == "august") or (date >= 1 and date <= 22 and month == "september"):
    print("Your Astrological sign is : Virgo")
elif (date >= 23 and date <= 30 and month == "september") or (date >= 1 and date <= 22 and month == "october"):
    print("Your Astrological sign is : Libra")
elif (date >= 23 and date <= 31 and month == "september") or (date >= 1 and date <= 21 and month == "november"):
    print("Your Astrological sign is : Scorpio")
elif (date >= 22 and date <= 30 and month == "november") or (date >= 1 and date <= 21 and month == "december"):
    print("Your Astrological sign is : Sagittarius")