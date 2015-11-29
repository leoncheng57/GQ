import re
import regex


#To test each functions
if __name__=='__main__':                                                       
    input = raw_input("Enter some names: ")                                    
    result_name = re.findall(regex.name, input)
    
    input = raw_input("Enter some dates: ")
    result_date = re.findall(regex.date, input)
    

    print("Name results: ")
    print result_name

    print("Date results: ")
    print result_date
