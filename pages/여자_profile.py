import streamlit as st
import pandas as pd
from PIL import Image
from deta import Deta
import io

target_sex = "여자"


drive_name = 'people_image'
db_name = 'people_feature'
conn_image = Deta(st.secrets[drive_name])
conn_db = Deta(st.secrets[db_name])

# Define the drive to store the files.

drive_image = conn_image.Drive(drive_name)
db = conn_db.Base(db_name)

people_json = db.fetch().items
people_db = pd.DataFrame(people_json)
db_man = people_db[people_db["sex"]==target_sex]


st.title(f'{target_sex} Profile')
cols = st.columns(len(db_man))

for idx, row in db_man.iterrows():

   with cols[idx % 2]:
      st.header(row["key"])
      man_image_get =drive_image.get(f"{row['key']}.PNG").read()
      man_image = Image.open(io.BytesIO(man_image_get))
      man_image_resized = man_image.resize((256, 256))
      st.image(man_image_resized)
      expander_stat = st.expander("profile")
      with expander_stat:
         st.write(f"키 : {row['height']}")
         st.write(f"나이 : {row['age']}")
         st.write(f"MBTI : {row['mbti']}")

      expander_introduce = st.expander("자기소개")
      with expander_introduce:
         expander_introduce.write(row['introduce'])
      expander_opentalk = st.expander("오픈톡 링크")
      with expander_opentalk:
         expander_opentalk.write(row['openchat'])




