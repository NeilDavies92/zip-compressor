import PySimpleGUI as sg
from zip import make_archive

sg.theme("GrayGrayGray")

files_text = sg.Text("Choose File: ")
files_input = sg.Input()
files_browse = sg.FilesBrowse("Choose", key="files")

folder_text = sg.Text("Choose Destination: ")
folder_input = sg.Input()
folder_browse = sg.FolderBrowse("Choose", key="folder")

compress = sg.Button("ZIP")
exit_button = sg.Button("Exit")
output = sg.Text(key="output")

window = sg.Window(
    "ZIP Compressor",
    layout=[
        [files_text, sg.Push(), files_input, files_browse],
        [folder_text, sg.Push(), folder_input, folder_browse],
        [compress, output, sg.Push(), exit_button, sg.Push()],
    ],
)

while True:
    event, values = window.read()
    filepath = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepath, folder)
    window["output"].update(value="Zip file created.")

    if event == sg.WIN_CLOSED or event == "Exit":
        break

window.close()
