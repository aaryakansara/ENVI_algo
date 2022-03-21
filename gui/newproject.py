import tkinter as tk
from tkinter import Button, Menu, filedialog, Text 
import os 

self = tk.Tk()
self.title('Create New Project')
self.resizable(True, True)



def loadmusic():
            filename = filedialog.askopenfilename(initialdir="C:/Users/Admin/Music", title="Select Your Music File",
            filetypes=(("MP3","*.mp3"), ("WAV", "*.wav"), ("AAC", "*.aac"), ("3GP", "*.3gp"), ("WEBM", "*.webm")))

        # def warn(event):
        #     res = messagebox.askquestion('Warning!!!', 'Are you sure you want to go back?\nThis will take you back to Home Page \nAny unsaved progress could be lost!!')
        #     if res == 'yes':
        #         controller.show_frame(HomePage)
        #     elif res == 'no':
        #         exit
        #     else:
        #         messagebox.showwarning('Error', 'Something went wrong!')
                
        # def fullscreen():
        #     self.attributes('-fullsecreen', True)

            
canvas = tk.Canvas(self, height=700, width=1340, bg="white")
canvas.pack()

frame = tk.Frame(self, bg="#6495ED")
frame.place(relwidth=1, relheight=1, relx=0, rely=0)

frameG = tk.Frame(self, bg="grey")
frameG.place(relwidth=1, relheight=0.010, relx=0, rely=0)

frameT = tk.Frame(self, bg="goldenrod1")
frameT.place(relwidth=1, relheight=0.036, relx=0, rely=0.002)

taskfile = tk.Frame(frameT, bg="red2")
taskfile.place(relwidth=0.04, relheight=0.9, relx=0.0009, rely=0.05)
        
bfile = tk.Label(taskfile, text="File", fg="white", padx=25, pady=15, font=('Microsoft YaHei UI', 10, "bold"), bg="red2") #
bfile.pack()
m1 = Menu(bfile, tearoff = 0)
m1.add_command(label ="Open Existing Project")
m1.add_command(label ="New Project")
m1.add_separator()
m1.add_command(label ="Save (Ctrl + S)")
m1.add_command(label ="Save as (Ctrl + F8)")
m1.add_separator()
m1.add_command(label ="Help")
def do_popup(event):
            try:
                m1.tk_popup(event.x_root, event.y_root)
            finally:
                m1.grab_release()
        
bfile.bind("<Button-1>", do_popup)
        
        
taskcompile = tk.Frame(frameT, bg="grey")
taskcompile.place(relwidth=0.06009, relheight=0.9, relx=0.042, rely=0.05)
bcompile = tk.Label(taskcompile, text="Compile", padx=25, pady=15, fg="white", font=('Microsoft YaHei UI', 10, "bold"), bg="red2")
bcompile.pack()
m2 = Menu(bcompile, tearoff = 0)
m2.add_command(label ="Compile in ENVI editor format")
m2.add_separator()
m2.add_command(label ="Compile in Executable file")
m2.add_separator()
m2.add_command(label ="Help: Know the difference?")
def do_popup(event):
            try:
                m2.tk_popup(event.x_root, event.y_root)
            finally:
                m2.grab_release()
        
bcompile.bind("<Button-1>", do_popup)
        
taskview = tk.Frame(frameT, bg="grey")
taskview.place(relwidth=0.04, relheight=0.9, relx=0.1025, rely=0.05)
bview = tk.Label(taskview, text="View", padx=25, pady=15, fg="white", font=('Microsoft YaHei UI', 10, "bold"), bg="red2")
bview.pack()
m3 = Menu(bview, tearoff = 0)
m3.add_command(label ="View Page Number: (Ctrl + F)")
m3.add_separator()
m3.add_command(label ="View Fullscreen Mode",)# command=fullscreen)  
def do_popup(event):
            try:
                m3.tk_popup(event.x_root, event.y_root)
            finally:
                m3.grab_release()
        
bview.bind("<Button-1>", do_popup)
        
taskedit = tk.Frame(frameT, bg="grey")
taskedit.place(relwidth=0.04, relheight=0.9, relx=0.1435, rely=0.05)
bedit = tk.Label(taskedit, text="Edit", padx=25, pady=15, fg="white", font=('Microsoft YaHei UI', 10, "bold"), bg="red2",)# command=lambda: controller.show_frame(Pagetakeskipinfo),)# relief=SUNKEN)
bedit.pack()
        # def editdetails(event):
        #     controller.show_frame(Pagetakeskipinfo)
        # bedit.bind("<Button-1>", editdetails)
        
taskback = tk.Frame(frameT, bg="grey")
taskback.place(relwidth=0.03, relheight=0.9, relx=0.938, rely=0.05)
bback = tk.Label(taskback, text="←", padx=25, pady=15, fg="white", font=('Microsoft YaHei UI', 10, "bold"), bg="#FF7256",)# command=warn)
bback.pack()
bback.bind("<Button-1>",)# warn)
        
taskhelp = tk.Frame(frameT, bg="grey")
taskhelp.place(relwidth=0.03, relheight=0.9, relx=0.9685, rely=0.05)
buthelp = tk.Label(taskhelp, text= "?", padx=25, pady=25, fg="white", font=("Arial",10, "bold"), bg="red2")
buthelp.pack()
        # def gohelp(event):
        #         controller.show_frame(HelpPagec)
        # buthelp.bind("<Button-1>", gohelp)

frame = tk.Frame(self, bg="lightblue")
frame.place(relwidth=0.3, relheight=0.919, relx=0.01, rely=0.06)

frame0 = tk.Frame(self, bg="lightblue")
frame0.place(relwidth=0.6665, relheight=0.66, relx=0.32, rely=0.06)
        
mainframe = tk.Frame(frame0, bg="grey")
mainframe.place(relwidth=0.99, relheight=0.98, relx=0.005, rely=0.01)

frame1 = tk.Frame(self, bg="lightblue")
frame1.place(relwidth=0.6665, relheight=0.2385, relx=0.32, rely=0.74045)

buttonframe = tk.Frame(frame1, bg="#6495ED")
buttonframe.place(relwidth=0.275, relheight=0.25, relx=0.02, rely=0.16)
bmusic = tk.Button(buttonframe, text="MUSIC", padx=95, pady=10, fg="white", borderwidth=0, font=('Microsoft YaHei UI', 15, "bold"), bg="#FF6103", command=loadmusic)
bmusic.pack()
buttonframe = tk.Frame(frame1, bg="#6495ED")
buttonframe.place(relwidth=0.275, relheight=0.25, relx=0.364, rely=0.16)
bflow = tk.Button(buttonframe, text="FLOW MAP", padx=75, pady=10, fg="white", borderwidth=0, font=('Microsoft YaHei UI', 15, "bold"), bg="#FF6103",)# command=lambda: controller.show_frame(FlowmapPage))
bflow.pack()
buttonframe = tk.Frame(frame1, bg="#6495ED")
buttonframe.place(relwidth=0.275, relheight=0.25, relx=0.705, rely=0.16)
bbranch = tk.Button(buttonframe, text="BRANCH OPTIONS", padx=75, pady=10, fg="white", borderwidth=0, font=('Microsoft YaHei UI', 15, "bold"), bg="#FF6103")
bbranch.pack()
buttonframe = tk.Frame(frame1, bg="#6495ED")
buttonframe.place(relwidth=0.275, relheight=0.25, relx=0.02, rely=0.6)
bimageset = tk.Button(buttonframe, text="IMAGE SETTINGS", padx=75, pady=10, fg="white", borderwidth=0, font=('Microsoft YaHei UI', 15, "bold"), bg="#FF6103")
bimageset.pack()
buttonframe = tk.Frame(frame1, bg="#6495ED")
buttonframe.place(relwidth=0.275, relheight=0.25, relx=0.364, rely=0.6)
bparaset = tk.Button(buttonframe, text="PARAMETER SETTINGS", padx=75, pady=10, fg="white", borderwidth=0, font=('Microsoft YaHei UI', 15, "bold"), bg="#FF6103")
bparaset.pack()
buttonframe = tk.Frame(frame1, bg="#6495ED")
buttonframe.place(relwidth=0.275, relheight=0.25, relx=0.705, rely=0.6)
bsandn = tk.Button(buttonframe, text="SAVE & NEXT", padx=75, pady=10, fg="white", font=('Microsoft YaHei UI', 15, "bold"), bg="#FF6103")
bsandn.pack()        
        
        
self.mainloop()