import csv
from tkinter.filedialog import askopenfilename
from tkinter import *
import os

fileA = 0   #initialize the file A
fileB = 0   #initialize the file B

def clicked():  #Define the file A
    global fileA
    fileA = askopenfilename()

def clicked2(): #Define the file B
    global fileB
    fileB = askopenfilename()

def conversion_and_compare():   #convert the file B and compare the file A and B
    fout = filedialog.asksaveasfilename(defaultextension=".csv")
    with open(fileA, 'r') as t1, open(fileB, 'r') as t2:

        #Conversion rules for the file B
        t2_converted = os.path.splitext(fileB)[0] + "_edited.csv"   #Create a staging file for the converted file B
        with t2, open(t2_converted, "w", newline='') as temp1:
            r = csv.reader(t2, delimiter=';')
            w = csv.writer(temp1, delimiter=';')
            for row in r:
                row[5] = row[5].replace('old_word1', 'new_word1')   #replace "old_word1" be "by_word1" in the 6th column
                row[1] = row[1].replace('old_word2', 'new_word2')   #replace "old_word2" be "by_word12" in the 2th column
                w.writerow(row)

        # compare the converted file B to the file A
        with open(t2_converted, "r") as temp2:
            fileone = t1.readlines()
            filetwo = temp2.readlines()
            with open(fout, 'w', newline='') as outFile:
                for line in filetwo:
                    if line not in fileone:
                        outFile.write(line)

        os.remove(t2_converted) #remove the staging fileB_edited.csv

window = Tk()   #Create a GUI
window.geometry('350x250')
window.title("Compare CSV file")
Label(text = "Compare 2 CSV files", bg="grey", width="350", height="2", font=("Calibri", 13)).pack()
lbl = Label(window, text="Select the path of the file A:").pack()
btn = Button(window, text="File A Path", width="30", height="2", command=clicked).pack()    #Button to launch the function clicked
lbl2 = Label(window, text="Select the path of the file B:").pack()
btn2 = Button(window, text="File B Path", width="30", height="2", command=clicked2).pack()  #Button to launch the function clicked2
lbl2 = Label(window, text="").pack()
btn2 = Button(window, text="Compare files A and B", width="30", height="2", command=conversion_and_compare).pack() #Button to launch the function conversion_and_compare
window.mainloop()


