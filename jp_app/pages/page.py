#!/usr/bin/env python
# coding: utf-8

# In[6]:


#!pip install google-generativeai
#!pip install streamlit
#!pip install nbconvert


# In[2]:


import google.generativeai as genai
import os
import random
import streamlit as st

genai.configure(api_key=)


# In[3]:


model = genai.GenerativeModel('gemini-1.5-pro-latest')

def load_quiz_2():
    st.title("日本語助詞学習支援アプリ")
    with open("quiz.txt", "r", encoding="utf-8") as file:
        quiz_lines = file.readlines()
    return [line.strip() for line in quiz_lines]

def main():
    quiz_list = load_quiz_2()
    quiz_placeholder_2 = st.empty()
    if 'random_quiz_2' not in st.session_state:
        st.session_state['random_quiz_2'] = random.choice(quiz_list)
    quiz_placeholder_2.write("問題:" + st.session_state['random_quiz_2'])
    user_input = st.text_input("空欄に入る助詞を入力してください:")

    if st.button("レスポンスを生成"):
        if user_input:
            try:
                filled_quiz = st.session_state['random_quiz_2'].replace("__", f"『{user_input}』")
                chat = model.start_chat(history=[
                    {"role": "user", "parts": f"ユーザーは、問題の穴埋めをする形で日本語の助詞を入力します。実際にユーザーが入力した部分は『』で示されます"},
                    {"role": "model", "parts": "あなたはユーザーが入力した助詞が自然であるかを判定してください。出力形式は、正解か不正解を英語で出力し、その理由を英語で説明してください。"}
                ])
                response = chat.send_message(filled_quiz)
                st.write(st.session_state['random_quiz_2'] + "\n\n" +response.text)
                st.session_state['random_quiz_2'] = random.choice(quiz_list)
                quiz_placeholder_2.write("問題:" + st.session_state['random_quiz_2'])
            except Exception as e:
                st.error(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()