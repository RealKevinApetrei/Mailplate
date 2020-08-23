import tkinter as tk

import config
from templates import *


# MAIN

def main_menu(): # Main Menu UI
    global selected_template_option
    global main_menu_tk


    main_menu_tk = tk.Tk()
    main_menu_tk.title(f"Mailplate - {config.BUILD_VERSION} - by {config.AUTHOR}")
    main_menu_tk.geometry("750x800")
    main_menu_tk.resizable(0, 0)

    selected_template_option = tk.StringVar() # Select Template Variable
    selected_template_option.set("Select Template") # Default Value


    main_menu_title = tk.Label(main_menu_tk, text="Mailplate", font="Helvetica 30 bold underline").place(x=375, y=100, anchor="center")
    main_menu_credits = tk.Label(main_menu_tk, text=f"Emailer - {config.BUILD_VERSION} - by {config.AUTHOR}", font="Helvetica 18 bold").place(x=375, y=150, anchor="center")

    template_option_menu = tk.OptionMenu(main_menu_tk, selected_template_option, *TEMPLATES.keys()).place(x=375, y=250, anchor="center")

    use_template_button = tk.Button(main_menu_tk, text="Use template", command=process_template_choice).place(x=375, y=300, anchor="center")


    current_email_login = tk.Label(main_menu_tk, text=f"Will log in to [{config.email_sender}]", font="12").place(x=5, y=795, anchor="sw")
    main_menu_tk.mainloop()


def process_template_choice():
    wanted_template = selected_template_option.get()
    main_menu_tk.destroy()
    TEMPLATES[wanted_template]()


if __name__ == "__main__":
    main_menu()
else:
    print("Run file directy for proper use.")


# MIT License
#
# Copyright (c) [year] [fullname]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
