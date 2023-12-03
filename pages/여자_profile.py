import streamlit as st
import numpy as np
from PIL import Image
import os

target_sex = "여자"
pjt_path = "C:/Users/detri/OneDrive/바탕 화면/jupyter_home/streamlit_test/"
# img_path = "C:/Users/detri/OneDrive/바탕 화면/jupyter_home/streamlit_test/images/"
img_path = "/mount/src/streamlit_test/images/"

# st.set_page_config(
#     page_title = "아무튼 웹페이지임",
#     page_icon = ""
# )

def batch(iterable, n=1):
   l = len(iterable)
   for ndx in range(0, l, n):
      yield iterable[ndx:min(ndx + n, l)]


st.title(f'{target_sex} Profile')
man_list = os.listdir(img_path+target_sex+"/")
cols = st.columns(len(man_list))

for idx, man_name in enumerate(man_list):

   with cols[idx % 2]:
      st.header(man_name.replace('.PNG', ''))
      man_image = Image.open(img_path + target_sex + "/" + man_name)
      st.image(man_image)
      st.write(f"상태 : 진행중")
      expander_stat = st.expander("profile")
      with expander_stat:
         st.write(f"키 : {np.random.randint(1,100)}")
         st.write(f"몸무게 : {np.random.randint(1,100)}")
      expander_introduce = st.expander("자기소개")
      with expander_introduce:
         expander_introduce.write("자기소개"+str(idx))
      expander_opentalk = st.expander("오픈톡 링크")
      with expander_opentalk:
         expander_opentalk.write("opentalk_url" + str(idx))





