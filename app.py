# importing required packages
import streamlit as st 
from st_pages import Page, show_pages
from scripts.funtions import buy_me_coffee
#from streamlit_extras.app_logo import add_logo

#add_logo('assets/PDFEditorLogo.jpg')

# Arranging orders, names and icons for pages including home page. 
show_pages([Page('app.py', 'Home', '🏠'),
            Page('pages/PDF_Merge.py', 'Merging PDFs', '➕'),
            Page('pages/PDF_Compression.py', 'Compressing PDF', '🗜️'),
            Page('pages/PDF_Insert.py', 'Inserting PDF', '🌭'),
            Page('pages/PDF_Split.py', 'Slicing PDF', '🪓'),
            Page('pages/PDF_Watermark_Stamp.py', 'Stamp PDF', '✒️'),])

# Content for Home Page
st.title('Welcome to the PDF Editor App!')

st.markdown('''This app allows you to perform various PDF editing tasks easily. 
         To get started, please navigate to the sidebar on the left where you will find the following editing options:''')

st.markdown('- Merge multiple PDF files into one.')
st.markdown('- Compress PDF files to reduce their size.')
st.markdown('- Insert one PDF into another after a certain page.')
st.markdown('- Slice some pages from a PDF file.')
st.markdown('- Add Watermark or Stamp to a PDF file.')

st.markdown('Simply click on the option you would like to use, and follow the instructions provided. Enjoy editing your PDFs! 🎉')

st.markdown(buy_me_coffee(), unsafe_allow_html=True)