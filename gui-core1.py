from tkinter import Tk, Text, BOTH, W, N, E, S, filedialog, END, StringVar
from tkinter.ttk import Frame, Button, Label, Style
from pathlib import PurePath
from PyPDF2 import PdfFileMerger, PdfFileReader

defaultFilePath = "/home/dheepak/Desktop"

class Example(Frame):
    """GUI Component"""

    def __init__(self):
        super().__init__()
        self.f_initUI()

        self.list_fileName = []
        self.dict_fileNameInOrder = dict()
        self.dict_fileDetailsInOrder = dict()
        self.var_contents = ''

    def f_initUI(self):
        self.var = StringVar()
        self.var.set(" ")
        self.master.title("FileMerger")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        headerLabel = Label(self, text="Files list ")
        headerLabel.grid(sticky=W, pady=4, padx=5)

        FileListLabel = Label(self, text="", textvariable=self.var)
        FileListLabel.grid(row=1, column=0)

        addFilesButton = Button(self, text="Add files", command=self.f_selectFiles)
        addFilesButton.grid(row=1, column=3)

        removeButton = Button(self, text="Remove", command=self.f_removeLastFile)
        removeButton.grid(row=2, column=3)

        mergeButton = Button(self, text="Merge", command=self.f_mergePDF)
        mergeButton.grid(row=3, column=3, pady=4)

        helpButton = Button(self, text="Help")
        helpButton.grid(row=5, column=0, padx=5)

        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.grid(row=5, column=3)

    def f_selectFiles(self):
        """Used to select PDF files from  defaultFilePath"""
        self.pdfFile = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")], initialdir = defaultFilePath)
        self.list_fileName.append(self.pdfFile)

        self.var_contents = self.var_contents + '\n' + PurePath(self.pdfFile).name
        self.var.set(self.var_contents)
        self.dict_fileDetailsInOrder[len(self.list_fileName)] = self.pdfFile

    def f_removeLastFile(self):
        """Remove last selected file"""
        self.var_contents = ""
#        Removing file from list
        self.list_fileName.pop()
#        Displaying updated file-list in the GUI
        for filename in self.list_fileName:
            self.var_contents = self.var_contents + '\n' + PurePath(filename).name
        self.var.set(self.var_contents)

    def f_mergePDF(self):

        if len(self.list_fileName) < 2:
            print("Not enough files")
            self.var_contents = self.var_contents + "\nSelect atleast 2 files to merge"
            self.var.set(self.var_contents)
        else:
            merger = PdfFileMerger()
            for filename in self.list_fileName:
                merger.append(PdfFileReader(filename, 'rb'))

            merger.write("/home/dheepak/Desktop/document-output.pdf")

            self.var_contents = self.var_contents + "\nFiles are merged!"
            self.var.set(self.var_contents)




def main():

    root = Tk()
    root.geometry("600x300+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
