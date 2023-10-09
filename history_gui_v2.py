from tkinter import *
from functools import partial # to prevent unwanted windows

class Converter:
    
    def __init__(self):
        # testin list 
        # 5 item list
        self.all_calculations = ['19 C° is 66 °F', '17 F° is -8 °C', '167 C° is 333 °F', '15 C° is 59 °F','homie']

        

        #common format for all buttons
        BUTTON_FONT = ('Arial', '12', 'bold')
        BUTTON_FG = '#ffffff'


        #set up Gui Frame
        self.temp_frame = Frame(padx=10,pady=10)
        self.temp_frame.grid()


        #button frame 
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=0)


        # history info button
        self.to_history_button = Button(self.button_frame, text = 'History / Export', bg = '#004C99', fg = BUTTON_FG ,font= BUTTON_FONT, width = 12, command=lambda: self.to_history(self.all_calculations))
        self.to_history_button.grid(row = 1, column = 1, padx = 5, pady=5)

        # renove when intergrating 
        self.to_history_button.config(state = NORMAL)
    def to_history(self, all_calculations):
        HistoryExport(self, all_calculations)


class HistoryExport:
    def __init__(self, partner, calc_list):
        
        #set maximum number of calculations to 5
        #this can be changed if we want to show fewer or more calculations

        max_calcs = 5
        self.var_max_calcs = IntVar()
        self.var_max_calcs.set(max_calcs)

        # function converts contents of calculation list into a string
        calc_string_text = self.get_calc_string(calc_list)
        
        
        
        # setup dialouge box and back ground color 
        self.history_box = Toplevel()
        #  disable the history / export button
        partner.to_history_button.config(state = DISABLED)
        # if the user press cross at the top , closes help box and release help button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # set up new frame and grid
        self.history_frame = Frame(self.history_box, width = 300, height = 200)
        self.history_frame.grid()

        # heading label
        self.history_heading_label = Label(self.history_frame, text = 'History / Export', font = ('Arial', '14', 'bold'), wrap = 350, justify = 'left')
        self.history_heading_label.grid(row = 0)

        # customise text and background colour for calculation 
        #area depending on wether all or only some calculations are shown
        num_calcs = len(calc_list)

        if num_calcs > max_calcs:
            calc_background = '#FFE6CC'  # peach
            showing_all = "Here are your recent calculations " \
                "({}/{} calculations shown). Please export your " \
                    "calculations to see your full calculation " \
                        "history".format(max_calcs, num_calcs)
        else:
            calc_background = '#B4FACB' # pale green
            showing_all = 'Below is your calculation history.'


        # text 1 label
        history_text_1 = '{} \n\n All calculations are shown to the nearest degree'.format(showing_all)
        self.history_text_1_label = Label(self.history_frame, text = history_text_1, wrap = 350, justify = 'left')
        self.history_text_1_label.grid(row = 1, padx = 10)

        # calculations label
        
        self.history_calculations_label = Label(self.history_frame, text= calc_string_text, justify = 'center', bg = calc_background, width = 46)
        self.history_calculations_label.grid(row = 2, padx = 10, pady = 10)

        # text 2 label
        history_text_2 = 'Either choose a custom file name (and push <Export>) or simply push <Export> to save your calculations in a text file. If the filename allready exists it will be overwritten!'
        self.history_text_2_label = Label(self.history_frame, text = history_text_2, wrap = 350, justify = 'left')
        self.history_text_2_label.grid(row = 3, padx = 10)

        # entry box
        self.text_file_entry = Entry(self.history_frame, font=('Arial','14'))
        self.text_file_entry.grid(row=4,padx=10,pady=10)

        # error label 
        self.history_text_error = Label(self.history_frame, text = 'Filename error goes here', justify = 'center', font = ('Arial', '13', 'bold'), fg = '#FF0000')
        self.history_text_error.grid(row = 5)

        # button frame - creates a simple grid that is good for putting buttons on
        self.history_button_frame = Frame(self.history_frame)
        self.history_button_frame.grid(row = 6)


        # Export Button
        self.export_button = Button(self.history_button_frame, font = ('Arial', '12', 'bold'), text = 'Export', bg = '#004C99', fg = '#ffffff', width = 12)
        self.export_button.grid(row = 0, column = 0, padx = 5, pady = 5)

        # dismiss button
        self.dismiss_button = Button(self.history_button_frame, font = ('Arial', '12', 'bold'), text = 'Dismiss', bg = '#666666', fg = '#ffffff', width = 12,command = partial(self.close_history, partner))
        self.dismiss_button.grid(row = 0, column = 1, padx = 5, pady = 5)

    
    #change calculation list into a string so that it can be ouitputted as a label
    def get_calc_string(self, var_calculations):
        # get max calc to display
        # (was set in __init__ function)
        max_calcs = self.var_max_calcs.get()
        calc_string = ''

        #work out how many times we need to loop
        # to output either the last five calculations or all calculations
        if len(var_calculations) >= max_calcs:
            stop = max_calcs

        else:
            stop = len(var_calculations)

        #iterate to all but last item
        # adding item and line break to calculation string
        for item in range(0, stop - 1):
            calc_string += var_calculations[len(var_calculations) - item - 1]
            calc_string += '\n'
        
        #add final item without extra linebreak
        # ie last item on list will be fifth from the end
        calc_string += var_calculations[-max_calcs]

        return calc_string

        #close help dialouge (used by x at top of dialouge)
    
    def close_history(self, partner):
        # put help back to normal ...
        partner.to_history_button.config(state = NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == '__main__':
    root = Tk()
    root.title('Temputure Converter')
    #calling Converter Class
    Converter()
    root.mainloop()

