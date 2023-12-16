import streamlit as st
from PIL import Image
import os

path = "C:/Users/detri/OneDrive/바탕 화면/jupyter_home/streamlit_test/"
# path = "/mount/src/streamlit_test/"






main_image = Image.open(path + 'images/사랑동이.PNG')
# st.set_page_config(
#     page_title = "아무튼 웹페이지임",
#     page_icon = path + "단데기"
# )

st.title('Auto 소개')

st.image(main_image)
st.sidebar.success("Select page")

st.header("0. 왼쪽 상단의 > 버튼 눌러 탭 오픈")

st.subheader("1. 이성을 찾고 싶다면?")
st.write("1-1. 이성의 프로필 확인")
st.write("1-2. 마음에 드는 사람의 오픈채팅에 들어가 대화")
st.write("1-3. ><")

st.subheader("2. 자기를 등록하고 싶다면")
st.write("2-1. form 클릭")
# st.write("2-1. 신규/수정/삭제 선택")
st.write("2-2. 정보 작성")
st.write("2-3. 관리자 코드 입력 후 전송")
