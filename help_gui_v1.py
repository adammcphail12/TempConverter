from tkinter import *
from functools import partial # to prevent unwanted windows

class Converter:
    
    def __init__(self):

        #common format for all buttons
        BUTTON_FONT = ('Arial', '12', 'bold')
        BUTTON_FG = '#ffffff'


        #set up Gui Frame
        self.temp_frame = Frame(padx=10,pady=10)
        self.temp_frame.grid()


        #button frame 
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)


        #help info button
        self.to_help_button = Button(self.button_frame, text = 'Help / Info', bg = '#CC6600', fg = BUTTON_FG ,font= BUTTON_FONT, width = 12, command=self.to_help)
        self.to_help_button.grid(row = 1, column = 0, padx = 5, pady=5)


    def to_help(self):
        DisplayHelp(self)


class DisplayHelp:

    def __init__(self, partner):
        BG = '#ffe6cc'
        self.help_box = Toplevel()

        # disable help button
        partner.to_help_button.config(state=DISABLED)

        # if user press cross at top, closes help button and releases help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))



        # frame of the GUI
        self.help_frame = Frame(self.help_box, width = 300, height = 200, bg = BG)
        self.help_frame.grid()


        # Heading of the GUI
        self.help_heading_label = Label(self.help_frame, bg = BG, text = 'Help / Info', font = ('Arial', '14', 'bold'))
        self.help_heading_label.grid(row = 0)

        # help text in the GUI
        help_text = 'To use this program, simply enter the temperature you wish to convert and then choose to convert it to either Celsius (centigrade) or Fahrenheit \n\nNote that -273  (-459 F) is absoulute 0, (the coldest possiable temperature). If you try to convert a tempuratture that is less then -273 degrees C, you will get an error message.\n\nTo see your calculation history and export it to a text file, please click the History / Export button'
        self.help_text_label = Label(self.help_frame, bg = BG, text = help_text, wrap = 350, justify = 'left')
        self.help_text_label.grid(row = 1, padx = 10)


        # dismmisal button for going back to converter GUI
        self.dismiss_button = Button(self.help_frame, font = ('Arial', '12', 'bold'), text = 'Dismiss', bg = '#CC6600', fg = '#FFFFFF', command = partial(self.close_help, partner))
        self.dismiss_button.grid(row = 2, padx = 10, pady = 10)

        # closes help dialouge (used by button and x at the top of dialouge)
    def close_help(self, partner):
        #put help button back to normal
        partner.to_help_button.config(state = NORMAL)
        self.help_box.destroy()

                            


# main routine
if __name__ == '__main__':
    root = Tk()
    root.title('Temputure Converter')
    #calling Converter Class
    Converter()
    root.mainloop()

