import streamlit as st


st.title("seo sky")
#st.write('hello seo sky?')

my_button = st.button('YOUTUBE')

st.write(my_button)

if my_button == True:
    st.write('클릭했을 때만 보임')

st.link_button('네이버로 이동', 'https://www.youtube.com')

agree = st.checkbox("동의합니다")
gender = st.radio("성별 선택", ["남성", "여성", "기타"])
