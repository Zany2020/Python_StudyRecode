from docx import Document
#dock是你安装的第三方库名

def read_docx(file_path):
        doc = Document(file_path)
        content = ""
        for para in doc.paragraphs:
            content += para.text
        return content

text = read_docx('test.docx')
print(text)