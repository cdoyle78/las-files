import re
import os


dirname = input('Enter directory path containing the files you would like to rename: ')

try:
    os.chdir(dirname)  #change directory to path specified

except:
    print('Directory cannot be opened') #bad path
    exit()

        
for filename in os.listdir():               #iterate through files in directory
    
    if filename.lower().endswith(".las"):
        count = 0
        try:
            fhand = open(filename)           #open *las file
        except:
            print('File cannot be opened')
            exit()
        for line in fhand:                  #iterate through lines in las file
            if 'UWI' in line:
                uwi = re.sub("[^0-9]", "", line) #extract UWI (numbers only) from las file
                newfname = uwi + '.las'             #create new filename with UWI
                while os.path.isfile(newfname):     #check to make sure new file name is unique. If not, add a count.
                    count += 1
                    newfname = uwi + '_' + str(count) + '.las'
        fhand.close()
        if count == 0:
            newfname = uwi + '.las'
        else:
            newfname = uwi + '_' + str(count) + '.las'
           
        os.rename(filename, newfname)                #rename file with new file name
        print(filename + '  has been changed to: ' + newfname)       
    else:
        continue




