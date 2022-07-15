from tkinter import *
import imdb,time
import string
from tkinter import messagebox

def search():
    if movieentry.get() =='':
        messagebox.showerror('Error', 'Please input a movie name')

    else:
        root1 = Toplevel()
        root1.geometry('1890x1900')
        root1.title('Movie Information')
        root1.config(bg='orange')

        # title label name
        TitleLabel = Label(root1, text='Title: ', font=('algerian', 30, 'bold'), bg='orange')
        TitleLabel.place(x=60, y=30)

        # label for getting the movie name
        TitlenameLabel = Label(root1, text='', font=('', 30), fg='white', bg='orange')
        TitlenameLabel.place(x=220, y=30)

        # label for the director
        DirectorLabel = Label(root1, text='Driector Name: ', font=('algerian', 30, 'bold'), bg='orange')
        DirectorLabel.place(x=60, y=110)

        # label for getting the director name
        DirectornameLabel = Label(root1, text='', font=('', 30, 'bold'), bg='orange', fg='white')
        DirectornameLabel.place(x=420, y=110)

        # label for getting the year name
        YearLabel = Label(root1, text='Year: ', font=('algerian', 30, 'bold'), bg='orange')
        YearLabel.place(x=60, y=190)

        # year
        yearnameLabel = Label(root1, text='', font=('', 30, 'bold'), bg='orange', fg='white')
        yearnameLabel.place(x=420, y=190)

        # runtime code
        RuntimeLabel = Label(root1, text='Runtime: ', font=('algerian', 30, 'bold'), bg='orange')
        RuntimeLabel.place(x=60, y=280)

        RunnametimeLabel = Label(root1, text='', font=('', 30, 'bold'), bg='orange',fg='white')
        RunnametimeLabel.place(x=420, y=280)


            # geners code
        GenresLabel = Label(root1, text='Genres: ', font=('algerian', 30, 'bold'), bg='orange')
        GenresLabel.place(x=60, y=370)

        GenrestimeLabel = Label(root1, text='', font=('', 30, 'bold'), bg='orange',fg='white')
        GenrestimeLabel.place(x=420, y=370)


        # rating code
        RatingLabel = Label(root1, text='Rating: ', font=('algerian', 30, 'bold'), bg='orange')
        RatingLabel.place(x=60, y=460)

        ratingnameLabel = Label(root1, text='', font=('', 30, 'bold'), bg='orange',fg='white')
        ratingnameLabel.place(x=490, y=460)

        # cast
        CastLabel = Label(root1, text='Cast: ', font=('algerian', 30, 'bold'), bg='orange')
        CastLabel.place(x=60, y=550)

        # cast_name
        CastnameLabel = Label(root1, text='',font=('', 30, 'bold'), bg='orange',fg='white', wraplength=615,justify= LEFT)
        CastnameLabel.place(x=420, y=550)

        imdbobj = imdb.IMDb()
        movie_name = movieentry.get()
        movies = imdbobj.search_movie(movie_name)
        index = movies[0].getID()
        movie = imdbobj.get_movie(index)

        # code for getting the movie
        title = movie['title']
        TitlenameLabel.config(text=title)

        # code for getting the year code
        year = movie['year']
        yearnameLabel.config(text=year)

        # coding for getting rating
        rating = movie['rating']
        ratingnameLabel.config(text=rating)

        # code for getting the director
        director = movie['director']
        for i in director:
            DirectornameLabel.config(text=i)

        # code for getting the cast
        cast = movie['cast']
        a = list(map(str,cast))
        strr = ' '
        for i in a[:6]:
            if i == a[5]:
                strr = strr + i + ' ' + '.'
            else:
                strr = strr + i + ','
        CastnameLabel.config(text=strr)

        # code for getting the runtime

        for i in movie['runtime']:
            hour = int(i) // 60
            minute = int(i) % 60
            RunnametimeLabel.config(text=f"{hour} hours {minute} minute")
        #code for getting the genres
        g =''
        for i in movie['genre']:
            g = g + i + ','

        GenrestimeLabel.config(text=g)

        root1.mainloop()


root = Tk()
root.geometry('1057x650+100+30')
root.title('Movie description')
root.resizable(0, 0)
root.config(bg='pink')
bgpic = PhotoImage(file='img.png')

bgLabel = Label(root, image=bgpic)
bgLabel.pack()
# bgLabel.place(x=0,y=0)


movieLabel = Label(root, text='Movie Name: ', font=('algerian', 30, 'bold'), bg='pink')
movieLabel.place(x=244, y=422)

movieentry = Entry(root, font=('', 20, 'bold'), bd=5)
movieentry.place(x=520, y=430)
movieentry.focus_set()

moviesearch = Button(root, text='SEARCH ', font=('algerian', 20, 'bold'), bd=5, command=search)
moviesearch.place(x=503, y=490)

root.mainloop()
