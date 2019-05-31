This file is written the 31st of May 2019. This file is organized as below:

1.Pre-requisite
2.Compare 2 CSV files script
3.Compare 2 CSV files with conversion rules script
4.How to read the report file
5.Contact

### 1.Pre-requisite

- This script has been written to work on Windows using Python 3.7
- The script use the modules csv, tkinter and os

### 2.Compare 2 CSV files script

The goal of this test script is to compare 2 csv files and create a report file with the result of the comparaison.

The test script is composed of 3 functions:
- clicked : define file A
- clicked2 : define file B
- conversion_and_compare : conver the file B according to conversion rules and compare the file A to the converted file B

### 3.Compare 2 CSV files with conversion rules script

The goal of this script is to clean 2 csv files by applying conversion rules, compare the 2 files and create a report file with the result of the comparaison.

The script contains a basic GUI created via the module tkinter

#### Get the Data
The script asks for the path of the file A and the file B that need to be compared.
The path of the files are stored in the variable fileA (reference object) and fileB (difference object).

#### Conversion
This section of the script needs to be updated according to your needs.
Some examples of conversion/data cleaning are by default in this section.

The script import the file B (reference object) perform the conversion rules defined for each object and create a new file

#### Compare

THe script compare each row between the file A and the converted file B and store the row that are different in a new file.

### 4.How to read the report file

The report file contains the rows that are different between the file A and the converted file B

### 5.Contact

Alexandre DOUDELET - adoudelet@protonmail.com
