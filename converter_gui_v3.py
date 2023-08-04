from tkinter import *

class Converter:
    
    def __init__(self):

        # Intialise variables (suchas the feedback variable)
        self.var_feedback = StringVar()
        self.var_feedback.set('')

        self.var_has_error = StringVar()
        self.var_has_error.set('no')


        
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
        self.output_label = Label(self.temp_frame,text = '', font= ('Arial', 9), fg='#9C0000' )
        self.output_label.grid(row=3)

        #button frame 
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        #to celcious button
        self.to_celsius_button = Button(self.button_frame, text = 'To degrees C', bg = '#990099', fg = BUTTON_FG, font= BUTTON_FONT , width = 12, command=self.temp_convert(-459)) 
        self.to_celsius_button.grid(row = 0, column = 0,padx = 5, pady = 5)

        # to farrenheit button
        self.to_farrenheit_button = Button(self.button_frame, text = 'To degrees F',bg = '#009900', fg = BUTTON_FG, font= BUTTON_FONT, width = 12, command=self.temp_convert(-273))
        self.to_farrenheit_button.grid(row = 0, column = 1, padx = 5, pady= 5)

        #help info button
        self.to_help_button = Button(self.button_frame, text = 'Help / Info', bg = '#CC6600', fg = BUTTON_FG ,font= BUTTON_FONT, width = 12)
        self.to_help_button.grid(row = 1, column = 0, padx = 5, pady=5)

        #history button
        self.to_history_button = Button(self.button_frame, text= 'History / Export', bg = '#004C99', fg = BUTTON_FG, font = BUTTON_FONT, width = 12, state= DISABLED)
        self.to_history_button.grid(row = 1, column = 1, padx = 5, pady = 5)


    # rounds answers to whole numbers
    @staticmethod
    def round_ans(val):
        var_rounded = (val * 2 + 1) // 2
        return '{:.0f}'.format(var_rounded)

    # input checker, designed to make sure a value is more then a set variable, we will ue this to check that the users 
    # inputs are actualy valid ones.
    def check_temp(self, min_value):
        
        has_error = 'no'
        error = 'Please enter a value that is more than {}'.format(min_value)
        
        response = self.temp_entry.get()


        try:
            response = float(response)

            if response < min_value:
                has_error = 'yes'
            
        except ValueError:
            has_error = 'yes'
        
        #sets var_has_error so that entry box,
        # and labels can be correctly formatted by formatting function
        if has_error == "yes":
            self.var_has_error.set('yes')
            self.var_feedback.set(error)
            return 'invalid'
        
        # if we have no errors 
        else:
            #set to 'no' in case of previous errors
            self.var_has_error.set('no')

            #return number to be
            #converted amd enable history button
            self.to_history_button.config(state=NORMAL)
            return response

       
    

    # check temputure is valid and convert it
    def temp_convert(self, min_val):
        
        to_convert = self.check_temp(min_val)
        degree_sign = u'\N{DEGREE SIGN}'
        set_feedback = 'yes'
        answer = ''
        from_to = ''
        if to_convert != 'invalid':
            set_feedback = 'no'
        # convert to celsius
        elif min_val == -459:
            # do calculation
            answer = (to_convert - 32) * 5 / 9
            from_to = '{} F{} is {} C{}'
        
        # convert to fahrenheit 
        else:
            # do calculation
            answer = to_convert * 1.8 + 32
            from_to = '{} C{} is {} C{}'

        if set_feedback == 'yes':
            to_convert = self.round_ans(to_convert)
            answer = self.round_ans(answer)

            #creates user output and add to calculation history
            feedback = from_to.format(to_convert, degree_sign, answer, degree_sign)
            self.var_feedback.set(feedback)
    
        self.output_answer()

    # shows user output and clears entry widget
    # ready for next calculation
    def output_answer(self):
        output = self.var_feedback.get()
        has_errors = self.var_has_error.get()

        if has_errors == 'yes':
            #red text, pink entry box
            self.output_label.config(fg='#9C0000')
            self.temp_entry.config(bg='#F8CECC')

        else:
            self.output_label.config(fg='#004C00')
            self.temp_entry.config(bg='#FFFFFF')

        self.output_label.config(text = output)




# main routine
if __name__ == '__main__':
    root = Tk()
    root.title('Temputure Converter')
    #calling Converter Class
    Converter()
    root.mainloop()

