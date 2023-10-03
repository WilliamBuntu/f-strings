def cast_number(number_str):
    try:
        casted_number = float(number_str)
        print(f" Casting {repr(number_str)} to {casted_number}")    
    except :
        print(f"Couldn't cast{repr(number_str)} to a number")    

    

cast_number("12.23")