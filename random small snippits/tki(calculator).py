import tkinter as tk

class calculator:
    def __init__(self, mytk):
        self.mytk = mytk
        mytk.title("Calcualtor")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        #create the display widget
        self.display = tk.Entry(mytk, textvariable=self.result_var, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5,sticky="nsew")

        #create the buttons
        buttons = [
            "7","8","9","/",
            "4","5","6","*",
            "3","2","1","-",
            "0",".","=","+"
        ]
        #create the button widgets and add them to the grid
        row=1
        col=0
        for button_text in buttons:
            button = tk.Button(mytk, text=button_text, width=5,height=2)
            button.grid(row=row,column=col, padx=5, pady=5, sticky="nsew")
            button.bind("<Button-1>", self.button_click)
            col += 1
            if col > 3:
                col=0
                row+=1 
    def button_click(self, event):
        button_text = event.widget["text"]

        if button_text == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        else:
            if self.result_var.get() == "0":
                self.result_var.set("")
            self.result_var.set(self.result_var.get()+button_text)

#create the main window and the loop
root = tk.Tk()
Calculator = calculator(root)
root.mainloop()