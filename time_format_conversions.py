"""
Purpose of this file is to create a script that can take a string of text and try to convert it from a 24 hour format (Like 20:00) to an AM/PM format (In this case 08:00 PM.) without the use of third party packages.
Please be sure to call this script in the following format:
"python, FILE_NAME.py, TIME_TO_CONVERT"
"""

import sys

# Once everything is working this can be converted to a class object and then be imported to the testing file.
def Time_Format_Conversion(time_string: str, AMPM: str):
    """
    Converts strings of time formatted in the 24 hour style to an AM/PM style.
    Converts strings of time formatted in the AM/PM style to the 24 hour style.
    Takes one argument which is a string that should be formatted either in "20:00" or "08:00 PM" formats.
    """

    list_of_valid_hrs = list()
    list_of_valid_mins = list()

    ########## VALIDATION ##########
    # Validate the argument passed.

    if len(time_string) < 3 and AMPM == "N/A":
        return print("The time that you've entered doesn't seem to be long enough to be recognized. \n Please enter an object with an hour value and minute value that are separated by a colon or an hour value with AM or PM. \n IE: 8:00, 8 AM, or 8 PM.")
    elif len(time_string) > 5:
        return print("The time that you've entered seems to be too long to be recognized. \n Please enter an object with an hour value and minute value that are separated by a colon or an hour value with AM or PM. \n IE: 8:00, 8 AM, or 8 PM.")

    if len(time_string) == 1:
        time_string += ":00"

    if ":" not in time_string:
        return print("You did not pass a valid time string! Please pass a time with hours and minutes separated by a ':'.")

    hrs = time_string.split(':')[0].zfill(2)
    mins = time_string.split(':')[1].zfill(2)
    AMPM = AMPM.upper()

    for hour in range(0, 23):
        list_of_valid_hrs.append(str(hour).zfill(2))
        list_of_valid_hrs.append("0")
    for minute in range(0, 59):
        list_of_valid_mins.append(str(minute).zfill(2))
        list_of_valid_mins.append("0")

    if hrs not in list_of_valid_hrs:
        return print("Your hour value is not valid! Please pass an hour value ranging from 0 to 23")
    if mins not in list_of_valid_mins:
        return print("Your minute value is not valid! Please pass a minute value ranging from 0 to 59")

    if AMPM not in ['AM', 'PM', 'A.M.', 'P.M.', 'N/A']:
        return print('Please make sure that your AM or PM argument is valid. \n IE: "AM", "PM", "am", "pm"')

    ########## VALIDATION ##########
    
    ########## CONVERSION ##########
    # Convert the time_string object.

    if AMPM == "N/A":
        #If this is NA then we're converting a 24hr time string to AMPM.
        if hrs in ['0', '00']:
            hrs = "12"
            AMPM = "AM"
        elif int(hrs) == 12:
            hrs = "12"
            AMPM = "PM"
        elif int(hrs) > 12:
            hrs = int(hrs)
            hrs = str(hrs-12)
            AMPM = "PM"
        else:
            AMPM = "AM"
        converted_time = (hrs + ":" + mins + " " + AMPM)
        return converted_time
    else:
        #If we have something that isn't NA then we should have an AM or PM value. We can do an AM/PM check at the start when we're getting args from the command line.
        if AMPM == "PM":
            #We should be in the PM so we need to add 12 hours to the time.
            hrs = int(hrs)
            hrs = str(hrs+12)
        elif int(hrs) == 12 and AMPM == 'AM':
            hrs = '00'
        converted_time = (hrs + ":" + mins)


    ########## CONVERSION ##########
    return(converted_time)

# Make sure this isn't being imported. If it is then variables will not be passed in through command line but as arguments in the coversion function.
if __name__ == "__main__":
    valid_args = False
    # Get inputs by using "sys.argv". sys.argv[0] = file name, sys.argv[1] = first arg, etc.
    if len(sys.argv) == 2:
        # Need to verify that the first two chars are ints, the third char is a ":" and the last two chars are ints.
        time_to_convert = sys.argv[1]
        AMPM = "N/A"
        print("Observed a 24hr format object.")
        valid_args = True
    elif len(sys.argv) == 3:
        # We should check in sys.argv[2] is AM/PM at some point.
        time_to_convert = sys.argv[1]
        AMPM = sys.argv[2]
        print("Observed an AMPM format object.")
        valid_args = True
    else:
        number_of_arguments = (len(sys.argv)-1)
        print("Please pass in at least 1 argument in a time format or 2 arguments in a time and AM/PM format. \nIE: 20:00 or 08:00 PM")
        print("The number of arguments you passed was/were: %s" % number_of_arguments)
        AMPM = "N/A"

    if valid_args:
        print(Time_Format_Conversion(time_to_convert, AMPM))