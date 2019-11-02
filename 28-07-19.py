name = 'Suresh'
print(name[0])

#Lists

information = ['Aman', 27 , 'IMS Proschool']
print(information[0])

information[1] = 28
print (information[1])

#append function

information.append('Preet Vihar')
information.append(['India', 'Delhi'])
information.extend(['India', 'Delhi'])

#difference between append and extend.
name = []
name.append('Aman')
name.extend('Aman')
name.extend(28)

#pop function.
w = name.pop(0)

#Insert Function.
a = [1,2,4]
a.insert(2,3)

#2 -> index number , 3 -> item to be replaced.


#Slicing:

l = [10, 20, 30, 40]
l[1:3]


l[-1:-2]

#clockwise rotation:
l[-2:] + l[:2]

l[2:] + l[:2]


#Dictionary:

d = {'name' : 'Aman' ,
     'Age' : 27 ,
     'organization' : 'IMS'}
d['organization'] = 'Ericsson'
d['place'] = 'Noida'

#Multiple DIctionary

employee_details = {'name' : ['Aman', 'Suresh'],
                    'age' : {'Aman' : 27, 
                             'Suresh' : 28
                             },
                    'designation' : {'Manager' : 'Suresh',
                                     'PM' : 'Aman'
                                     },
                    }
employee_details['designation']['Manager']
employee_details['age']['Suresh']
