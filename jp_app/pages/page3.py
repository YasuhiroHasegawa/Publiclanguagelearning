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

def load_quiz():
    st.title("日本語丁寧語・尊敬語・謙譲語学習支援アプリ")
    with open("quiz2.txt", "r", encoding="utf-8") as file:
        quiz_lines = file.readlines()
    return [line.strip() for line in quiz_lines]

def main():
    quiz_list = load_quiz()
    quiz_placeholder = st.empty()
    quiz_word =["の尊敬語","の謙譲語","の丁寧語"]
    if 'random_quiz' not in st.session_state:
        st.session_state['random_quiz'] = random.choice(quiz_list) + quiz_word[random.randint(0,2)]
    quiz_placeholder.write("問題:" + st.session_state['random_quiz'])
    user_input = st.text_input("適切な日本語を入力してください:")

    if st.button("レスポンスを生成"):
        if user_input:
            try:
                filled_quiz = st.session_state['random_quiz'] + "は『"  + user_input + "』です。"
                chat = model.start_chat(history=[
                    {"role": "user", "parts": f"ユーザーは、問題に答える形で日本語の尊敬語・謙譲語・丁寧語を入力します。実際にユーザーが入力した部分は『』で示されます"},
                    {"role": "model", "parts": "あなたはユーザーが入力した尊敬語・謙譲語・丁寧語が自然であるかを判定してください。出力形式は、正解か不正解を英語で出力し、その理由を英語で説明してください。"}
                ])
                response = chat.send_message(filled_quiz)
                st.write(st.session_state['random_quiz'] + "\n\n" +response.text)
                st.session_state['random_quiz'] = random.choice(quiz_list) + quiz_word[random.randint(0,2)]
                quiz_placeholder.write("問題:" + st.session_state['random_quiz'])
            except Exception as e:
                st.error(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()