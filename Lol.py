import tkinter as tk
 
class LolApp(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master,width=300,height=200)
        self.master.title('Better League Client')
        self.pack_propagate(0)
        self.pack()
        self.greeting_var = tk.StringVar()
        self.greeting = tk.OptionMenu(self,self.greeting_var,'hello','goodbye','heyo')
        self.greeting_var.set('hello')
        self.recipient_var = tk.StringVar()
        self.recipient = tk.Entry(self,textvariable=self.recipient_var)
        self.recipient_var.set('world')
        self.go_button = tk.Button(self,text='Go',command=self.print_out)
        self.go_button.pack(fill=tk.X, side=tk.BOTTOM)
        self.greeting.pack(fill=tk.X, side=tk.TOP)
        self.recipient.pack(fill=tk.X, side=tk.TOP)
 
    def print_out(self):
        print('%s, %s!' % (self.greeting_var.get().title(),self.recipient_var.get()))
    def run(self):
        self.mainloop()
 
app = LolApp(tk.Tk())
app.run()