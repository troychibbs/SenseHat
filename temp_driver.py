from sense_emu import SenseHat
from time import sleep
import csv
from datetime import datetime
# You can change sense_emu to sense_hat for physical SenseHat hardware use
sense = SenseHat()

#method to return double temp as string
def get_temp_string ():
    temp = sense.get_temperature()
    return str(temp)

#Formats date to set as file name
date = datetime.now()
formatted_date = date.strftime("%m_%d_%Y")

#open file to write temp data
with open(formatted_date + '_readings' + '.csv', mode = 'w') as temp_file:
    
    #Create csvwriter object and write header
    temp_writer = csv.writer(temp_file, delimiter = ',', quotechar = "'", quoting = csv.QUOTE_MINIMAL)
    temp_writer.writerow(["Temperature", "Time"])
    
    #iterates for 5 readings
    read_count = 0
    while read_count != 5:
        
        #retrieve temp and increment count
        read_count += 1
        temp = get_temp_string()
        
        #print temp to console and set LED matrix
        print(temp)
        sense.show_message(temp + " degrees" , text_colour = [0, 255, 0], scroll_speed = 0.025)
        
        #take time and write line of data to .csv file
        date = datetime.now()
        temp_writer.writerow([temp, date.strftime("%H:%M:%S")])
        
        
        #freeze loop for 2 seconds
        sleep(2)
        
temp_file.close()







