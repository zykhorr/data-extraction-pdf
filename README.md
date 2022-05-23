# Extract data from PDF
Extract the data from PDF file format

#Installation
You are required to install few libraries in order to run the tool. 
Copy and paste the command below to install the required libraries.

## 
```pip
pip3 install io
```
## 
```pip
pip3 install pdfminer
```
## 
```pip
pip3 install pdfminer.six
```
## 
```pip
pip3 install lxml
```
##
```pip
pip3 install re
```
##
```pip
pip3 install pandas
```

#Demonstration
Firstly, after converted the pdf into html, you need to check for the location of the data which you want to extract. For the scenario of this demonstration, I would like to extract the data from invoice section. Hence, the location of the data would be left1: 420, left2: 420, top1: 110, top2: 179 
[alt enter data page](img/htmlheaders.png)

Those selected range is to extract the data as headers and put inside a list, the next we need to do is to select the position of the data value, which is left1: 478, left2: 478, top1: 111, top2: 111
[alt enter data page](img/htmlvalues.png)

Those extracted data will be put into a list too.

After done the headers and values selection, then we will need to use the function (split_remove) to remove 'null' from the extracted data list.

The next step is to form a dataframe and put those processed headers and values into a table.

Last but not least, export the table into a csv file format.