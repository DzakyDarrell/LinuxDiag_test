import tkinter as tk
from tkinter import messagebox
import subprocess

class InxiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LinuxDiag test 1.0 beta")

        self.theme = "light"
        self.apply_theme()

        # Output area
        self.output = tk.Text(self.root, wrap="word", height=30, width=100)
        self.output.pack(fill="both", expand=True)

        # Build menu
        menubar = tk.Menu(self.root, tearoff=False)

        # Direct command menus (no submenus)
        menubar.add_command(label="Full Info", command=lambda: self.run_inxi("inxi -b"))
        menubar.add_command(label="Audio", command=lambda: self.run_inxi("inxi -A"))
        menubar.add_command(label="Battery", command=lambda: self.run_inxi("inxi -B"))
        menubar.add_command(label="CPU", command=lambda: self.run_inxi("inxi -C -I"))
        menubar.add_command(label="GPU", command=lambda: self.run_inxi("inxi -G"))
        menubar.add_command(label="Disk", command=lambda: self.run_inxi("inxi -D -d"))
        menubar.add_command(label="Memory", command=lambda: self.run_inxi("inxi -m -j"))
        menubar.add_command(label="Device", command=lambda: self.run_inxi("inxi -M -J"))
        menubar.add_command(label="Network", command=lambda: self.run_inxi("inxi -N -E"))

        # Options (submenu)
        options = tk.Menu(menubar, tearoff=False)

        theme_menu = tk.Menu(options, tearoff=False)
        theme_menu.add_command(label=" Light ", command=lambda: self.set_theme("light"))
        theme_menu.add_command(label=" Dark ", command=lambda: self.set_theme("dark"))

        options.add_cascade(label=" Theme ", menu=theme_menu)
        options.add_separator()
        options.add_command(label=" Help ", command=self.show_help)
        options.add_command(label=" About ", command=self.show_about)

        menubar.add_cascade(label="Options", menu=options)

        self.root.config(menu=menubar)

        # Auto-load full system info on launch
        self.run_inxi("inxi -b")

    def run_inxi(self, cmd):
        self.output.delete("1.0", tk.END)
        try:
            result = subprocess.check_output(cmd.split(), stderr=subprocess.STDOUT).decode()
        except Exception as e:
            result = f"Error:\n{e}"
        self.output.insert(tk.END, result)

    def set_theme(self, mode):
        self.theme = mode
        self.apply_theme()

    def apply_theme(self):
        if self.theme == "dark":
            bg = "#1e1e1e"
            fg = "#e0e0e0"
        else:
            bg = "#ffffff"
            fg = "#000000"

        self.root.configure(bg=bg)
        try:
            self.output.configure(bg=bg, fg=fg, insertbackground=fg)
        except:
            pass

    def show_help(self):
        messagebox.showinfo(
            "Help",
            "-Click any menu item to shows system info.\n"
            "-You can change theme under Options."
        )

    def show_about(self):
        messagebox.showinfo(
            "About",
            "-LinuxDiag 1.0 beta\n-Build using Python + Tkinter\n-Shows system info using inxi."
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = InxiApp(root)
    root.mainloop()
