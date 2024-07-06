from tkinter import*
import os
window=Tk()

#helper
frame_collection=[] #create a list just to save the last frame ,frame is saved as address in list.
                    #adress of the frame is elements

def createFrame():
    global frame_collection
    if len(frame_collection)>0:
        previous_frame=frame_collection.pop() #one saved in list is save to prevframe
        previous_frame.destroy()              #frame is distroyed 

    newFrame=Frame(window)
    frame_collection.append(newFrame)
    return newFrame

#create
def createuser(namenEtry,phoneEntry):
    name=namenEtry.get()
    phone=phoneEntry.get()
    filepath=f"./PBFH/{name}.txt"
    file=open(filepath,'w')
    file.write(f"{name}\n{phone}")
    file.close()

def createButtonClick():
    new_frame=createFrame()
    new_frame.grid(row=1,column=1)

    namelabel=Label(new_frame,text="enter a user name : ")
    namelabel.pack()

    nameEntry=Entry(new_frame)
    nameEntry.pack()

    phonelabel1=Label(new_frame,text="Enter a number : ")
    phonelabel1.pack()

    phoneEntry=Entry(new_frame)
    phoneEntry.pack()

    createuserbutton=Button(new_frame,text="Create the user",command=lambda:createuser(nameEntry,phoneEntry))
    createuserbutton.pack()

option1=Button(window,text="create",font=8,width=20,height=2,bg="green",fg="white",command=createButtonClick)
option1.grid(row=0,column=0,padx=10,pady=10)

def viewbuttonclick():
    def viewUser():
        name=nameEntry.get()
        filepath=f"./PBFH/{name}.txt"
        try:
            file=open(filepath)
            lines=file.readlines()
            phone=lines[1]
            phoneLabel.config(text=phone)
        except:
            phoneLabel.config(text="User Not Found")

    new_Frame=createFrame()
    new_Frame.grid(row=1,column=1)

    nameLabel=Label(new_Frame,text="Enter a name to search")
    nameLabel.pack()

    nameEntry=Entry(new_Frame)
    nameEntry.pack()

    viewbuttoN=Button(new_Frame,text="click to view",command=viewUser)
    viewbuttoN.pack()

    phoneLabel=Label(new_Frame,text="")
    phoneLabel.pack()


#view
option2=Button(window,text="view",font=8,width=20,height=2,bg="blue",fg="white",command=viewbuttonclick)
option2.grid(row=0,column=1,padx=10,pady=10)

def deleteuser():
    def delete():
        name=nameEntry.get()
        filepath=f"./PBFH/{name}.txt"
        os.remove(filepath)
        nameEntry.delete(0,END)

    new_Frame=createFrame()
    new_Frame.grid(row=1,column=1)

    nameLabel=Label(new_Frame,text="Enter a name to search")
    nameLabel.pack()

    nameEntry=Entry(new_Frame)
    nameEntry.pack()

    deletebuttoN=Button(new_Frame,text="click to delete",command=delete)
    deletebuttoN.pack()



#delete
option3=Button(window,text="delete",font=8,width=20,height=2,bg="red",fg="white",command=deleteuser)
option3.grid(row=0,column=2,padx=10,pady=10)

#edit
def edituser():
    def editname():
        name=nameEntry.get()
        filepath=f"./PBFH/{name}.txt"
        try:
            file=open(filepath)
            lines=file.readlines()
            file.close()
            newname=newnameentry.get()
            newphone=newphoneentry.get()
            file=open(filepath,'w')
            file.write(f"{newname}\n{newphone}")
            filepath2=f"./PBFH/{newname}.txt"
            file.close()
            
            dir_path = os.path.dirname(filepath)
            new_file_path = os.path.join(dir_path,filepath2)
            os.rename(filepath, filepath2)

            changelabel.config(text=newname)
        except:
            changelabel.config(text="User Not Found")


    new_Frame=createFrame()
    new_Frame.grid(row=1,column=1)

    nameLabel=Label(new_Frame,text="Enter a name to search : ")
    nameLabel.grid(row=2,column=3)

    nameEntry=Entry(new_Frame)
    nameEntry.grid(row=2,column=5)

    newnamelabel=Label(new_Frame,text="enter new name : ")
    newnamelabel.grid(row=3,column=3)

    newnameentry=Entry(new_Frame)
    newnameentry.grid(row=3,column=5)

    newphonelabel=Label(new_Frame,text="enter new num : ")
    newphonelabel.grid(row=4,column=3)
   
    newphoneentry=Entry(new_Frame)
    newphoneentry.grid(row=4,column=5)

    editebuttoN=Button(new_Frame,text=" edit ",command=editname)
    editebuttoN.grid(row=5,column=3,columnspan=5)

    changelabel=Label(new_Frame,text="")
    changelabel.grid(row=7,column=5)


option4=Button(window,text="edit",font=8,width=20,height=2,bg="yellow",fg="black",command=edituser)
option4.grid(row=0,column=3,padx=10,pady=10)

window.mainloop()