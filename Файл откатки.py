import subprocess
import os
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "Инструкция.docx")
def open_doc_file(file_path):
    try:
        subprocess.Popen(["start", "WINWORD.EXE", file_path], shell=True)
        return "Файл успешно открыт"
    except Exception as e:
        return f"Ошибка при попытке открыть файл: {str(e)}"

file_path = image_path
result = open_doc_file(file_path)
print(result)