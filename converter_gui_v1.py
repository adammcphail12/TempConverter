from tkinter import *

class Converter:
    
    def __init__(self):
        
        #common format for all buttons
        BUTTON_FONT = ('Arial', '12', 'bold')
        BUTTON_FG = '#ffffff'


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
        self.temp_error = Label(self.temp_frame,text = '', font= ('Arial', 9), fg='#9C0000' )
        self.temp_error.grid(row=3)

        #button frame 
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        #to celcious button
        self.to_celsius_button = Button(self.button_frame, text = 'To degrees C', bg = '#990099', fg = BUTTON_FG, font= BUTTON_FONT , width = 12, command=self.to_celsius) 
        self.to_celsius_button.grid(row = 0, column = 0,padx = 5, pady = 5)

        # to farrenheit button
        self.to_farrenheit_button = Button(self.button_frame, text = 'To degrees F',bg = '#009900', fg = BUTTON_FG, font= BUTTON_FONT, width = 12 )
        self.to_farrenheit_button.grid(row = 0, column = 1, padx = 5, pady= 5)

        #help info button
        self.to_help_button = Button(self.button_frame, text = 'Help / Info', bg = '#CC6600', fg = BUTTON_FG ,font= BUTTON_FONT, width = 12)
        self.to_help_button.grid(row = 1, column = 0, padx = 5, pady=5)

        #history button
        self.to_history_button = Button(self.button_frame, text= 'History / Export', bg = '#004C99', fg = BUTTON_FG, font = BUTTON_FONT, width = 12, state= DISABLED)
        self.to_history_button.grid(row = 1, column = 1, padx = 5, pady = 5)


    # input checker, designed to make sure a value is more then a set variable, we will ue this to check that the users 
    # inputs are actualy valid ones.
    def check_temp(self, min_value):
        error = 'Please enter a value that is more than {}'.format(min_value)
        
        
        try:
            response = self.temp_entry.get()
            response = float(response)

            if response < min_value:
                print(error)
            else:
                return response
            
        except ValueError:
            self.temp_error.config(text=error)
    
    # convert to celsius function
    def to_celsius(self):
        
        self.check_temp(-459)




# main routine
if __name__ == '__main__':
    root = Tk()
    root.title('Temputure Converter')
    #calling Converter Class
    Converter()
    root.mainloop()

