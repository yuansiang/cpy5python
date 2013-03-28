#filename: q7_generate_payroll.py
#author: Yuan Siang
#created: 25/1/13
#modified: -
#description: Generates payroll
#Practical 01.Q7

#main
#prompt for input of information
name = str(input("Enter name: "))
hrs = int(input("Enter number of hours worked weekly: "))
rate = float(input("Enter hourly pay rate: "))
cpfrate = float(input("Enter CPF contribution rate(%): "))

#calculate gross pay
gross = rate * hrs

#calculate CPF contribution
#check if CPF contribution is capped at 100%
if (0<=cpfrate<=100):
    cpf = gross * (cpfrate/100)
    #calculate net pay
    netpay = gross - cpf

    #print results
    print("")
    print("Payroll statement for " + name)
    print("Number of hours worked in week: " + "{0:0.0f}".format(hrs))
    print("Hourly pay rate: $" + "{0:0.2f}".format(rate))
    print("Gross pay = $" + "{0:0.2f}".format(gross))
    print("CPF contribution at " + "{0:0.0f}".format(cpfrate) + "% = $" + "{0:0.2f}".format(cpf))
    print("Net pay = $" + "{0:0.2f}".format(netpay))

else:
    print("INVALID! Restart application to continue.")



          
