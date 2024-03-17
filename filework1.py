"""data ={
    "name":"dips",
   " roll" :"10",
    "subject" :["data science", "web development","cloud computin
}

import json
with open ("data.json","w") as f:
   print( json.dump(data,f) ) # to perform write operation

with open ("data.json","r") as f:
    data1= ( json.load(f) )  #to perform read operation
    print(data1)

print(data1['subject'][2]);

# to create a csv file....write and read data from file

"""
import csv

data = [["roll","name","email"],
        [ "10","dips","dipi@gmail.com"],
        [ "11","vidya","vidya@gmail.com"],
        [ "14","janhavi","janhavi@gmail.com"]
         ]

with open("data.csv","w") as f:
    writer= csv.writer(f)  # writerrow is used to write every row 
    
    for i in data:
      print(writer.writerrow(i));

with open("data.csv","r") as f:
   read_data =csv.reader(f)

for i in read_data:
   print(i) ;