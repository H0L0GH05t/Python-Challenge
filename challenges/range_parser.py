"""
Implement a function that returns an inclusive list of numbers
from a Python slice style string with 1 <= N <= 10.

    '1'      # returns [1]
    ':7'     # returns [1, 2, 3, 4, 5, 6, 7]
    '8:'     # returns [8, 9, 10]
    '2:5'    # returns [2, 3, 4, 5]
    'a:b'    # returns 'Range values must be integers!'
    '1:2:3'  # returns 'Only two values allowed!'

"""
import re


def range_parser(s):
    # create list to hold numbers
    range_list = []
    
    # use regex to find values in given range
    range_re = r'^(\d*):(\d*)\Z'
    
    # count number of ':' in s
    if s.count(':') == 1:
        
        # match s to regex
        match_obj = re.match(range_re, s)
        if match_obj:
            match_groups = match_obj.groups(default=0)
            
            # convert numbers parsed from s to type int
            num1 = match_groups[0]
            num2 = match_groups[1]
            
            if num1 == '' or int(num1) == 0:
                # set to 1, beginning of possible range 
                num1 = 1
            elif num2 == '' or int(num2) == 0:
                # set to 10, end of possible range
                num2 = 10

            for num in range(int(num1), int(num2)+1):
                range_list.append(num)
            
        else:
            # input values were not integers
            return 'Range values must be integers!'
        
    elif s.count(':') > 1:
        # if there's more than 1 ':' return message
        return 'Only two values allowed!'
    else:
 
        try:
            num = int(s)
        except AttributeError:
            return 'Range values must be integers!'
            
        range_list.append(num)
    
    return range_list
