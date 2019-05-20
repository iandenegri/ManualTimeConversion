"""
Purpose of this file is to create a script that can take a string of text and try to convert it from a 24 hour format (Like 20:00) to an AM/PM format (In this case 08:00 PM.) without the use of third party packages.
Please be sure to call this script in the following format:
"python, FILE_NAME.py, TIME_TO_CONVERT"
"""

import sys

def Time_Format_Conversion(time_string: str, AMPM: str):
    """
    Converts strings of time formatted in the 24 hour style to an AM/PM style.
    Converts strings of time formatted in the AM/PM style to the 24 hour style.
    Takes one argument which is a string that should be formatted either in "20:00" or "08:00 PM" formats.
    """
    if AMPM == "N/A":
        #If this is NA then we're converting a 24hr time string to AMPM.
        hrs = time_string.split(':')[0]
        mins = time_string.split(':')[1]
        print(hrs)
        print(mins)
        if hrs == 0:
            hrs = "12"
            AMPM = "AM"
            converted_time = (hrs + mins + AMPM)
            print(converted_time)
            return converted_time
        elif hrs == 12:
            hrs = "12"
            AMPM = "PM"
            converted_time = (hrs + mins + AMPM)
            print(converted_time)
            return converted_time
        elif hrs > 12:
            hrs = str(hrs-12)
            print(hrs)
        else:
            AMPM = "AM"
            converted_time = (hrs + mins + AMPM)
            print(converted_time)
            return converted_time
    else:
        #If we have something that isn't NA then we should have an AM or PM value. We can do an AM/PM check at the start when we're getting args from the command line.
        if AMPM == "AM":
            #If we're in the AM then no conversions need to be done. :-)
            time = time_string[:6]
            print(time)
            hrs = time_string.split(':')[0]
            mins = time_string.split(':')[1]
            print(hrs)
            print(mins)
            converted_time="uwu"
        else:
            #We should be in the PM so we need to add 12 hours to the time.
            hrs = time_string.split(':')[0]
            mins = time_string.split(':')[1]
            print(hrs)
            print(mins)
            pass
    return(converted_time)


def determine_time_format():
    # Move all the logic for determining what the input was to here.
    return "uwu"

# Make sure this isn't being imported. If it is then variables will not be passed in through command line but as arguments in the coversion function.
if __name__ == "__main__":
    # Get inputs by using "sys.argv". sys.argv[0] = file name, sys.argv[1] = first arg, etc.
    if len(sys.argv) == 2:
        # Need to verify that the first two chars are ints, the third char is a ":" and the last two chars are ints.
        time_to_convert = sys.argv[1]
        AMPM = "N/A"
        print("Observed a 24hr format object.")
    elif len(sys.argv) == 3:
        # We should check in sys.argv[2] is AM/PM at some point.
        time_to_convert = sys.argv[1]
        AMPM = sys.argv[2]
        print("Observed an AMPM format object.")
    else:
        number_of_arguments = (len(sys.argv)-1)
        print("Please pass in at least 1 argument in a time format or 2 arguments in a time and AM/PM format. \nIE: 20:00 or 08:00 PM")
        print("The number of arguments you passed was/were: %s" % number_of_arguments)
        AMPM = "N/A"

    Time_Format_Conversion(time_to_convert, AMPM)