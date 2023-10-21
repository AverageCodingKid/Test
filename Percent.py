#Remove errors
try:
    #Data
    original = int(input("Enter the number that you would like to find the percentage of: "))
    percent = int(input("Enter the percentage: % "))
    print(original * percent / 100)
    inc = str(input("Would you like to find the increased value? Y|N : ")).lower()
    
    #More Data
    if inc == "y".lower():
        print(original * percent / 100 + original)
    #If answer is no (or anything other than y), print(Goodbye and end code)
    else:
        print("Goodbye!")

#Remove any errors
except ValueError:
    print("🔴 Error Code 1: Invalid Data Type, use integers only 🔴") 