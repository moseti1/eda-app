import streamlit as st 
import pandas as pd 
import plotly.express as px 
import numpy as np



st.title('A simple EDA app')


st.markdown("""
this app performs EDA
* ** Python libraries:** streamlit, pandas, ...
* ** Need to contract ** 
""")


file_bytes = st.file_uploader("Upload a file", type="csv")

if file_bytes is not None:
    data = pd.read_csv(file_bytes)
    obj = []
    int_float = []
    for i in data.columns:
        clas = data[i].dtypes 
        if clas == 'object':
            obj.append(i)
            
        else:
            int_float.append(i)
            
            
    # Adding a submit button sidebar        
    with st.form(key='my_form'):
        with st.sidebar:
            st.sidebar.header("To remove Null Values press the below button")
            submit_button = st.form_submit_button(label = 'Remove Null')
            
    # If we click Remove Null button Null values will replace with mean and mode
    if submit_button:
        for i in data.columns:
            clas = data[i].dtypes 
            if clas == 'object':
                data[i].fillna(data[i].mode()[0], inplace=True)
            else: 
                data[i].fillna(data[i].mean(), inplace=True)
                
                
    # Finding number of null values in each column
    
    lis = []
    dd = sum(pd.isnull(data[i]))
    lis.append(dd)
    
    
    # if no null values are zero it will display some tex else it will display bar plot by each column.
    if max(lis) == 0:
        st.write("Total no. of Null Values   "+ str(max(lis)))
                 
    else:
        st.write("Bar plot to know no. of Null values in each column")
        st.write("Total no. of Null Values   "+ str(max(lis)))
        fig2 = px.bary(x=data.columns, y=lis, labes={'x':"Columns Names", 'y':"No. of Null Values"})
        st.plotly_chart(fig2)
                 
                 
    
    # Frequency plot 
    st.sidebar.header("Select Variable")
    selected_pos = st.sidebar.selectbox('Object Variable', obj)
    st.write("Bar Plot to know frequency of each category")
    frequency_data = data[selected_pos].value_counts()
    fig = px.bar(frequency_data, x=frequency_data.index, y=selected_pos, labels={'x':selected_pos, 'y':'count'})
    st.plotly_chart(fig)
    
    # Histogram 
    st.sidebar.header("Select Variable")
                 
    selected_pos1 = st.sidebar.selectbox("Int of Float Variables", int_float)
    st.write("Bar Plot to know count of values based on range")
    counts, bins = np.histogram(data[selected_pos1], bins=range(int(min(data[selected_pos1])), int(max(data[selected_pos1]))))
    bins = 0.5 * (bins[:-1] + bins[1:])
    fig1 = px.bar(x=bins, y=counts, labels={'x':selected_pos1, 'y':'count'})
  
    st.plotly_chart(fig1) 
    
    
    # correlation plot 
    
              
