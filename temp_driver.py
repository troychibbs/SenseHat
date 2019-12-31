from sense_emu import SenseHat
from time import sleep
import csv

read_count = 0
sense = SenseHat()

#returns int temp as string
def get_temp_string ():
    temp = sense.get_temperature()
    return str(temp)

#open file to write temp data
with open('temp_data.csv', mode = 'w') as temp_file:
    #Create csvwriter object and write header
    temp_writer = csv.writer(temp_file, delimiter = ',', quotechar = "'", quoting = csv.QUOTE_MINIMAL)
    temp_writer.writerow(["Temperature", "Reading #"])
    
    while read_count != 5:
        
        #retrieve temp and increment count
        read_count += 1
        temp = get_temp_string()
        
        #print temp to console and set LED matrix
        print(temp)
        sense.show_message(temp + " degrees" , text_colour = [0, 255, 0], scroll_speed = 0.025)
        
        #write line of data to .csv file
        temp_writer.writerow([temp, read_count])
        
        
        #freeze loop for 2 seconds
        sleep(2)
temp_file.close()







