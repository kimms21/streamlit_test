import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from deta import Deta

drive_name = 'people_image'
db_name = 'people_feature'
conn_image = Deta(st.secrets[drive_name])
conn_db = Deta(st.secrets[db_name])
drive_image = conn_image.Drive(drive_name)
db = conn_db.Base(db_name)



people_json = db.fetch().items
people_db = pd.DataFrame(people_json)

tab_titles = ["신규", "삭제"]
tabs = st.tabs(tab_titles)

with tabs[0]:
   with st.form("new"):
      is_error = False
      name = st.text_input(label = "별명입력",value = "단데기")
      sex = st.selectbox(label = "성별", options=["남자","여자"])
      age = st.number_input(label = "나이",value = 25)
      height = st.number_input(label = "키(cm)",value = 180)
      mbti = st.text_input(label="MBTI",value = "ISTP")
      introduce = st.text_area(label = "자기소개",value = "성격, 사는곳 등 자유롭게 적어주세요")
      openchat = st.text_input(label="오픈챗_url",value = "오픈챗주소")
      permission = st.text_input(label="관리자코드")
      uploaded_file = st.file_uploader("이미지는 256x256 size로 바뀌어 업로드됩니다")
      submitted = st.form_submit_button("Submit")

      if submitted:
         if name in list(people_db["key"]):
            st.error('중복된 별명이 있습니다')
            is_error = True

         if permission not in ["ms"]:
            st.error('업로드 권한이 업습니다 관리자코드를 입력해주세요')
            is_error = True

         if uploaded_file is None:
            st.error('대표 이미지를 업로드 해주세요')
            is_error = True

         if is_error == True:
            st.stop()
            st.rerun()

         else:
            st.success("신규요청완료! (profile 페이지에서 확인하세요)")
            bytes_data = uploaded_file.getvalue()
            uploaded_image = Image.open(uploaded_file)
            uploaded_image_reiszed = uploaded_image.resize((256, 256))
            drive_image.put(f"{name}.PNG", data=bytes_data)
            db.put({"key": name, "sex": sex, "age": age, "height": height, "mbti": mbti, "introduce": introduce,
                    "openchat": openchat, "permission": permission})


with tabs[1]:
   with st.form("delete"):
      st.write("Inside the form")
      name_del = st.text_input(label = "별명입력",value = "단데기")
      submitted_del = st.form_submit_button("Submit")

      if submitted_del:
         if name_del not in list(people_db["key"]):
            st.error('사용자정보가 없습니다')
            st.stop()

         else:
            db.delete(name_del)
            drive_image.delete(f"{name_del}.PNG")
            st.success("삭제요청완료!")
