import pyttsx3
import PyPDF2

# Open the PDF file in binary mode
with open('oop.pdf', 'rb') as book:
    # Create a PdfReader object
    pdfReader = PyPDF2.PdfReader(book)
    
    # Get the total number of pages in the PDF
    pages = len(pdfReader.pages)
    
    # Initialize the text-to-speech engine
    speaker = pyttsx3.init()

    # Iterate through pages starting from page 7
    for num in range(6, pages):
        # Get the page object
        page = pdfReader.pages[num]
        
        # Extract text from the page
        text = page.extract_text()
        
        # Say the extracted text
        speaker.say(text)
        speaker.runAndWait()
