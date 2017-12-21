import os
import tkFileDialog
import tkMessageBox
from Tkinter import *
import ttk
import json

title_str = "tk"
CODE = 0xA3
MAX = 100


class Application(Frame):

    def createWidgets(self):
        Label(self, text=self.labeltable["CHS"]["SRC_FILE"]).grid(row=0, column=0, sticky=E, padx=5, pady=5)
        Label(self, text=self.labeltable["CHS"]["DST_PATH"]).grid(row=1, column=0, sticky=E, padx=5, pady=5)
        Label(self, text=self.labeltable["CHS"]["DST_NAME"]).grid(row=2, column=0, sticky=E, padx=5, pady=5)

        src_entry = Entry(self, textvariable=self.src_pathname)
        self.dst_path_entry = dst_path_entry = Entry(self, textvariable=self.dst_path)
        self.dst_name_entry = dst_name_entry = Entry(self, textvariable=self.dst_name)

        src_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
        dst_path_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
        dst_name_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

        src_btn = Button(self, text=self.labeltable["CHS"]["SELECT_SRC"], command=self.select_file_callback)
        src_btn.grid(row=0, column=3, padx=5, pady=5)

        default_path_cbtn = Checkbutton(self, text=self.labeltable["CHS"]["DEFAULT_PATH"],
                                        variable=self.default_path, command=self.default_path_callback)
        default_path_cbtn.grid(row=1, column=3, padx=5, pady=5)

        default_name_cbtn = Checkbutton(self, text=self.labeltable["CHS"]["DEFAULT_NAME"],
                                        variable=self.default_name, command=self.default_name_callback)
        default_name_cbtn.grid(row=2, column=3, padx=5, pady=5)

        self.reset_btn = reset_btn = Button(self, text=self.labeltable["CHS"]["RESET"], command=self.reset_callback)
        self.start_btn = start_btn = Button(self, text=self.labeltable["CHS"]["START"], command=self.start_callback)
        self.exit_btn = exit_btn = Button(self, text=self.labeltable["CHS"]["EXIT"], command=self.exit_callback)

        reset_btn.grid(row=3, column=1, padx=5, pady=5)
        start_btn.grid(row=3, column=2, padx=5, pady=5)
        exit_btn.grid(row=3, column=3, padx=5, pady=5)

        self.progressbar = ttk.Progressbar(self, variable=self.progress, maximum=MAX,
                                           length=self.winfo_width()-10)
        self.progressbar.grid(row=4, column=0, columnspan=4, padx=5, pady=5)

    def __init__(self, master=None):
        global title_str
        Frame.__init__(self, master)
        f = open("labels.json", "r")
        self.labeltable = json.loads(f.read(), encoding='utf-8')
        f.close()
        title_str = self.labeltable["CHS"]["TITLE"]
        self.default_path = IntVar()
        self.default_name = IntVar()
        self.src_pathname = StringVar()
        self.dst_path = StringVar()
        self.dst_name = StringVar()
        self.dst_path_entry = None
        self.dst_name_entry = None
        self.progressbar = None
        self.progress = DoubleVar()
        self.reset_btn = None
        self.start_btn = None
        self.exit_btn = None
        self.pack()
        self.createWidgets()

    def select_file_callback(self):
        filename = tkFileDialog.askopenfilename(initialdir="./", title="Select file",
                                                filetypes=(("cache files", "*.uc!"), ("all files", "*.*")))
        self.src_pathname.set(filename)
        print (filename)

    def default_path_callback(self):
        default_path = self.default_path.get()
        if default_path == 1:
            self.dst_path_entry.config(state=DISABLED)
        else:
            self.dst_path_entry.config(state=NORMAL)

    def default_name_callback(self):
        default_name = self.default_name.get()
        if default_name == 1:
            self.dst_name_entry.config(state=DISABLED)
        else:
            self.dst_name_entry.config(state=NORMAL)

    def reset_callback(self):
        self.src_pathname.set("")
        self.dst_path.set("")
        self.dst_name.set("")
        self.default_path.set(0)
        self.default_name.set(0)
        self.dst_path_entry.config(state=NORMAL)
        self.dst_name_entry.config(state=NORMAL)

    def exit_callback(self):
        self.quit()

    def start_callback(self):
        self.reset_btn.config(state=DISABLED)
        self.start_btn.config(state=DISABLED)
        self.exit_btn.config(state=DISABLED)
        src = self.src_pathname.get()
        default_path = self.default_path.get()
        default_name = self.default_name.get()
        if len(src) == 0:
            tkMessageBox.showerror(self.labeltable["CHS"]["TITLE"], self.labeltable["CHS"]["SRC_EMPTY_ERR"])
            self.reset_btn.config(state=NORMAL)
            self.start_btn.config(state=NORMAL)
            self.exit_btn.config(state=NORMAL)
            return

        last_sep = src.rfind(os.path.sep)
        if default_path == 1:
            dst_path = src[:last_sep + 1]
        else:
            dst_path = self.dst_path.get()
            if len(dst_path) == 0:
                tkMessageBox.showerror(self.labeltable["CHS"]["TITLE"],
                                       self.labeltable["CHS"]["DSTPATH_EMPTY_ERR"])
                self.reset_btn.config(state=NORMAL)
                self.start_btn.config(state=NORMAL)
                self.exit_btn.config(state=NORMAL)
                return
            dst_path += os.path.sep if dst_path[-1] != os.path.sep else ""

        if default_name == 1:
            dest = dst_path + src[last_sep + 1: last_sep + src[last_sep:].find(".")] + ".mp3"
        else:
            if len(self.dst_name.get()) == 0:
                tkMessageBox.showerror(self.labeltable["CHS"]["TITLE"],
                                       self.labeltable["CHS"]["DSTNAME_EMPTY_ERR"])
                return
            dest = dst_path + self.dst_name.get()
            dest += ".mp3" if dest[-4:] != ".mp3" else ""

        rs = self.decode(src, dest)
        self.reset_btn.config(state=NORMAL)
        self.start_btn.config(state=NORMAL)
        self.exit_btn.config(state=NORMAL)
        if rs is None:
            tkMessageBox.showinfo(self.labeltable["CHS"]["TITLE"], self.labeltable["CHS"]["SUCCESS"])
        else:
            tkMessageBox.showerror(self.labeltable["CHS"]["TITLE"], self.labeltable["CHS"]["ERR"]+rs)

    def decode(self, origin_filepath, result_filepath):
        try:
            fin = open(origin_filepath, "rb")
        except IOError as e:
            print(str(e))
            return str(e)

        try:
            fout = open(result_filepath, "wb")
        except IOError as e:
            print(str(e))
            return str(e)

        music = fin.read()
        music_length = len(music)
        print("Source file length: %s" % music_length)
        music_decode = bytearray()
        for i, byte in enumerate(music):
            music_decode.append(int(byte.encode('hex'), 16) ^ CODE)
            progress = (i+1) * 100
            if progress % music_length == 0:
                print("\rProgress: %d%% %d" % (progress / music_length, i)),
                self.progress.set(progress / music_length)
                self.progressbar.update()
        print()
        fout.write(music_decode)
        fin.close()
        fout.close()
        return None

root = Tk()
app = Application(master=root)
app.master.title(title_str)
app.master.maxsize(960, 360)
root.update()
print(root.winfo_width(), root.winfo_reqwidth(), root.winfo_screenwidth(), root.winfo_geometry())
app.progressbar.config(length=root.winfo_reqwidth()-10)
app.mainloop()
# root.destroy()
