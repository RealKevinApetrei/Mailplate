import tkinter as tk
from tkinter import filedialog
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import email, smtplib, ssl
from email import encoders
from email.mime.application import MIMEApplication
import mimetypes
import os

import config


context = ssl.create_default_context() # SSL Context Connection
filelist = []

SIGNATURES = { # Add HTML Encoding
    "Select Signature": """\
    This is an example Signature<br>"""
}

# TEMPLATES

def select_template_fun(): # TODO: Fix CC and BCC and add extra details box
    def browse_file(): # Select a file to open
        global filelist

        filelist = filedialog.askopenfilenames()
        files_attached_tk.set("Files Attached: " + str(len(filelist)))

    def send_mail():
        # (TO) VALUE

        to_variable_tk_get = to_variable_tk.get()
        to_email = to_variable_tk_get.replace(" ", "")

        # (CC) VALUE

        cc_variable_tk_get = cc_variable_tk.get()
        cc_email = cc_variable_tk_get.replace(" ", "")

        # (BCC) VALUE

        bcc_variable_tk_get = bcc_variable_tk.get()
        bcc_email = bcc_variable_tk_get.replace(" ", "")

        # (SUBJECT) VALUE

        subject_email = subject_variable_tk.get() + " (Example Template)"

        # (POINTS) VALUE(S)

        points_raw = points_variable_tk.get()
        points = points_raw.replace(",", "<br>- ")

        # (SIGNATURE) VALUE
        signature_email = SIGNATURES[selected_signature_option_tk.get()]

        # SEND EMAIL
        sender_email = config.email_sender
        reciever_email = to_email

        message = MIMEMultipart("alternative")
        message["Subject"] = subject_email
        message["From"] = sender_email
        message["To"] = reciever_email
        message["Cc"] = cc_email # TODO: Fix this
        message["Bcc"] = bcc_email # TODO: Fix this

        # Text Version
        text = """\
        Hi,

        This is an important message that you need to read.
        Please read the attached File.

        Here are some points:

        - {}

        {}

        """.format(points, signature_email)
        # HTML Version
        html = """\
        <html>
            <body>
                <p>Hi,<br><br>This is an important message that you need to read.</p>
                <p>Please read the attached file if there is on regarding payment details.<br>
                <br>Here are some payments you will need to complete:
                <br><br><strong>- {}</strong><br><br> <span style="color: rgb(128, 128, 128);"
                >{}</span></p>
            </body>
        </html>
        """.format(points, signature_email)

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/Plain parts to Multipart message
        # Email client will render last part first

        message.attach(part1)
        message.attach(part2)

        # Add attachments
        for file in filelist:
            mimetype, _ = mimetypes.guess_type(file)
            mimetype = "application/octet-stream" if mimetype is None else mimetype
            _, _, subtype = mimetype.partition("/")
            attachment_part = MIMEApplication(open(file, "rb").read(), subtype)
            attachment_part.add_header("Content-Disposition", "attachment; filename=%s" % os.path.basename(file))
            message.attach(attachment_part)

        # Create Server Connection
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(config.email_sender, config.email_password)
            server.sendmail(
                sender_email, reciever_email, message.as_string()
            )


    select_template_ui = tk.Tk()
    select_template_ui.title(f"Nottingham Serviced Apartments Emailer - {config.BUILD_VERSION} - by {config.AUTHOR}")
    select_template_ui.geometry("750x800")
    select_template_ui.resizable(0, 0)

    to_variable_tk = tk.StringVar()
    cc_variable_tk = tk.StringVar()
    bcc_variable_tk = tk.StringVar()

    subject_variable_tk = tk.StringVar()
    points_variable_tk = tk.StringVar()

    files_attached_tk = tk.StringVar()

    selected_signature_option_tk = tk.StringVar()
    selected_signature_option_tk.set("Select Signature")


    template_type_label = tk.Label(select_template_ui, text="Example Template", font="Helvetica 30 bold underline").place(x=375, y=50, anchor="center")

    to_label = tk.Label(select_template_ui, text="To:", font="System 13 bold").place(x=15, y=150, anchor="w")
    to_entry = tk.Entry(select_template_ui, textvariable=to_variable_tk, width="30").place(x=325, y=150, anchor="e")

    cc_label = tk.Label(select_template_ui, text="Cc:", font="System 13 bold").place(x=350, y=150, anchor="w")
    cc_entry = tk.Entry(select_template_ui, textvariable=cc_variable_tk, width="30").place(x=675, y=150, anchor="e")

    bcc_label = tk.Label(select_template_ui, text="Bcc:", font="System 13 bold").place(x=15, y=200, anchor="w")
    bcc_entry = tk.Entry(select_template_ui, textvariable=bcc_variable_tk, width="30").place(x=325, y=200, anchor="e")

    subject_label = tk.Label(select_template_ui, text="Subject:", font="System 15 bold").place(x=15, y=250, anchor="w")
    subject_entry = tk.Entry(select_template_ui, textvariable=subject_variable_tk, width="30").place(x=375, y=250, anchor="e")

    points_label = tk.Label(select_template_ui, text="Example List:", font="System 15 bold").place(x=15, y=350, anchor="w")
    points_entry = tk.Entry(select_template_ui, textvariable=points_variable_tk, width="60").place(x=675, y=350, anchor="e")


    files_attached_tk.set("Files Attached: " + str(len(filelist)))
    files_attached_label = tk.Label(select_template_ui, textvariable=files_attached_tk, font="bold", bg="gray").place(x=15, y=700, anchor="w")
    attach_files_button = tk.Button(select_template_ui, text="Attach File(s)", command=browse_file).place(x=200, y=700, anchor="w")


    signature_option_menu = tk.OptionMenu(select_template_ui, selected_signature_option_tk, *SIGNATURES.keys()).place(x=700, y=700, anchor="e")
    send_button = tk.Button(select_template_ui, text="Send Email", command=send_mail).place(x=425, y=700, anchor="center")


    current_email_login = tk.Label(select_template_ui, text=f"Logged in to [{config.email_sender}]", font="12").place(x=5, y=795, anchor="sw")
    select_template_ui.mainloop()


TEMPLATES = { # Template Name, Function
            "Select Template": select_template_fun,
            }


if __name__ == "__main__":
    print("Please run 'main.py' for proper use.")


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
