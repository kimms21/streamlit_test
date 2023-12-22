import streamlit as st
from PIL import Image
import streamlit_authenticator as stauth
import pickle
from pathlib import Path

names = ["ms","dy"]
usernames = ["kms", "ody"]
passwords = ["kms", "ody"]
hashed_pw = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_pw,file)

