import datetime

def getEndDate():

    try:

        inputEndDate = input("Enter the end date (YYYY-MM-DD) ")

        endDate = datetime.datetime.strptime(inputEndDate, "%Y-%m-%d").date()

    except:

            if endDate <= begin_date:

                print("Error: Start date cannot be later than end date. Please enter the dates again.")
                print("")

    else:
    
            return endDate
    
getEndDate();
