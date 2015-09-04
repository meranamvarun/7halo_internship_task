#!/usr/bin/python

#Module to use MySql with python
import MySQLdb

#Simplejson ---> dump a dict at simplejson and get back json
import simplejson

#model ---> view 
def edit_view_html(text):
    file=open("view.html",'w')
    file.write('Content-type:application/json; charset=utf-8\n\n'+text)
    file.close()

#takes in the id value and plays around with it... creates view as per the id value send in by the user 
def get_request(intern_id):
    output={}
    data={}

    try:
        db = MySQLdb.connect(host="localhost", # your host, usually localhost
        user="root", # your username
        passwd=")(*&^%$#@!", # your password ... 
        db="7halo") # name of the data base ... .
            
        cur = db.cursor() 
	cur.execute("SELECT name from interns where id=%s",str(intern_id))

       
    except MySQLdb.Error as err: #In case the user enters wrong passwd ,username or db name,will throw up a error page at user at the view.
        edit_view_html(str(err))
            
    else:
	for name_tuple in cur:
            name=name_tuple[0]

	try:
            if name:      #checking if there exsist a student for particular id
		output["success"]=True      
                data["name"]=name
                output["data"]=data
                json_output=simplejson.dumps(output)  #dict to json conversion
                edit_view_html(json_output)#feeding output to view 
	except NameError:
	    output["success"]=False  
	    output["data"]={}
	    json_output=simplejson.dumps(output)
            edit_view_html(json_output)
	     

               
    
        
        
            
  
        
        
