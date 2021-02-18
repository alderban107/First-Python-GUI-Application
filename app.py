import PySimpleGUI as sg
import random

sg.theme(random.choice(sg.theme_list())) # chooses a random theme
layout = [[sg.Button('List themes'), sg.Button('Cancel')]] # layout, used in window
window = sg.Window('Window Theme Program', layout) # creates window
themeWindow = None # declares themeWindow variable
while True: # event loop
    event, _ = window.read()
    if themeWindow: # if themeWindow has been instantiated
        theme_event, theme_values = themeWindow.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'List themes': # if user presses 'List themes' button
        layout2 = [[sg.Listbox(values=sg.theme_list(), size=(700, 700))]] # layout, used in themeWindow
        themeWindow = sg.Window('Theme List', layout2, size=(800, 800)) # creates themeWindow window
        themeWindow.read()

window.close() # Closes window