
Rotten Potatoes
ACIT 2911 Group 10

Created by: Rai, Brian, Riley, Matthew, RJ, Vince


Rotten Potatoes is a simple desktop GUI application with C.R.U.D capabilities. Users can search movie reviews by name, year, rating, and key words. 


Project Structure:

Business directory 
responsible for passing data from UI to database. Acts as middle man passing data through frames

DB directory 
responsible for backend SQLite commands to interact with database

Models directory 
responsible for handling logic for attributes of movie reviews stored

Resource files directory
stores Rotten Tomatoes logo img

Tests directory
	responsible for storing tests for movie review model, and for db
	
UI directory
responsible for displaying screens to users and collecting input. There are 3 different frames - main frame, insert frame, update frame


CircleCI directory
stores config.yml file that is responsible for running unit tests on each push 


app.py
responsible for running our program - initializes and passes a Tkinter object to mainframe in UI

conftest.py
file needed for CircleCI integration to work


Technologies Used:
Python
Tkinter
SQLite
Pyinstaller
CircleCI
GitHub

NOTE: Only add dependencies once a virtual environment has been created, as to not interfere with global packages. Dependencies (install using 'pip install x', where x is the name of the library listed below):

Dependencies Required:
Pillow
Pytest - if you want to run unit tests


Installation

We created an EXE for this project so users do not have to download Python and the dependencies needed. The EXE will not be part of our final deliverable - it was only for the presentation. We are submitting the source code for our project.

The following instructions will explain how to run the application from the source code (no EXE).

	Procedure
After installing the above programs and dependencies:
Open Windows terminal in the root directory of the application
Execute “python app.py” - this will start with application
To view movie reviews in the database, click on the “Search” button beside “Search by name:”

*Windows OS needed. Desktop app has not been tested on any other OS*







Features - C.R.U.D

Select all reviews - Users can view all entries in the database.

Search - Users can search movie reviews entries by name, rating, and year.

Select review - Users can click on a single movie review entry to select it - will be highlighted

Add review (green button) - Users can add movie review entries to the database.

Remove review (red button) - Users can remove movie review entries from the database.

Update review (yellow button) - Users can update movie reviews in the database.

Clear fields (button) - User can clear inputs given for all 3 different text boxes (search by rating, year, name)

Exit (button) - User can exit application


*To REMOVE or UPDATE movie review entries, users must SELECT the intended movie review first, and then click the corresponding button according to their desired action*

If users do not SELECT movies before clicking UPDATE review or DELETE review, a helpful error message will be presented in the GUI specifying how to correctly complete the action.







