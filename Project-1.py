def get_zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries (March 21 - April 19)"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus (April 20 - May 20)"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini (May 21 - June 20)"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer (June 21 - July 22)"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo (July 23 - August 22)"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo (August 23 - September 22)"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra (September 23 - October 22)"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio (October 23 - November 21)"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius (November 22 - December 21)"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn (December 22 - January 19)"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius (January 20 - February 18)"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces (February 19 - March 20)"
    else:
        return "Invalid date!"

# Main program
try:
    print("Welcome to the Zodiac Sign Teller!")
    month = int(input("Enter your birth month (1-12): "))
    day = int(input("Enter your birth day (1-31): "))

    if 1 <= month <= 12 and 1 <= day <= 31:
        zodiac_sign = get_zodiac_sign(day, month)
        print(f"Your zodiac sign is: {zodiac_sign}")
    else:
        print("Please enter a valid date.")
except ValueError:
    print("Invalid input! Please enter numerical values for month and day.")
