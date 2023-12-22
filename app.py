import streamlit as st
from PIL import Image
import streamlit_authenticator as stauth
import pickle
from pathlib import Path

names = ["ms","dy"]
usernames = ["kms", "ody"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_pw = pickle.load(file)
credentials = {
    "usernames":{
        usernames[0]:{
            "name":names[0],
            "password":hashed_pw[0]
            },
        usernames[1]:{
            "name":names[1],
            "password":hashed_pw[1]
            }
        }
    }
auth = stauth.Authenticate(credentials= credentials,  cookie_expiry_days=30, cookie_name="auto",key="asd")

name, auth_status, username = auth.login("login",'main')
if auth_status == False:
    st.error("AA")


if auth_status == None:
    st.error("BB")

if auth_status:


    auth.logout("logout","sidebar")
    path = "C:/Users/detri/OneDrive/바탕 화면/jupyter_home/streamlit_test/"
    # path = "/mount/src/streamlit_test/"
    main_image = Image.open('images/사랑동이.PNG')

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
