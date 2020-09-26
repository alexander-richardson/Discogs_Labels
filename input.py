from tkinter import *

def save_info():
    release_id_info = release.get()
    print(release_id_info)
    file = open("release.txt", "w")
    file.write(str(release_id_info))
    file.close()


app = Tk()

app.geometry("500x500")

app.title("Label Generator")

heading = Label(text="Enter the release id's bellow", bg ='yellow', fg='black', font='10', width='500', height='3')
heading.pack()

release_id = Label(text="Release ID: ")
release_id.place(x='15', y='70')

release =IntVar()

release_id_entry= Entry(textvariable=release, width='30')
release_id_entry.place(x="15", y="100")

add_release =Button(app, text='add release id', command= save_info, width='30', height='2', bg="grey")
add_release.place(x="15", y="130")

id_text = Text(app,)

mainloop()
