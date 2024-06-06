#!/usr/bin/env python
# coding: utf-8

# In[6]:


#!pip install google-generativeai
#!pip install streamlit
#!pip install nbconvert


# In[2]:


import google.generativeai as genai
import os
genai.configure(api_key=)


# In[3]:


model = genai.GenerativeModel('gemini-1.5-pro-latest')


# In[5]:


import streamlit as st
def main():
    st.title("日本語数え方学習支援アプリ")
    user_input = st.text_input("コメントを入力してください:")
    chat = model.start_chat(history=[
    {
    "role": "user",   # ユーザーの役割を指定
    "parts": "ユーザーは日本語、または英語で数えたい物について入力します。"  # ユーザーの入力を指定
    },
    {
    "role": "model",  # モデルの役割を指定
    "parts": "あなたは物の1から１０までの数え方について表形式で出力してください。その際、数(Number)、漢字(kanji)、日本語の読み方(kana)、日本語の発音(pronunciation)をつけてください。例えば、１、1個、いっこ、ikkoのように出力してください。また、その数え方を日本語と英語の読み方を出力してください。その後、English: Count apples with 個 (ko).のように簡単な説明をつけてください。"
    }
    ])
    if st.button("レスポンスを生成"):
        if user_input:
            try:
                response = chat.send_message(user_input)
                st.write(response.text)
            except Exception as e:
                st.error(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()

