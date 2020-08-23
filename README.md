# Mailplate (End Of Life)
Mailplate is a templated emailer for business developers.

Requirements:
=============

- Python 3.x

- import tkinter as tk
- from tkinter import filedialog
- import email, smtplib, ssl
- from email.mime.text import MIMEText
- from email.mime.multipart import MIMEMultipart
- from email.mime.base import MIMEBase
- from email import encoders
- from email.mime.application import MIMEApplication
- import mimetypes
- import os

Developer Usage:
================

- Add HTML Encoded Signatures to your liking: (key="NAME", value="""HTML SIGNATURE""") (templates.SIGNATURES)
- Add Templates to your liking: (key="NAME", value=TEMPLATE_FUNCTION) (templates.TEMPLATES)

- Configure your own template by reference to Example Template function.

- Enter gmail login in config.py
- Make sure mail has enabled LESS SECURE APPS

(This program is very low-level and does not include result boxes or much exception handling.)

Make your own template:
  - Initialise UI similar to reference function.
  - Create TO, CC, BCC Entries similar to reference function.
  - Add your own extra entries. Make UI Larger if needed.
  - Create and send email using a send_email() function. Change/Remove/Add Variables using function reference.
  - Do not change anything other than (???) VALUE and text/html variable within the send_email() function.
  - Format HTML variable how you want your email to look.
  - Format HTML and TEXT variable with entry boxes.
  
  (You will need a basic understanding of Python3.x and Tkinter to create a template.)
  (Please note that this program was not intended for non-developer use during template creation.)
  
  
CREDITS AND NOTES:
==================

(Please note that this program was not intended for non-developer use during template creation.)

Programmed by: Kevin Apetrei
Twitter: @kevinapetrei

Thank you! This was a mini project but was scrapped due to lack of further use.
  
