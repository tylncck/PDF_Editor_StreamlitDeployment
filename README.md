# PDF Editor Application

This is a simple PDF Editor Application that allows users to perform various operations on PDF files, such as merging, compressing, splitting, and inserting one PDF into another. The application is built using Streamlit and leverages the PyPDF2 library for PDF manipulation.

The original repository for this application, which is build with Docker images for general purpose deployments, can be reached [tylncck/PDF_Editor](https://github.com/tylncck/PDF_Editor). 

This repository is just a copy of the original repository and tailored for [streamlit.io](https://streamlit.io/) deployments. 

This application is running on [editpdfs.streamlit.app](https://editpdfs.streamlit.app/) page for you to explore. 

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoffee.com/tylncck)

## Application Pages

### Home Page
- Welcoming message and navigation instructions.

### PDF Merger Page
- Upload and merge multiple PDF files into one PDF file.

### PDF Compression Page
- Upload and compress a PDF file to reduce its size. Performance depends on the content of the uploaded file. 

### PDF Slicer Page
- Upload and slice a PDF file to only get some pages and use these pages to create a new PDF file.

### PDF Inserter Page
- Upload two PDF files and insert the second file after a specified page of the first file. Files can be used with all pages or you can decide which pages to use. 

### Watermarking Page
- Upload a PDF file and add a watermark with determined text, color, and position. (Currently *Confidential* and *Do Not Copy* version are available.)

## Credits
- The application utilizes the [PyPDF2](https://pypdf2.readthedocs.io/en/3.0.0/) library for PDF manipulation. 

- Ghostscript is used for PDF compression. Visit [Ghostscript](https://www.ghostscript.com/) for more information.

Credits to the PyPDF2 and Ghostscript developers for their contribution to open source habitat. 

## Conclusion
This PDF Editor Application provides a user-friendly interface for common PDF editing tasks. Feel free to explore and enhance your PDFs seamlessly!
I'll try my best to add new features to the application. 

by tylncck
