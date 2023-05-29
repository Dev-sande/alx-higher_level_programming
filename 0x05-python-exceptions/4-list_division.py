#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            
            try:
                dividend = float(dividend)
            except ValueError:
                raise TypeError("wrong type")
            
            try:
                divisor = float(divisor)
                if divisor == 0:
                    raise ZeroDivisionError("division by 0")
            except ValueError:
                raise TypeError("wrong type")
            
            result.append(dividend / divisor)
        
        except IndexError as e:
            print("out of range")
            result.append(0)
        except ZeroDivisionError as e:
            print("division by 0")
            result.append(0)
        except TypeError as e:
            print("wrong type")
            result.append(0)
        finally:
            pass
        
    return result

