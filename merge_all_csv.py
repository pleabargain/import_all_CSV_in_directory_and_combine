# script that will open a folder and import all csv files and convert into a single csv file
# the data is comma separated
# the data is in the format of a table
# the data has a header row
       
# import pandas
# from distutils.filelist import FileList
import pandas as pd
#import os
import os
# create variables for input output files
input_folder = "PUT DIR PATH HERE"
output_folder = 'PUT DIR PATH HERE'

# create a list of files in the input folder
fileList = os.listdir(input_folder)
print(fileList)
# open each file in the list
for file in fileList:
    # check if file is valid csv
    try:
        df = pd.read_csv(input_folder + file)
        # if file is valid csv, append to output file
        df.to_csv(output_folder + 'output.csv', mode='a', index=False)
    except:
        print('File is not a valid csv: ' + file)
        continue
print(file)
df = pd.read_csv(input_folder + file)
df.to_csv(output_folder + 'consolidated.csv', mode='a', header=True)
# print statement to show that the script has completed
print('Script has completed')
