import fitz
from flask import Flask, request, jsonify
import difflib

app = Flask(__name__)

def extract_text_from_pdf(file_path):
    document = fitz.open(file_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

def compare_texts(text1, text2):
    diff = difflib.ndiff(text1.splitlines(), text2.splitlines())
    changes = []
    current_paragraph = []
    for line in diff:
        if line.startswith('- ') or line.startswith('+ '):
            current_paragraph.append(line)
        elif current_paragraph:
            changes.append(current_paragraph)
            current_paragraph = []
    if current_paragraph:
        changes.append(current_paragraph)
    return changes

@app.route('/compare_pdfs', methods=['POST'])
def compare_pdfs():
    data = request.get_json()
    if 'file1_path' not in data or 'file2_path' not in data:
        return jsonify({"error": "Please provide both PDF file paths"}), 400

    file1_path = data['file1_path']
    file2_path = data['file2_path']

    # Extract text from the provided file paths
    text1 = extract_text_from_pdf(file1_path)
    text2 = extract_text_from_pdf(file2_path)

    changes = compare_texts(text1, text2)
    grouped_changes = [{"paragraph": i+1, "changes": change} for i, change in enumerate(changes)]

    return jsonify(grouped_changes)

if __name__ == '__main__':
    app.run(debug=True,port=8084)
