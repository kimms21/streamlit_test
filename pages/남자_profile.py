import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import os

target_sex = "남자"
# path = "C:/Users/detri/OneDrive/바탕 화면/jupyter_home/streamlit_test/"
path = "/mount/src/streamlit_test/"





# st.set_page_config(
#     page_title = "아무튼 웹페이지임",
#     page_icon = ""
# )

db = pd.read_csv(path+"db/people.csv",encoding = "cp949")
db_man = db[db["성별"]==target_sex]


st.title(f'{target_sex} Profile')
man_list = os.listdir(path+"images/"+target_sex+"/")
cols = st.columns(len(man_list))

for idx, row in db_man.iterrows():
   man_name, sex, age, height, job, mbti, introduce, opentalk, permission = row
   with cols[idx % 2]:
      st.header(man_name)
      man_image = Image.open(f"{path}images/{target_sex}/{man_name}.PNG")
      st.image(man_image)
      expander_stat = st.expander("profile")
      with expander_stat:
         st.write(f"키 : {height}")
         st.write(f"직업 : {job}")
         st.write(f"MBTI : {mbti}")

      expander_introduce = st.expander("자기소개")
      with expander_introduce:
         expander_introduce.write(introduce)
      expander_opentalk = st.expander("오픈톡 링크")
      with expander_opentalk:
         expander_opentalk.write(opentalk)




