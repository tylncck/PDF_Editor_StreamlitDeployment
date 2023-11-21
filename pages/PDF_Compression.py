import streamlit as st
from scripts.funtions import pdf_compress, delete_pdf_files, save_file, pdf_compress_ghost
import subprocess
import io 
import os

delete_pdf_files()

st.title('Compressing PDFs')

st.markdown(
    '''
    Welcome to the PDF Compression Tool! Choose a compression method and upload your PDF file below. 
    The tool supports two compression methods: **PyPDF2 Compression** and **Ghostscript Compression**.
    
    - **PyPDF2 Compression:** This method uses the PyPDF2 library to compress PDF files.
    - **Ghostscript Compression:** This method uses Ghostscript to compress PDF files.
    
    For Ghostscript Compression, you will have two options: Screen and eBook

    - **Screen Compression:** Optimized for quick online viewing, "Screen" settings reduce file size and resolution, ideal for web pages and electronic presentations.
    - **eBook Compression:** Balance between quality and size. Offering better resolution than "Screen," perfect for digital publications and e-reader compatibility.
    
    First upload the PDF file you wish to compress. Then click the **Compress PDF** button to start the compression process. 
    The compressed file will be available for download once the process is complete.
    '''
)

# Create a radio button to choose the compression method
compression_method = st.radio('Select Compression Method', ('PyPDF2 Compression', 'Ghostscript Compression'))
if compression_method == 'Ghostscript Compression':
    pdf_settings = st.radio('Select Compression Setting', ('eBook', 'Screen'))

uploaded_file = st.file_uploader('Upload your PDF file (single file upload supported)', type=['pdf'], accept_multiple_files=False)

if uploaded_file:
    if st.button('Compress PDF'):
        output_file_name = uploaded_file.name.replace('.pdf', '_compressed.pdf')
        if compression_method == 'PyPDF2 Compression':
            compressed_pdf = pdf_compress(uploaded_file)
        else:
            output_file = pdf_compress_ghost(uploaded_file=uploaded_file, 
                                             output_file_name = output_file_name,
                                             pdf_settings=pdf_settings)
            
            with open(output_file, 'rb') as f:
                compressed_pdf = io.BytesIO(f.read())

        uploaded_file_size = len(uploaded_file.getvalue()) / (1024 * 1024)
        compressed_file_size = len(compressed_pdf.getvalue()) / (1024 * 1024)

        st.write(f'Compressed the uploaded PDF successfully using the {compression_method}. Initial file size {uploaded_file_size:.2f} MB reduced to {compressed_file_size:.2f} MB. Click the button to download the compressed file.')

        delete_pdf_files()

        st.download_button('Download Compressed PDF', compressed_pdf, key='download_pdf', file_name=output_file_name)

