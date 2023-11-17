import streamlit as st
from scripts.funtions import get_pdf_page_count, pdf_inserter, save_file, delete_pdf_files

delete_pdf_files()

st.title('PDF File Inserter')
st.markdown('''
            Welcome to the PDF file inserter tool! Follow these steps to customize your PDF:

            1. **Upload First PDF:** Use the file uploader to upload your first PDF file.

            2. **Select Pages from First PDF:** Adjust the sliders to choose the page range from the first PDF.

            3. **Upload Second PDF:** Upload the second PDF file for insertion.

            4. **Select Pages from Second PDF:** Choose the page range from the second PDF using sliders.

            5. **Set Insertion Position:** Determine the position in the first PDF for the second PDF insertion.

            6. **Insert Files:** Click the 'Insert Files' button to combine and insert the selected pages.

            7. **Download Final PDF:** After successful insertion, use the 'Download Final PDF' button to get your customized PDF.

            **Note:**
            - Customize your PDF by selecting specific page ranges.
            - Ensure the selected pages and insertion position are correct before inserting.
            ''')


pdf_file_1 = st.file_uploader('Upload the First PDF (single file)', type=['pdf'], accept_multiple_files=False)

if pdf_file_1:
        
    path1 = save_file(file_uploader = pdf_file_1)
    
    f1_pages = get_pdf_page_count(path1)
    
    if f1_pages > 1:
        col1, col2 = st.columns(2)
        with col1:
            min1 = st.slider('First page from File 1', min_value=1, max_value=f1_pages, value=1) - 1
        with col2:
            max1 = st.slider('Last page from File 1', min_value=1, max_value=f1_pages, value=f1_pages)
        pagerange1 = (min1, max1)
    else: 
        st.write('The uploaded file only has 1 page. That page will be used directly as slicing is not possible for the file.')
        min1 = 0
        max1 = 1
        pagerange1 = (min1, max1)

    pdf_file_2 = st.file_uploader('Upload the Second PDF (single file)', type=['pdf'], accept_multiple_files=False)

    if pdf_file_2:
            
        path2 = save_file(file_uploader = pdf_file_2)
            
        f2_pages = get_pdf_page_count(path2)
        
        if f2_pages > 1:
            col1, col2 = st.columns(2)
            with col1:
                min2 = st.slider('First page from File 2', min_value=1, max_value=f2_pages, value=1) - 1
            with col2:
                max2 = st.slider('Last page from File 2', min_value=1, max_value=f2_pages, value=f2_pages)
            pagerange2 = (min2, max2)
        else: 
            st.write('The uploaded file only has 1 page. That page will be used directly as slicing is not possible for the file.')
            pagerange2 = (0,1)
        
        max_pos = max1 - min1
        
        if max_pos > 1:
            pos = st.slider('Select the page after which you want to insert the second file (or parts of second file)', min_value=1, max_value=max_pos, value=1)
        else:
            pos = 1

        if st.button('Insert Files'):
            final_pdf = pdf_inserter(pdf1 = path1, 
                                    pagerange1 = pagerange1, 
                                    pdf2 = path2,
                                    pagerange2 = pagerange2, 
                                    position = pos)

            delete_pdf_files()

            st.write('PDF Files sliced and insterted successfully. Click the button to download the final file')
                    
            st.download_button('Download Final PDF', final_pdf, key='download_pdf', file_name='Final_File.pdf')