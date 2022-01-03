import streamlit as st
import pandas as pd
import smtplib

def app():
    df=pd.read_csv('sample.csv')
    d=df.nlargest(1,['cgpa'])
    st.dataframe(d)
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("20r21a0412@mlrinstitutions.ac.in","MLRIT@PREMCHAND")
    msg="congratulations! "
    msg+=d['roll_no']
    server.sendmail("20r21a0412@mlrinstitutions.ac.in","20r21a0411@mlrinstitutions.ac.in", msg)
    


