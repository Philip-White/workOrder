import kivy
from kivy.app import App
from kivy.uix.label import Label
import sqlite3
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button



class MyGrid(GridLayout):

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.make_sure = True # this is set so you can't keep making calls and piling up more 
                                     # and more widgets that won't go away!!

        self.cols = 1 # Set columns for main layout
        self.inner = GridLayout()
        self.inner.cols = 2

        self.inner.add_widget(Label(text="Part: "))
        self.inner.rows1 = TextInput(multiline=False)
        self.inner.add_widget(self.inner.rows1)
        self.add_widget(self.inner) # Add the interior layout to the main

                
        self.search = Button(text="Search", font_size=40)
        self.search.bind(on_press=self.pressed)
        self.add_widget(self.search)


        self.clear = Button(text="Clear Results", font_size=40)
        self.clear.bind(on_press=self.cleared)
        self.add_widget(self.clear)

    def pressed(self, instance):
        if self.make_sure != False:
            part = self.inner.rows1.text + '%'
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

    def cleared(self, instance):
        if self.make_sure != True:
            self.results.clear_widgets()
            self.remove_widget(self.results)
            self.make_sure = True



            
class MainApp(App):
    def build(self):
       return MyGrid()
        

if __name__ == '__main__':
    app = MainApp()
    app.run()