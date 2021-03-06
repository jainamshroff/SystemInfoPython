# -*- coding: utf-8 -*-
"""Group assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fT4DP1w5WK-vF_8rl38m9eevIyNVEyAv
"""

import smtplib 
import psutil
import platform
import os
import ctypes, sys
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
from fpdf import FPDF 


def texttoPDF():
  pdf = FPDF()    
  pdf.add_page() 
  pdf.set_font("Arial", size = 15) 
  f = open("systeminfofinal.txt", "r") 
    
  # insert the texts in pdf 
  for x in f: 
      pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 
  
  pdf.output("SystemInfoJainamShroff.pdf")  

def writeFile(string):
  f = open("systeminfofinal.txt", "a")
  f.write("\n")
  f.write(string)
  f.close()

def fileInfo():
  cpupercentage = str(psutil.cpu_percent())
  placeholder = "CPU USAGE percentage: "
  placeholder = placeholder + cpupercentage
  writeFile(placeholder)
  placeholder = ""
  rampercentage = str(psutil.virtual_memory().percent)
  placeholder = "RAM USAGE percentage: "
  placeholder = placeholder + rampercentage
  writeFile(placeholder)
  placeholder = ""
  osname = str(os.name)
  placeholder = "OS Name: "
  placeholder = placeholder + osname
  writeFile(placeholder)
  placeholder = ""
  platformname = str(platform.system())
  placeholder = "Platform Name: "
  placeholder = placeholder + platformname
  writeFile(placeholder)
  placeholder = ""
  relversion = str(platform.release())
  placeholder = "Platform Release Version: "
  placeholder = placeholder + relversion
  writeFile(placeholder)
  placeholder = ""
  endian = str(sys.byteorder)
  placeholder = "Endianness: "
  placeholder = placeholder + endian
  writeFile(placeholder)
  placeholder = ""
  arch = str(platform.machine())
  placeholder = "architecture: "
  placeholder = placeholder + arch
  writeFile(placeholder)
  placeholder = ""
  texttoPDF()


def sendEmail(recvEmail, filename):

  fromaddr = "Sender's Email ID"
  toaddr = recvEmail

  # instance of MIMEMultipart 
  msg = MIMEMultipart() 

  # storing the senders email address 
  msg['From'] = fromaddr 

  # storing the receivers email address 
  msg['To'] = toaddr 

  # storing the subject 
  msg['Subject'] = "System Details"

  # string to store the body of the mail 
  body = "Below Attached is the PDF containing System details"

  # attach the body with the msg instance 
  msg.attach(MIMEText(body, 'plain')) 

  # open the file to be sent 
  attachment = open(filename, "rb") 

  # instance of MIMEBase and named as p 
  p = MIMEBase('application', 'octet-stream') 

  # To change the payload into encoded form 
  p.set_payload((attachment).read()) 

  # encode into base64 
  encoders.encode_base64(p) 

  p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

  # attach the instance 'p' to instance 'msg' 
  msg.attach(p) 

  # creates SMTP session 
  s = smtplib.SMTP('smtp.gmail.com', 587) 

  # start TLS for security 
  s.starttls() 

  # Authentication 
  s.login(fromaddr, "Sender's password") 

  # Converts the Multipart msg into a string 
  text = msg.as_string() 

  # sending the mail 
  s.sendmail(fromaddr, toaddr, text) 

  # terminating the session 
  s.quit() 



fileInfo()

sendEmail("Enter receiver's mail ID", "SystemInfoJainamShroff.pdf")