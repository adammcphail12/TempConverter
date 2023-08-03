from tkinter import *

class Converter:
    
    def __init__(self):
        
        #set up Gui Frame
        self.temp_frame = Frame(padx=10,pady=10)
        self.temp_frame.grid()


        #heading                                                              
        self.temp_heading = Label(self.temp_frame, text='Temputre Converter', font=('Arial', '16','bold'))
        self.temp_heading.grid(row=0)


        #instructions
        instructions = 'Please enter a temperature below then press one of the buttons to convert it from centigrade to Fahrenheirt'
        self.temp_instructions = Label(self.temp_frame, text= instructions,wrap = 250 , width = 40, justify='left')
        self.temp_instructions.grid(row=1)


        # entry box
        self.temp_entry = Entry(self.temp_frame, font=('Arial','14'))
        self.temp_entry.grid(row=2,padx=10,pady=10)
        
        #error label
        self.temp_error = Label(self.temp_frame, text= 'Error message if file name is invalid', font= )


# main routine
if __name__ == '__main__':
    root = Tk()
    root.title('Temputure Converter')
    #calling Converter Class
    Converter()
    root.mainloop()

