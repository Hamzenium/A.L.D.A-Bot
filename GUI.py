import collections
import collections.abc
from kivy.uix.label import Label
import script_text as st
from kivy.uix.boxlayout import BoxLayout


# # GUI Part
# import PySimpleGUI as sg
# layout = [
#              [sg.Text("Please enter the folder path: "), sg.Input(key="-IN-"), ],
#             [sg.Text("Please enter the final folder path: "), sg.Input(key="-out-"), ],
#              [sg.Exit(), sg.Button("Run")], ],
#
# window = sg.Window("\t\tA.L.D.A BOT", layout, [50, 50])
# while True:
#     event, values = window.read()
#     print(event, values)
#     if event in (sg.WINDOW_CLOSED, "Exit"):
#         break
#     if event == "Run":
#         str = values[r"-IN-"]
#         str1 = values[r"-out-"]
#         result = st.path_adder(str)
#         st.batch_processor(result, str, str1)
#
# window.close()

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.core.text import LabelBase
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    result = ObjectProperty(None)

    def callback(self):
        str = '/Users/muhammadhamzasohail/Desktop/Tester_ALDA'
        str1 = '/Users/muhammadhamzasohail/Desktop/Summary_files'
        result = st.path_adder(str)
        st.batch_processor(result, str, str1)
        exit()

    def select(self, *args):
        try: self.label.text = args[1][0]
        except: pass


class Display(App):
    def build(self):
        return MyGrid()



if __name__ == "__main__":
    Display().run()
