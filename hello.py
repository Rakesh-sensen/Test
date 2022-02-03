import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
from PIL import Image

io = ExcelFile(io, storage_options=storage_options, engine=engine)
df=pd.read_excel('https://github.com/Rakesh-sensen/Test/blob/main/sensen1.xlsx')


df['Start Date']=pd.to_datetime(df['Start Date']).dt.date
df['End Date']=pd.to_datetime(df['End Date']).dt.date


try:
    tip=st.sidebar.text_input("search with Employe name").title()
    tip=tip.split(",")
    dtf=df['Surname'].isin(tip)
    dtf=df[dtf]
   
except Exception as e:
    print(e)


project=st.sidebar.selectbox('project',list(['France','Spain','Germany']))


#names=df.columns.unique()
#names=list(names)
#st.sidebar.multiselect('Names Of The columns',names,names)



i=Image.open('download.png')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.image(i)

st.title('''SenSen Networks''')
st.write("""**Test web page**
* **python Libraries used :** Pandas,streamlit,seaborn""")

st.header('DataSet')
st.dataframe(df)



with st.expander("Employee Details"):
    st.dataframe(dtf)





#st.header('Resources For Project')
if project=='France':
    df1=pd.DataFrame(df['Surname'][df['Projects']=='France'])
    with st.expander("Resources For Project"):
        st.dataframe(df1)
if project=='Spain':
    df1=pd.DataFrame(df['Surname'][df['Projects']=='Spain'])
    with st.expander("Resources For Project"):
        st.dataframe(df1)
if project=='Germany':
    df1=pd.DataFrame(df['Surname'][df['Projects']=='Germany'])
    with st.expander("Resources For Project"):
        st.dataframe(df1)


search=st.sidebar.text_input('Start_date(YY-DD-MM)', '2021-01-11')
search0=pd.to_datetime(search)
search=df.loc[(df['Start Date']==search0)]
#st.header('Data as per the Start Date')
with st.expander("Data as per the Start Date"):
    st.dataframe(search)


search1=st.sidebar.text_input('End_date(YY-DD-MM)', '2021-05-11')
search10=pd.to_datetime(search1)
search1=df.loc[df['Start Date']==search10]
#st.header('Data as per the End Date')
with st.expander("Data as per the End Date"):
    st.dataframe(search1)

df5=df[df['Start Date'].between(search0,search10)]

with st.expander("Data as per the Test Date"):
    st.dataframe(df5)



st.header('Data Analysis On Number Of Resources per Project')
st.write("""* **X-axis :** Number Of Employees
* **Y-axis :** Name Of Projects""")



try:
    try:
        uploaded_file = st.file_uploader(label="Choose a file",type=['csv','xlsx'])
        ddf=pd.read_csv(uploaded_file)
    
    except Exception as e:
        print(e)
        ddf=pd.read_excel(uploaded_file)
    

   
    st.write(ddf)
    
except Exception as e:
    print(e)
