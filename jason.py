#!/usr/bin/python
#import the model
from model import get_request

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
id = form.getvalue('id')


get_request(id)

file=open("view.html","r")

html_data=file.read()
html_line_data=html_data.split("\n")

for html_line in html_line_data:
    print html_line

