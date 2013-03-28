#filename: q8_convert_milliseconds.py
#author: Yuan Siang
#created: 22/2/13
#modified: -
#description: Convert into milliseconds to hours minutes seconds
#Practical 03 Q8

#define function convert_ms(n)
def convert_ms(n):
    secs_raw = n // 1000
    mins_raw = n // 60000
    hrs = n // 3600000 #find n in seconds, minutes and hours respectively

    secs = secs_raw - mins_raw*60 #convert it into hr:min:secs format
    mins = mins_raw - hrs *60
    print(str(hrs) + ":" + str(mins) + ":" + str(secs))

#main
n = int(input("Enter time in milliseconds: ")) #prompt for n
convert_ms(n)
            
