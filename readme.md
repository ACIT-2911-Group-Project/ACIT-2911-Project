
# ![GitHub Logo](./resource_files/Potatoe.PNG)

## ACIT 2911 Group 10
Created by: Rai, Brian, Riley, Matthew, RJ, Vince


## **Description**
Rotten Potatoes is a simple desktop GUI application with C.R.U.D capabilities. Users can search movie reviews by name, year, rating, and key words. 

## **Project Structure:**

* ### **Business directory** 
    responsible for passing data from UI to database. Acts as middle man passing data through frames

* ### **DB directory** 
    responsible for backend SQLite commands to interact with database

* ### **Models directory** 
    responsible for handling logic for attributes of movie reviews stored

* ### **Resource files directory**
    stores Rotten Tomatoes logo img

* ### **Tests directory**
	responsible for storing tests for movie review model, and for db
	
* ### **UI directory**
    responsible for displaying screens to users and collecting input. There are 3 different frames - main frame, insert frame, update frame


* ### **CircleCI directory**
    Stores config.yml file that is responsible for running unit tests on each push 


* ### **app.py**
    responsible for running our program - initializes and passes a Tkinter object to mainframe in UI

## **Technologies Used**

* Pytest
* VSCode
* Tkinter
* SQLite
* Pyinstaller
* CircleCI
* GitHub

NOTE: Only add dependencies once a virtual environment has been created, as to not interfere with global packages. Dependencies (install using 'pip install x', where x is the name of the library listed below):

## **Dependencies Required:**
* Pillow
* Pytest - if you want to run unit tests

## **Installation**

We created an EXE for this project so users do not have to download Python and the dependencies needed. The EXE will not be part of our final deliverable - it was only for the presentation. We are submitting the source code for our project.

The following instructions will explain how to run the application from the source code (no EXE).

### **Procedure**
* After installing the above programs and dependencies:
    1. Open Windows terminal in the root directory of the application
    2. Execute “python app.py” - this will start with application
    3. To view movie reviews in the database, click on the “Search” button beside   “Search by name:”
    
    *Windows OS needed. Desktop app has not been tested on any other OS*





## **Features - C.R.U.D**

* **Select all reviews** - Allows the user to view all the movies registered in the application.

* **Search** - the user can search movies that they want to read or write reviews by names, rating, and year.

* **Add reviews** (in green) - Allows the user to see their own movie reviews later on.

* **Remove reviews (in red)** - Allows the user to be able to clean up their own list of movie reviews.

* **Update reviews (in yellow)** - Allows the user to match certain movie reviews towards their own honest opinion and interests.

* **Clear fields** - Allows users to clear input from the search bar.

* **Exit** - Allows users to be able to exit the application.

---
__*To REMOVE or UPDATE movie review entries, users must SELECT the intended movie review first, and then click the corresponding button according to their desired action*__

__If users do not SELECT movies before clicking UPDATE review or DELETE review, a helpful error message will be presented in the GUI specifying how to correctly complete the action.__






