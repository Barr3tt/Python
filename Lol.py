import tkinter as tk
 
class LolApp(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master,width=300,height=200)
        self.master.title('Better League Client')
        self.pack_propagate(0)
        self.pack()
        self.choice_var = tk.StringVar()
        self.choice = tk.OptionMenu(self,self.choice_var,'League Of Legends','LOL V2','Make League Better"')
        self.choice_var.set('League Of Legends')
        self.go_button = tk.Button(self,text='Go',command=self.print_out)
        self.go_button.pack(fill=tk.X, side=tk.BOTTOM)
        self.choice.pack(fill=tk.X, side=tk.BOTTOM)
 
    def print_out(self):
        print('%s!' % (self.choice_var.get().title()))
    def run(self):
        self.mainloop()
 
app = LolApp(tk.Tk())
app.run()