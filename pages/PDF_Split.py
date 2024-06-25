import streamlit as st
from scripts.funtions import get_pdf_page_count, pdf_split, save_file, delete_pdf_files, buy_me_coffee

delete_pdf_files()

st.title('PDF File Slicing')

with st.expander(label='Job Aids'):
    st.info('''
            Welcome to the PDF File Slicing Tool! Use the steps below to customize your PDF:
            
            1. **Upload PDF File:** Upload your PDF file using the file uploader.
            
            2. **Select Page Range:** Adjust the sliders to choose the page range you want to extract from the PDF.
            
            3. **Slice PDF File:** Click the 'Slice PDF File' button to extract the selected pages.
            
            4. **Download Final PDF:** After successful extraction, use the 'Download Final PDF' button to get your customized PDF.

            **Note:**
            - Customize your PDF by selecting a specific page range.
            - Ensure the selected pages are correct before slicing.
            ''')

pdf_file = st.file_uploader('Upload the First PDF (single file)', type=['pdf'], accept_multiple_files=False)

if pdf_file:
        
    path = save_file(file_uploader = pdf_file)
    
    pages = get_pdf_page_count(path)
    
    if pages > 1:

        col1, col2 = st.columns(2)
        with col1:
            min1 = st.slider('First page from the file', min_value=1, max_value=pages, value=1) - 1
        with col2:
            max1 = st.slider('Last page from the file', min_value=1, max_value=pages, value=pages)
        
        pagerange = (min1, max1)

        if st.button('Slice PDF File'):
            final_pdf = pdf_split(pdf = path, 
                                pagerange = pagerange)

            delete_pdf_files()

            st.success('PDF Files sliced successfully. Click the button to download the final file')
                        
            st.download_button('Download Final PDF', final_pdf, key='download_pdf', file_name='Final_File.pdf')
    else:
        delete_pdf_files()
        st.error('The uploaded file has only 1 page and cannot be sliced. Please upload multi-page file.')

st.markdown(buy_me_coffee(), unsafe_allow_html=True)
