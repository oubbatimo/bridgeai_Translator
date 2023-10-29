#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:14:52 2022

@author: mohamedoubbati
"""
import streamlit as st
from googletrans import Translator
from MyLanguages import *

st.title('bridgeai')
st.subheader('Machine Translation based on Google Translator')

target_language = st.selectbox("Select target language:", languages)

source_text = st.text_area("Enter text to translate:")

TranslateOrder = st.button('Translate')

if TranslateOrder:
    mytranslator = Translator()
    out = mytranslator.translate(source_text,dest=target_language)
    st.write(out.text)

#mytranslator=Translator()
#out=mytranslator.translate('wie geht es dir?',dest='fr')

#print(out)