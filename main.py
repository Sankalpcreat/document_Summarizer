from services.langchain_service import summarize_text
from utils.file_handler import read_pdf_file, read_text_file

def main():
    print("Document Summarizer")
    file_path = input("Enter the path to your document (PDF or TXT): ")
    

    if file_path.endswith('.pdf'):
        content = read_pdf_file(file_path)
    elif file_path.endswith('.txt'):
        content = read_text_file(file_path)
    else:
        print("Unsupported file type. Please use PDF or TXT.")
        return
    

    if content:
        print("\nGenerating summary...\n")
        summary = summarize_text(content)
        print("Summary:\n")
        print(summary)
    else:
        print("Failed to read the content from the file.")

if __name__ == "__main__":
    main()
