import kivy
from kivy.app import App
from kivy.uix.label import Label
import sqlite3
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from functools import partial


class FirstScreen(Screen):
    
    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)
        self.make_sure = True # this is set so you can't keep making calls and piling up more 
                                     # and more widgets that won't go away!!
        

    def one(self):
        show_one = self.ids.one.text
        popupWindow1 = Popup(title="Popup Window", content=Label(text=str(show_one)), size_hint=(None,None),size=(400,400)) 
        # Create the popup window

        popupWindow1.open() # show the popup
        self.make_sure = False


    def two(self):
        show_two = self.ids.two.text
        popupWindow2 = Popup(title="Popup Window", content=Label(text=str(show_two)), size_hint=(None,None),size=(400,400)) 
        # Create the popup window

        popupWindow2.open() # show the popup
        self.make_sure = False

    def three(self):
        show_three = self.ids.three.text
        popupWindow3 = Popup(title="Popup Window", content=Label(text=str(show_three)), size_hint=(None,None),size=(400,400)) 
        # Create the popup window

        popupWindow3.open() # show the popup
        self.make_sure = False


    def pressed(self):#This is triggered from the submit button

        if self.make_sure != False:
            part = self.ids.part.text + '%'
            if part == '%':
                return
            else:    
                with sqlite3.connect("backUp.sqlite") as db:
                    cursor = db.cursor()
                rows = cursor.execute('select "Part Descripion" from backUp where "Part Descripion" like? limit 3', (part,))
                self.rows2 = cursor.fetchall()
                if self.rows2:
                    for x in self.rows2:
                        #stuff = Button(text=str(x[0]))
                        #stuff.bind(on_press=self.show_popup)
                        #self.ids.last_thing.add_widget(stuff)
                        #namers.append(stuff.text)
                        one, two, three = self.rows2
                        self.ids.one.text = str(one[0])
                        self.ids.two.text = str(two[0])
                        self.ids.three.text = str(three[0])
                    self.make_sure = False
                else:
                    return      
        else:
            return

    def cleared(self):#This is triggered by the 'clear results' button
        if self.make_sure != True:
            #self.ids.last_thing.clear_widgets()
            self.ids.one.text = ''
            self.ids.two.text = ''
            self.ids.three.text = ''
            self.make_sure = True
 
class SecondScreen(Screen):
    pass

class ThirdScreen(Screen):
    pass

class FourthScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

        



            
class SwitcherScreenApp(App):

    def build(self):
        
        return MyScreenManager()

if __name__ == '__main__':
    app = SwitcherScreenApp()
    app.run()