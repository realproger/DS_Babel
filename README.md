## Part I ```SQL``` <i>to</i> ```CSV```.
**We will start with the ```SQL``` format to ```CSV```**
> **Your function will receives a ```connection``` (an ```sqlite3``` object from import sqlite3 which will be already connected), ```table_name```.
Your function will transform the content of ```table_name``` to ```CSV``` format and return it. (Columns separated by ```comma``` and rows separated by ```\n```)_**

---


## Part II ```CSV``` <i>to</i> ```SQL```
> **Your function will transform the content to ```SQL``` format by creating the ```table_name``` and adding each row._**
---
## Part III
> **a) You will use your function to convert the <a href="https://storage.googleapis.com/qwasar-public/track-ds/list_volcano.csv">```list of all volcanos```</a> from ```CSV``` to ```SQL```.**

> **b) You will use your function to convert the <a href="https://storage.googleapis.com/qwasar-public/track-ds/all_fault_line.db">```list of all fault lines```</a> from ```SQL``` to ```CSV```.
Data are inside the table named: fault_lines.**
---
## Technical Specifications
> **1# sql_to_csv will receive two strings as parameters and return a string.
the database is a filename where sql_to_csv will fetch the information.
table_name is the table from the database file to fetch the information.
your return value will be a CSV formatted string:
"ColA,ColB,ColC\n1,2,3\n4,5,6\n"**

> **2# csv_to_sql will receive three strings as parameters and return nothing.
csv_content is a StringIO following the CSV format.
the database is a filename where csv_to_sql will push the information.
table_name is the table from the database file to insert the data.**
