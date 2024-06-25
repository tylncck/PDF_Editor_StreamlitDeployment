import streamlit as st
from scripts.funtions import pdf_merger, delete_pdf_files, buy_me_coffee
from streamlit_sortables import sort_items

delete_pdf_files()

st.title('Merging Multiple PDFs')

with st.expander(label='Job Aids'):
    st.info('''Upload multiple PDF files, then sort them in the desired order, and merge them into a single PDF file. 
         Your uploaded files are not saved anywhere, so you can merge your files with peace of mind.''')


uploaded_files = st.file_uploader('Upload your PDF files (multiple files supported)', type=['pdf'], accept_multiple_files=True)

if uploaded_files:
    file_data = [{'file': file, 'name': file.name} for file in uploaded_files]
    file_names = [item['name'] for item in file_data]

    st.info('Please sort the files in the order you wish them to be merged.')
    sorted_names = sort_items(file_names)  # Sort file names
    
    output_file_name = st.text_input("Enter the merged PDF file name (optional):")
    
    if st.button('Merge PDFs'):
        sorted_file_data = sorted(file_data, key=lambda x: sorted_names.index(x['name']))
        sorted_files = [item['file'] for item in sorted_file_data]
        
        merged_pdf = pdf_merger(sorted_files)
        st.success('Merged the uploaded PDFs successfully. Click the button to download the merged file')
        
        if output_file_name:
            st.download_button('Download Merged PDF', merged_pdf, key='download_pdf', file_name=f'{output_file_name}.pdf')
        else:
            st.download_button('Download Merged PDF', merged_pdf, key='download_pdf', file_name='Merged_File.pdf')

st.markdown(buy_me_coffee(), unsafe_allow_html=True)
