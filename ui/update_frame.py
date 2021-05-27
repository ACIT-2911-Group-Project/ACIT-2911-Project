from Models.movie_review import Movie
from business.data_access_helper import DataAccessHelper

from tkinter import *
from tkinter.ttk import Combobox, Treeview


class UpdateFrame(Frame):
  
  def __init__(self, parent_, movie_):
    
    Frame.__init__(self, parent_)
    
    #color styling
    background = "#000C66"
    lbl_color = 'white'
    self.configure(bg=background) 
    
    self._movie = movie_
    self._parent = parent_
        
    self._updateWindow = Toplevel(parent_)
    self._updateWindow.transient(parent_)
    self._updateWindow.grab_set()    
    self._updateWindow.configure(bg=background)
    
    self._updateWindow.title("Update Movie Review")
    #self._updateWindow.geometry('350x300')
    self.center_window(350,300)
    
    self._movie_name = StringVar()
    self._movie_year = StringVar()
    self._movie_rating = StringVar()
    self._movie_genre = StringVar()
    self._movie_review = StringVar()
    
    #name entry
    lbl_name = Label(self._updateWindow, text='Name:', font=('bold', 12), padx=5, pady=5, fg=lbl_color, bg=background)
    lbl_name.grid(row=0, column=0, sticky="W")

    entry_name = Entry(self._updateWindow, width=35, textvariable=self._movie_name)
    entry_name.grid(row=0, column=1, sticky="W")
    
    #year entry
    lbl_year = Label(self._updateWindow, text='Year:', font=('bold', 12), padx=5, pady=5, fg=lbl_color, bg=background)
    lbl_year.grid(row=1, column=0, sticky="W")

    entry_year = Entry(self._updateWindow, width=35, textvariable=self._movie_year)
    entry_year.grid(row=1, column=1, sticky="W")
    
    #rating entry
    lbl_rating = Label(self._updateWindow, text='Rating:', font=('bold', 12), padx=5, pady=5, fg=lbl_color, bg=background)
    lbl_rating.grid(row=2, column=0, sticky="W")

    entry_rating = Entry(self._updateWindow, width=35, textvariable=self._movie_rating)
    entry_rating.grid(row=2, column=1, sticky="W")
    
    #genre entry
    lbl_genre = Label(self._updateWindow, text='Genre:', font=('bold', 12), padx=5, pady=5, fg=lbl_color, bg=background)
    lbl_genre.grid(row=3, column=0, sticky="W")

    genres=('Horror', 'Action', 'Romance', 'Comedy', 'Science Fiction', 'Drama', 'Thriller', 'Documentary', 'Western', 'Musical', 'Crime', 'Fiction', 'Romantic Comedy', 'Music', 'War', 'Adventure', 'Epic')
    sorted_genres = sorted(genres)
    cbox_genre = Combobox(self._updateWindow, width=32, textvariable=self._movie_genre)
    cbox_genre.grid(row=3, column=1, sticky="W") 
    cbox_genre['values'] = sorted_genres
    cbox_genre['state'] = 'readonly'  # normal    
    #cbox_genre.bind('<<ComboboxSelected>>', genre_selected)  

    lbl_review = Label(self._updateWindow, text='Review:', font=('bold', 12), padx=5, pady=5, fg=lbl_color, bg=background)
    lbl_review.grid(row=6, column=0, sticky="W")

    self._entry_review = Text(self._updateWindow, width=40, height=5)
    self._entry_review.grid(row=7, column=0, columnspan=2, sticky="W", padx=10, pady=5)
    
    update_btn = Button(self._updateWindow, text='Update Review', width=12, command=self.btnClickUpdateReview, fg=lbl_color, bg='#2ECC71')
    update_btn.grid(row=10, column=0, sticky="W", padx=5, pady=10)

    cancel_btn = Button(self._updateWindow, text='Cancel', width=12, command=self.btnClickCancel, fg=lbl_color, bg='#E74C3C')
    cancel_btn.grid(row=10, column=1, sticky="E", padx=5, pady=10)
    
    #
    # Initialize the controls with the movie review that was selected
    #
    entry_name.delete(0, END)
    entry_name.insert(END, self._movie.name)  
    
    entry_year.delete(0, END)
    entry_year.insert(END, self._movie.year)
    
    entry_rating.delete(0, END)
    entry_rating.insert(END, self._movie.rating)
    
    current_index = sorted_genres.index(self._movie.genre)
    cbox_genre.current(current_index)
    
    self._entry_review.delete('1.0', 'end')
    self._entry_review.insert('end', self._movie.review)         

    #self.pack()
    self.pack(fill="x", padx=20, pady=20)
                  
    # self._insertWindow.mainloop()
      
  def btnClickUpdateReview(self):
    try:
      review = Movie(self._movie.id, 
                        self._movie_name.get(), 
                        int(self._movie_year.get()), 
                        float(self._movie_rating.get()), 
                        self._movie_genre.get(),
                        self._entry_review.get('1.0', 'end-1c'))
       
      DataAccessHelper().updateMovieReview(review)
      
    except Exception as e:
      print (e)
    
    finally:
      self._updateWindow.destroy()
    
  def btnClickCancel(self):
      self._updateWindow.destroy()
      
  def center_window(self, w=300, h=200):
      # get screen width and height
      ws = self._updateWindow.winfo_screenwidth()
      hs = self._updateWindow.winfo_screenheight()
      # calculate position x, y
      x = (ws/2) - (w/2)    
      y = (hs/2) - (h/2)
      self._updateWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))      
      