import tkinter as tk
import webbrowser, os, signal

class LolApp(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master,width=400,height=400)
        self.master.title('Better League Client')
        self.pack_propagate(0)
        self.pack()
        self.choice_var = tk.StringVar()
        self.choice = tk.OptionMenu(self,self.choice_var,'League Of Legends','The Better League','Make League Better')
        self.choice_var.set('Select Option')
        self.go_button = tk.Button(self,text='Go',command=self.action_out)
        self.go_button.pack(fill=tk.X, side=tk.BOTTOM)
        self.choice.pack(fill=tk.X, side=tk.BOTTOM)

    def action_out(self):
        if(self.choice_var.get().title()=="League Of Legends"):
            os.startfile (r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\League of Legends.lnk")
        elif(self.choice_var.get().title()=="The Better League"):
            webbrowser.open("https://store.steampowered.com/app/1731720/FURRY_SEX_Cabaret/", new=2)
        elif(self.choice_var.get().title()=="Make League Better"):
            os.kill(int('LeagueClientUx.exe'), signal.SIGKILL)
        else:
            print('You need to make a selection...')

    def run(self):
        self.mainloop()

app = LolApp(tk.Tk())
app.run()