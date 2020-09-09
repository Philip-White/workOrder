import kivy
from kivy.app import App
from kivy.uix.label import Label
import sqlite3
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock




class FirstScreen(Screen):
    
    
    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)
        self.make_sure = True # this is set so you can't keep making calls and piling up more 
                                     # and more widgets that won't go away!!
        

    def pressed(self):
        


        if self.make_sure != False:
            part = self.ids.part.text + '%'
            if part == '%':
                return
            else:    
                with sqlite3.connect("backUp.sqlite") as db:
                    cursor = db.cursor()
                rows = cursor.execute('select "Part Descripion" from backUp where "Part Descripion" like? limit 20', (part,))
                self.rows2 = cursor.fetchall()

                self.results = GridLayout()
                self.results.cols = 2
                for x in self.rows2:
                    self.results.add_widget(Label(text=str(x[0])))
                self.add_widget(self.results)  
                self.make_sure = False  
        else:
            return
 
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