from tkinter import Tk,BOTH, W, filedialog, StringVar
from tkinter.ttk import Frame, Button, Label
from pathlib import PurePath
from PyPDF2 import PdfFileMerger, PdfFileReader
import os
import sys
from datetime import datetime
import logging




class theCore(Frame):
    """GUI Component"""

    def __init__(self):
        super().__init__()
        self.f_initUI()

        self.list_fileName = []
        self.dict_fileNameInOrder = dict()
        self.dict_fileDetailsInOrder = dict()
        self.var_contents = ''

    def f_initUI(self):
        try:
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

        except:
            logging.debug("Something wrong with GUI component")
        finally:
            logging.debug("GUI component executed successfully")

    def f_selectFiles(self):
        """Used to select PDF files"""

        # Selects files of type PDF
        self.pdfFile = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        self.list_fileName.append(self.pdfFile)
        # var_contents holds the value to be displayed on the GUI window
        self.var_contents = self.var_contents + '\n' + PurePath(self.pdfFile).name
        self.var.set(self.var_contents)
        # Dictionary is used to retain the order of file selection by the user
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
            # To warn if only one file was asked to merge
            logging.debug("Not enough files")
            self.var_contents = self.var_contents + "\nSelect atleast 2 files to merge"
            self.var.set(self.var_contents)
        else:
            merger = PdfFileMerger()
            for filename in self.list_fileName:
                merger.append(PdfFileReader(filename, 'rb'))
            merger.write(output_file_name)
            logging.debug('Output file is %s',output_file_name)

            self.var_contents = self.var_contents + "\nFiles are merged!"
            self.var.set(self.var_contents)


def main():
    logging.debug('Start of core operation')

    root = Tk()
    root.geometry("600x300+300+300")
    theCore()
    root.mainloop()


if __name__ == '__main__':

    # Identifying the os path where the script is running
    abs_file_path = os.path.dirname(sys.argv[0]) + '/'
    file_gen_time = str(datetime.today().strftime('%Y%m%d-%H%M%S'))
    output_file_name = abs_file_path + 'Merged on ' + file_gen_time + '.pdf'

    config_directory = abs_file_path + '.PDF-merger.config'

    if not os.path.exists(config_directory):
        os.makedirs(config_directory)
        log_init = "The config folder was created"
    else:
        log_init = "The config folder already exists"

    log_file = config_directory + '/PDF-Merger.log'

    logging.basicConfig(level=logging.DEBUG, filename=log_file, filemode='a',format='%(asctime)s - %(levelname)s - %(message)s')
    logging.debug('%s',log_init)

    main()
