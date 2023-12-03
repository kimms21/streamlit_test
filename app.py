import streamlit as st
from PIL import Image


pjt_path = "C:/Users/detri/OneDrive/바탕 화면/jupyter_home/streamlit_test/"
img_path = "C:/Users/detri/OneDrive/바탕 화면/jupyter_home/streamlit_test/images/"
main_image = Image.open(img_path + '단데기.png')

# st.set_page_config(
#     page_title = "아무튼 웹페이지임",
#     page_icon = path + "단데기"
# )

st.title('아무튼 웹페이지임')

st.image(main_image)
st.sidebar.success("Select page")


# col1, col2 = st.columns([1,1])
#
# with col1:
#     st.link_button('남자',"https://www.youtube.com/watch?v=g8Deu7a9rS8")
# with col2:
#     st.button('여자')