"""
Purpose of this file is to create a script that can take a string of text and try to convert it from a 24 hour format (Like 20:00) to an AM/PM format (In this case 08:00 PM.).
Please be sure to call this script in the following format:
"python, FILE_NAME.py, TIME_TO_CONVERT"
"""

import sys

# Make sure this isn't being imported. If it is then variables will not be passed in through command line but as arguments in the coversion function.
if __name__ == "__main__":
    # Get inputs by using "sys.argv". sys.argv[0] = file name, sys.argv[1] = first arg, etc.
    if len(sys.argv) == 2:
        time_to_convert = sys.argv[1]
        AMPM = "NA"
        print("Observed a 24hr format object.")
    elif len(sys.argv) == 3:
        time_to_convert = sys.argv[1]
        AMPM = sys.argv[2]
        print("Observed an AMPM format object.")
    else:
        print("Please pass in at least 1 argument in a time format or 2 arguments in a time and AM/PM format. \nIE: 20:00 or 08:00 PM")
        print(len(sys.argv))
        AMPM = "NA"

def Time_Format_Conversion(time_string: str, AMPM: str):
    """
    Converts strings of time formatted in the 24 hour style to an AM/PM style.
    Converts strings of time formatted in the AM/PM style to the 24 hour style.
    Takes one argument which is a string that should be formatted either in "20:00" or "08:00 PM" formats.
    """
    print(time_string)
