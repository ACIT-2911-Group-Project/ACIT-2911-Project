from ui.insert_frame import InsertFrame
from business.data_access_helper import DataAccessHelper
from db.db_manager import DatabaseManager
from Models.movie_review import Movie

from tkinter import *
from tkinter.ttk import Combobox, Treeview

selected_movie_review = ""

class MainFrame(Frame):
  
  def __init__(self, parent):
    #Initialize the main frame
    Frame.__init__(self, parent)
    
    self._parent = parent    
    #Define string variables for text entry fields
    self._movie_name_text = StringVar()
    self._movie_year_text = StringVar()
    self._movie_rating_text = StringVar()

    self.pack()
    
    #Search by Movie name
    #Create a label, an entry field, and a button      
    lbl_search = Label(self, text='Search by name:', font=('bold', 12), pady=15)
    lbl_search.grid(row=0, column=0, sticky="W")

    moviename_search_entry = Entry(self, width=60, textvariable=self._movie_name_text)
    moviename_search_entry.grid(row=0, column=2)
    
    search_btn = Button(self, text='Search', width=12, command=self.btnClickSearchByName)
    search_btn.grid(row=0, column=6)       

    #Search by Movie year
    #Create a label, an entry field, and a button
    year_label = Label(self, text='Search by year:', font=('bold', 12), pady=15)
    year_label.grid(row=1, column=0, sticky="W")
    
    year_entry = Entry(self, textvariable=self._movie_year_text)
    year_entry.grid(row=2, column=0)
    
    search_btn2 = Button(self, text='Search', width=12, command=self.btnClickSearchByYear)
    search_btn2.grid(row=3, column=0)
    
    #Search by Movie rating
    #Create a label, an entry field, and a button
    rating_label = Label(self, text='Search by rating:', font=('bold', 12), pady=15)
    rating_label.grid(row=1, column=6, sticky="W")
    
    rating_entry = Entry(self, textvariable=self._movie_rating_text)
    rating_entry.grid(row=2, column=6)
    
    search_btn3 = Button(self, text='Search', width=12, command=self.btnClickSearchByRating)
    search_btn3.grid(row=3, column=6)
    
    #Create a new frame for the Insert, Update and Delete buttons
    # frame_btns = Frame(self)
    # frame_btns.grid(row=4, column=0, columnspan=5, pady=40)

    add_btn = Button(self, text='Add Review', width=12, padx=15, command=self.addReview)
    add_btn.grid(row=8, column=0, sticky="W", padx=15)

    remove_btn = Button(self, text='Remove Review', width=12, padx=15, command=self.deleteReview)
    remove_btn.grid(row=8, column=1, padx=15)

    update_btn = Button(self, text='Update Review', width=12, padx=15, command=self.updateReview)
    update_btn.grid(row=8, column=2, sticky="E", padx=15)

    # clear_btn = Button(frame_btns, text='Clear Input', width=12, command=self.clearText)
    # clear_btn.grid(row=0, column=3)      
    
    #Create a frame for the results
    frame_reviews = Frame(self)
    frame_reviews.grid(row=10, column=0, columnspan=11, rowspan=10, pady=40)

    #Create a column for the result
    columns = ['id', 'Name', 'Year', 'Rating', 'Genre', 'Review']
    self._movie_tree_view = Treeview(frame_reviews, columns=columns, show="headings")
    self._movie_tree_view.column("id", width=30)
    for col in columns[1:]:
      self._movie_tree_view.column(col, width=130)
      self._movie_tree_view.heading(col, text=col)
          
    #Create the list of the tree view of the movie     
    self._movie_tree_view.bind('<<TreeviewSelect>>', self.select_movie)
    self._movie_tree_view.pack(side="left", fill="y")
    scrollbar = Scrollbar(frame_reviews, orient='vertical')
    scrollbar.configure(command=self._movie_tree_view.yview)
    scrollbar.pack(side="right", fill="y")
    self._movie_tree_view.config(yscrollcommand=scrollbar.set)          

          
  def btnClickSearchByName(self):
    #Function to seach for the movie by name
    movie_name = self._movie_name_text.get()      
    #movie_reviews = DataAccessHelper().queryByMovieName(movie_name)
    if not movie_name:
      movie_reviews = DataAccessHelper().queryAll()
    else:
      movie_reviews = DataAccessHelper().queryByMovieName(movie_name)
        
    self.populate_list(movie_reviews)
      
  def btnClickSearchByYear(self):
    #Function to seach for the movie by name
    movie_year = int(self._movie_year_text.get())  
    movie_reviews = DataAccessHelper().queryByMovieYear(movie_year)
    self.populate_list(movie_reviews)
    
  def btnClickSearchByRating(self):
  #Function to seach for the movie by name
    movie_rating = int(self._movie_rating_text.get())  
    movie_reviews = DataAccessHelper().queryByMovieRating(movie_rating)
    self.populate_list(movie_reviews)

  def populate_list(self, movie_reviews):
    #Display the list of movies from the tree view
    self.clear_list()
        
    for row in movie_reviews:
        self._movie_tree_view.insert('', 'end', values=row)
          
  def clear_list(self):
    #Clear the list of the movie tree view
    for i in self._movie_tree_view.get_children():
        self._movie_tree_view.delete(i)
            
  def select_movie(self, event):
    #Select the movie
    global selected_movie_review
    index = self._movie_tree_view.selection()[0]
    selected_movie_review = self._movie_tree_view.item(index)["values"]
    print(selected_movie_review[0])
      
  def addReview(self):
    #Add review of the movie
    dlg = InsertFrame(self._parent)    
    if dlg is not False:
      movie_reviews = DataAccessHelper().queryAll()
      self.populate_list(movie_reviews)
    
  def deleteReview(self):
    #Delete the review
    pass

  def updateReview(self):
    #Update the review
    pass
