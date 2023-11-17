import streamlit as st
from scripts.funtions import pdf_compress, delete_pdf_files, save_file
import subprocess
import io 
import os

delete_pdf_files()

st.title('Compressing PDFs')

st.markdown(
    """
    Welcome to the PDF Compression Tool! Choose a compression method and upload your PDF file below. 
    The tool supports two compression methods: **PyPDF2 Compression** and **Ghostscript Compression**.
    
    - **PyPDF2 Compression:** This method uses the PyPDF2 library to compress PDF files.
    - **Ghostscript Compression:** This method uses Ghostscript to compress PDF files.
    
    First upload the PDF file you wish to compress. Then click the **Compress PDF** button to start the compression process. 
    The compressed file will be available for download once the process is complete.
    """
)

# Create a radio button to choose the compression method
compression_method = st.radio("Select Compression Method", ("PyPDF2 Compression", "Ghostscript Compression"))

uploaded_file = st.file_uploader('Upload your PDF file (single file upload supported)', type=['pdf'], accept_multiple_files=False)

if uploaded_file:
    if st.button('Compress PDF'):
        output_file_name = uploaded_file.name.replace('.pdf', '_compressed.pdf')
        if compression_method == "PyPDF2 Compression":
            compressed_pdf = pdf_compress(uploaded_file)
        else:
            target_directory = 'files'
            target_path = save_file(uploaded_file)
            output_file = target_directory + '/' + output_file_name
            compression_command = f'gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile="{output_file}" "{target_path}"'
            
            subprocess.run(compression_command, shell=True, check=True)
            
            with open(output_file, 'rb') as f:
                compressed_pdf = io.BytesIO(f.read())

        uploaded_file_size = len(uploaded_file.getvalue()) / (1024 * 1024)
        compressed_file_size = len(compressed_pdf.getvalue()) / (1024 * 1024)

        st.write(f'Compressed the uploaded PDF successfully using the {compression_method}. Initial file size {uploaded_file_size:.2f} MB reduced to {compressed_file_size:.2f} MB. Click the button to download the compressed file.')

        delete_pdf_files()

        st.download_button('Download Compressed PDF', compressed_pdf, key='download_pdf', file_name=output_file_name)

