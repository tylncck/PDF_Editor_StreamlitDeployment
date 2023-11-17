import streamlit as st
from scripts.funtions import save_file, delete_pdf_files, stamp, watermark

delete_pdf_files()

st.title('PDF Watermarking')
st.markdown("""
            Welcome to the PDF Watermarking Tool! Use the steps below to customize your PDF with a watermark:
            
            1. **Upload PDF File:** Upload your PDF file using the file uploader.
            
            2. **Select Watermark Options:** Choose the watermark text, color, and position.
            
            3. **Apply Watermark:** Click the 'Apply Watermark' button to add the selected watermark to your PDF.

            4. **Download Final PDF:** After successful watermarking, use the 'Download Final PDF' button to get your customized PDF.

            **Note:**
            - Customize your PDF by selecting watermark text, color, and position.
            - Preview your changes before applying the watermark.
            """)

pdf_file = st.file_uploader('Upload PDF (single file)', type=['pdf'], accept_multiple_files=False)

if pdf_file:
    content_path = save_file(file_uploader = pdf_file)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        w_text = st.radio('Select Watermark Text', ('Confidential', 'DoNotCopy'))
    with col2:
        w_color = st.radio('Select Watermark Color', ('Red', 'Grey'))
    with col3: 
        w_position = st.radio('Select Watermark Position', ('Overlay', 'Underlay'))
    
    w_path = f'assets/{w_text}_{w_color}.pdf'

    if st.button('Apply Watermark'):

        if w_position == 'Overlay':
            final_pdf = stamp(content_path, w_path)
        elif w_position == 'Underlay':
            final_pdf = watermark(content_path, w_path)
    
        st.download_button('Download Final PDF', final_pdf, key='download_pdf', file_name='Final_File.pdf')