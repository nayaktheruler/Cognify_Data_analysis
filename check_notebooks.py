import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os

def run_notebook(path):
    print(f"Running {path}...")
    with open(path, encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    try:
        ep.preprocess(nb, {'metadata': {'path': os.path.dirname(path)}})
        with open(path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print(f"Successfully ran {path}")
        return True, None
    except Exception as e:
        print(f"Error running {path}: {e}")
        return False, str(e)

base_dir = r"d:\cognify_data_analysis123"
folders = ["level 1", "level 2", "level 3"]

results = []
for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    if not os.path.exists(folder_path):
        continue
    for file in os.listdir(folder_path):
        if file.endswith(".ipynb"):
            full_path = os.path.join(folder_path, file)
            success, error = run_notebook(full_path)
            results.append((full_path, success, error))

print("\nSummary:")
for path, success, error in results:
    status = "SUCCESS" if success else "FAILED"
    print(f"{status}: {path}")
    if error:
        print(f"  Error: {error}")
