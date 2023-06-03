import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

#st.set_page_config(layout="wide")
####
st.header('データ活用支援　フレームワーク')
st.checkbox(label='Check')
st.slider(label='Slider')
st.selectbox(label='フレームワークを選択してください', options=['PEST', 'SWOT', 'クロスSWOT'])
####
image_1 = Image.open("PEST.jpg")
st.image(image_1, caption='PEST分析の解説', use_column_width=True) #width=700
####　PEST
col1, col2= st.columns([1, 1], gap="small")
with col1:
    st.text_area("P（Politics：政治的要因）", value=" ", key="text_input1") 
with col2:
    st.text_area("E（Economy：経済的要因）", value=" ", key="text_input2") 
####　PEST
col1, col2= st.columns([1, 1], gap="small")
with col1:
    st.text_area("S（Society：社会的要因）", value=" ", key="text_input3") 
with col2:
    st.text_area("T（Technology：技術的要因）", value=" ", key="text_input4") 

### 表（CSV）
dfg = pd.read_csv("WLAN.csv", encoding="shift-jis")
st.dataframe(dfg)

####
st.button("button") # ボタン
st.selectbox("selectbox", ("select1", "select2")) # セレクトボックス
st.multiselect("multiselectbox", ("select1", "select2")) # 複数選択可能なセレクトボックス
st.radio("radiobutton", ("radio1", "radio2")) # ラジオボタン
st.text_input("text input", key="text_input5") # 文字入力(1行)
st.text_area("text area") # 文字入力(複数行)
st.slider("slider", 0, 100, 50,key="slider1") # スライダー

## サイドバー
st.sidebar.text_input("text input", key="text_input6")
st.sidebar.text_area("text area", key="text_input7")
st.sidebar.slider("slider", 0, 100, 50,key="slider2")

## ファイルアップロード
file_name1 = "図/スライド1.jpg"
uploaded_file=st.file_uploader("ファイル選択",key="file_uploader2",type='jpg')

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    st.image(image, caption='upload images',width=200)

## 地図
df = pd.DataFrame(
     np.random.randn(10, 2) / [50, 50] + [35.51, 139.56],columns=['lat', 'lon'])
st.map(df)
