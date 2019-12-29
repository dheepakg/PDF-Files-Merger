import PySimpleGUI as sg


def sgui():
    sg.theme("Dark Blue 3")  # please make your windows colorful

    layout = [
        [sg.Text("PDF File Name 1")],
        [sg.Input(), sg.FileBrowse(file_types=(("PDF Files", "*.pdf"),))],
        [sg.Text("PDF File Name 2")],
        [sg.Input(), sg.FileBrowse(file_types=(("PDF Files", "*.pdf"),))],
        [sg.OK(), sg.Cancel()],
    ]

    window = sg.Window("PDF File Merger", layout)

    event, values = window.read()
    window.close()

    files = {1: values["Browse"], 2: values["Browse0"]}

    if event in ["Ok", "OK"]:
        sg.popup("Files are Merged")

    return files


file_dict = sgui()
print("files dict  is ", file_dict)
