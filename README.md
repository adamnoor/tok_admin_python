# tok_admin_python

README

Title: tok_admin_python

Author: Adam Noor

Date Published: October 10, 2019

License: MIT


This is the CRUD application for the Theory of Knowledge app published on the Play Store.  Below are the requirements to make this compile for anyone interested using this code.  The application is published under an MIT license.  

Steps to run program:

Prerequisites:

Python 3
Pip
firebase-admin library (use pip to install into the project)
Firebase Project with a collection called “resources”
JSON file holding the private key for the firebase project named serviceAccountKey.json (put this in the folder)



To run (this is really for Aly but should work for everyone):

1. Go to Applications >> Python 3.7 >> idle
2. Go to file >> open
3. Select main.py from the tok_admin_python folder
4. Go to run >> run module (if you do not see “run” in the toolbar, select the main.py file and it should appear)

Relevant Files:

updated_data.csv

This file is used to update the database.  Any resource that is the current date or before will be added to the database.  Any resources with dates in the future will not be added to the database.

backup_data_date_time

This file is created every time the Backup button is selected.  If the button is selected within the same minute then the backup file will overwrite but if it is done in a new minute a new backup is created.

serviceAccountKey.json

This file is the key used to connect to the Firebase database.  It should not be included in any file sharing.

main.py

This is the python script that has the code to run the admin panel.  It’s written in Python 3 and uses tkinter for the GUI.



