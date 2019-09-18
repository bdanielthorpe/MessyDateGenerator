import numpy as np

import random

month_dict = {
    "january": 31
    , "february": 28
    , "march": 31
    , "april": 30
    , "may": 31
    , "june": 30
    , "july": 31
    , "august": 31
    , "september": 30
    , "october": 31
    , "november": 30
    , "december": 31
    , "jan": 31
    , "feb": 28
    , "mar": 31
    , "apr": 30
    , "jun": 30
    , "jul": 31
    , "aug": 31
    , "sep": 30
    , "sept": 30
    , "oct": 31
    , "nov": 30
    , "dec": 31
    , "jan.": 31
    , "feb.": 28
    , "mar.": 31
    , "apr.": 30
    , "jun.": 30
    , "jul.": 31
    , "aug.": 31
    , "sep.": 30
    , "sept.": 30
    , "oct.": 31
    , "nov.": 30
    , "dec.": 31
}

month_dict_2 = { 1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31 }

# Generate ordinal:
gen_ordinal = lambda n: "%d%s"%(n,{1:"st",2:"nd",3:"rd"}.get(n if n<20 else n%10,"th"))

def gen_year():
    year = random.choice( [ "", "19", "20" ] )
    if year == "":
        year = random.choice([ ""
                             , str( np.random.randint(50,100) )
                             , "0"+str( np.random.randint(0,10) )
                             , str( np.random.randint(10,25) )
                            ])
    elif year == "19":
        year += str( np.random.randint(50,100) )
    else:
        year += random.choice( [ "0"+str( np.random.randint(0,10) ), str( np.random.randint(10,25) ) ] )
    return year
        
def gen_date_1():
    month = str( random.choice( list( month_dict ) ) )
    day = np.random.randint( 1, month_dict[month] )
    if random.choice([True,False]):
        day = gen_ordinal( day )
    day = str( day )
    year = gen_year()
    day_position = random.choice( [1,2] )
    delimiter = random.choice( [" ", " ", " ", "-"])
    if day_position == 1:
        if year:
            date = day + delimiter + month + delimiter + year
        else:
            date = day + delimiter + month
    else:
        if year:
            date = month + delimiter + day + delimiter + year
        else:
            date = month + delimiter + day
    return date

def gen_date_2():
    month = np.random.randint(1,13)
    day = np.random.randint( 1, month_dict_2[month] )
    month = str( month )
    day = str( day )
    year = gen_year()
    delimiter = random.choice( ["-",".","/" ] )
    month_index = random.choice( [1,2] )
    if month_index == 1:
        if year:
            date = month + delimiter + day + delimiter + year
        else:
            date = month + delimiter + day
    else:
        day_index = random.choice( [1,3] )
        if day_index == 1:
            if year:
                date = day + delimiter + month + delimiter + year
            else:
                date = day + delimiter + month
        else:
            if year:
                date = year + delimiter + month + delimiter + day
            else:
                date = month + delimiter + day
    return date

def gen_date():
    date_type = random.choice( [1,2] )
    if date_type == 1:
        date = gen_date_1()
    else:
        date = gen_date_2()
    return date

def gen_date_list( n ):
    return [ gen_date() for i in range(n) ]