#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
from datetime import datetime

def parse_month(month):
    month_dict = {
        'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07', 
        'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12' 
        
    }

    if month in month_dict:
        return month_dict[month]
    else: 
        return None

#parse_date function should return the date formated as MM/DD/YYYY
def parse_date(user_string):
    words = user_string.split()

    if len(words) >= 3:
        month = parse_month(words[0])
        day = words[1].rstrip(',').zfill(2)
        year = words[2]

        if month and day.isdigit() and year.isdigit():
            return f'{month}/{day}/{year}'
    return None

#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    user_string = input()
    formatted_date = parse_date(user_string)
    
    print(formatted_date)
    #Resubmitting