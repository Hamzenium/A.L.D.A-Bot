import script_text as st

# GUI Part
import PySimpleGUI as sg
layout = [
             [sg.Text("Please enter the folder path: "), sg.Input(key="-IN-"), ],
            [sg.Text("Please enter the final folder path: "), sg.Input(key="-out-"), ],
             [sg.Exit(), sg.Button("Run")], ],

window = sg.Window("\t\tA.L.D.A BOT", layout, [50, 50])
while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == "Run":
        str = values[r"-IN-"]
        str1 = values[r"-out-"]
        result = st.path_adder(str)
        st.batch_processor(result, str, str1)

window.close()