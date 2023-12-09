import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# path = "C:/Users/detri/OneDrive/바탕 화면/jupyter_home/streamlit_test/"
path = "/mount/src/streamlit_test/"



people_db = pd.read_csv(path + "db/people.csv", encoding = "cp949")
# st.set_page_config(
#     page_title = "아무튼 웹페이지임",
#     page_icon = ""
# )


with st.form("my_form"):
   st.write("Inside the form")
   name = st.text_input(label = "별명입력",value = "단데기")
   sex = st.selectbox(label = "성별", options=["남자","여자"])
   age = st.number_input(label = "나이",value = 25)
   height = st.number_input(label = "키(cm)",value = 180)
   job = st.text_input(label = "직업",value = "번데기")
   mbti = st.text_input(label="MBTI",value = "ISTP")
   introduce = st.text_area(label = "자기소개",value = "난단데기임")
   openchat = st.text_input(label="오픈챗_url",value = "오픈챗주소")
   permission = st.text_input(label="관리자코드")
   uploaded_file = st.file_uploader("Choose a file")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")

   if name in list(people_db["별명"]):
      st.error('중복된 별명이 있습니다')
      st.stop()
   
   if permission not in ["ms"]:
      st.error('업로드 권한이 업습니다 관리자코드를 입력해주세요')
      st.stop()

   row = [name,sex,age,height, job, mbti, introduce, openchat, permission]
   new_info = pd.DataFrame([row],columns = people_db.columns)
   added_db = pd.concat([people_db, new_info],axis = 0)
   added_db.to_csv(path + "db/people.csv", index = False, encoding="cp949")

   if uploaded_file is not None:
      uploaded_image = Image.open(uploaded_file)
      uploaded_image.save(f"{path}images/{sex}/{name}.PNG")


st.success("전송완료!")