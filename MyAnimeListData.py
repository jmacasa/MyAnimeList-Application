import tkinter as tk
from tkinter import *
from tkinter import ttk
from jikanpy import Jikan


def newSearch():
    global search
    global typeSearch
    global searchLabel
    searchLabel = tk.Label(text="Enter search:")
    searchLabel.pack()
    titleSearch = StringVar()
    search = tk.Entry(textvariable=titleSearch)
    search.pack()
    typeSearch = tk.Button(text="Search", command=lambda: searchDisplay(search.get()))
    typeSearch.pack()

def searchDisplay(searchTitle):
    typeSearch.destroy()
    searchLabel.destroy()
    newWindow = Toplevel()
    newWindow.title("Search Results for '" + search.get() + "'")
    search.destroy()
    searchResult = jikan.search(type.get(), searchTitle, page=1)
    main_frame = Frame(newWindow)
    main_frame.pack(fill=BOTH, expand=1)
    canvas = Canvas(main_frame)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)
    scrollbar = tk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    second_frame = Frame(canvas)
    canvas.create_window((0, 0), window=second_frame, anchor="nw")
    for result in searchResult['results']:
        tk.Button(second_frame, text=result['title'], command=lambda result=result: getRating(result)).pack(side=TOP)

def getRating(result):
    ratingWindow = Toplevel()
    ratingWindow.title(result['title'])
    tk.Label(ratingWindow, text="The rating of " + result['title'] + " is " + str(result['score'])).pack()

jikan = Jikan()
window = tk.Tk()
window.title("Ratings from MyAnimeList")
message = tk.Label(text="Welcome! This program is designed to help get data of an anime or manga from MyAnimeList.")
message.pack()
inputMessage = tk.Label(text="What are you looking for?")
inputMessage.pack()
searchType = StringVar()
type = ttk.Combobox(window, textvariable=searchType)
type['values'] = ("anime", "manga")
type.state(["readonly"])
type.pack()
searchButton = tk.Button(text="Search", command=newSearch)
searchButton.pack()
window.mainloop()
