from Models.movie_review import Movie
from business.data_access_helper import DataAccessHelper

from tkinter import *
from tkinter.ttk import Combobox,Style, Treeview

class InsertFrame(Frame):
  
  def __init__(self, parent):
    #initialize the insert frame
    Frame.__init__(self, parent)

    #background color and style
    background = "#000C66"
    lbl_color = 'white'
    self.configure(bg=background) 
    

    self._parent = parent

    #set the insert window frame    
    self._insertWindow = Toplevel(self._parent)
    self._insertWindow.transient(parent)
    self._insertWindow.grab_set()
    self._insertWindow.configure(bg=background) 

    #The windows title and the size
    self._insertWindow.title("Insert Movie Review")
    self._insertWindow.geometry('350x300')
    
    #Define the string variables for the column
    self._movie_name = StringVar()
    self._movie_year = StringVar()
    self._movie_rating = StringVar()
    self._movie_genre = StringVar()
    self._movie_review = StringVar()
     
    #create the label for the name, year, rating, and genre with an entry field
    lbl_name = Label(self._insertWindow, text='Name:', font=('bold', 12), padx=5, pady=5, fg=lbl_color, bg=background)
    lbl_name.grid(row=0, column=0, sticky="W")

    entry_name = Entry(self._insertWindow, width=30, textvariable=self._movie_name)
    entry_name.grid(row=0, column=1)
    
    lbl_year = Label(self._insertWindow, text='Year:', font=('bold', 12), padx=5, pady=5, fg=lbl_color, bg=background)
    lbl_year.grid(row=1, column=0, sticky="W")

    entry_year = Entry(self._insertWindow, width=30, textvariable=self._movie_year)
    entry_year.grid(row=1, column=1)
    
    lbl_rating = Label(self._insertWindow, text='Rating:', font=('bold', 12), padx=5, pady=5, fg=lbl_color, bg=background)
    lbl_rating.grid(row=2, column=0, sticky="W")

    entry_rating = Entry(self._insertWindow, width=30, textvariable=self._movie_rating)
    entry_rating.grid(row=2, column=1)
    
    lbl_genre = Label(self._insertWindow, text='Genre:', font=('bold', 12), padx=5, pady=5, fg=lbl_color, bg=background)
    lbl_genre.grid(row=3, column=0, sticky="W")

    genres=('Horror', 'Action', 'Romance', 'Comedy', 'Science Fiction', 'Drama', 'Thriller', 'Documentary', 'Western', 'Musical', 'Crime', 'Fiction', 'Romantic Comedy', 'Music', 'War', 'Adventure', 'Epic')
    cbox_genre = Combobox(self._insertWindow, width=27, textvariable=self._movie_genre)
    cbox_genre.grid(row=3, column=1) 
    cbox_genre['values'] = sorted(genres)
    cbox_genre['state'] = 'readonly'  # normal    
    #cbox_genre.bind('<<ComboboxSelected>>', genre_selected)  

    lbl_review = Label(self._insertWindow, text='Review:', font=('bold', 12), padx=5, pady=5, fg=lbl_color, bg=background)
    lbl_review.grid(row=6, column=0, sticky="W")

    self._entry_review = Text(self._insertWindow, width=40, height=5, padx=5)
    self._entry_review.grid(row=7, column=0, columnspan=2, padx=8, sticky="W")
    
    insert_btn = Button(self._insertWindow, text='Add Review', width=12, command=self.btnClickInsertReview, fg=lbl_color, bg='#2ECC71')
    insert_btn.grid(row=10, column=0, sticky="W", padx=5, pady=15)

    cancel_btn = Button(self._insertWindow, text='Cancel', width=12, command=self.btnClickCancel, fg=lbl_color, bg='#E74C3C')
    cancel_btn.grid(row=10, column=1, sticky="E", padx=5, pady=15)       

    #self.pack()
    self.pack(fill="x", padx=20, pady=20)

      
  def btnClickInsertReview(self):
    try:
      new_review = Movie(0, 
                        self._movie_name.get(), 
                        int(self._movie_year.get()), 
                        float(self._movie_rating.get()), 
                        self._movie_genre.get(),
                        self._entry_review.get('1.0', 'end-1c'))
       
      DataAccessHelper().insertMovieReview(new_review)
      
      self._insertWindow.destroy()
      
      
      
    except Exception as e:
      print(e)
    
    finally:
      self._insertWindow.destroy()
      
      
  def btnClickCancel(self):
      self._insertWindow.destroy()

 

