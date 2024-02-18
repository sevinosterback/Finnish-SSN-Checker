from datetime import datetime
ssn = input("Enter a Finnish Social Security Number:")
date = ssn[:6]
century = ssn[6]
unique = ssn[7:10]
checker = ssn[10]
checker_fixed = int(date + unique) % 31
century_checker = "+-UVWXYABCDEF"
check_list = "0123456789ABCDEFHJKLMNPRSTUVWXY"

if len(ssn) != 11:
   print("Invalid length. The length has to be 11 characters.")
elif century not in century_checker:
   print("Invalid SSN")
else:
   try:
       date_obj = datetime.strptime(date, "%d%m%y")
   except ValueError:
       print("Invalid SSN")
   else:
       if not (2 <= int(unique) <= 899):
           print("Invalid SSN")
       elif checker != check_list[checker_fixed]:
           print("Invalid SSN")
       else:
           print("Valid SSN.")
    
            
    

