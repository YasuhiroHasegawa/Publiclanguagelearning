import nbformat
from nbconvert import PythonExporter

def convert_notebook(notebook_path, output_path):
    # ノートブックファイルを読み込む
    with open(notebook_path, 'r', encoding='utf-8') as fh:
        nb = nbformat.read(fh, as_version=4)

    # Pythonエクスポーターを使ってコードを抽出
    exporter = PythonExporter()
    source, _ = exporter.from_notebook_node(nb)

    # 変換したコードをファイルに書き込む
    with open(output_path, 'w', encoding='utf-8') as fh:
        fh.write(source)

# 使用例
convert_notebook('main.ipynb', 'app.py')
