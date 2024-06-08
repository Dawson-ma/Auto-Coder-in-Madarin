### Created by Nicolas Mejia Petit at Vezora
### We invested a significant amount of time in developing this script. If you intend to use it to filter out non-functional code in your own projects or datasets, please include the following attribution in your model's or dataset's repository:
### "Filtered Using Vezora's CodeTester"


import json
import subprocess
import re
import os
import ijson
from multiprocessing import Pool, cpu_count
from tqdm import tqdm

def run_python_code(code):
    try:
        os.makedirs('cache', exist_ok=True)
        os.chdir('cache')
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        result = subprocess.run(['python', '-c', code], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, timeout=1, startupinfo=startupinfo)
        os.chdir('..')
    except Exception as e:
        os.chdir('..')
        return False
    return True

def extract_python_code(output):
    pattern = r'```python(.*?)```'
    match = re.search(pattern, output, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def test_python_code(example):
    output = example['output']
    code = extract_python_code(output)
    if code:
        if run_python_code(code):
            return example, None  # Working code
        else:
            return None, example  # Non-working code
    return example, None  # Not Python related

def test_python_codes(dataset):
    with Pool(cpu_count()) as p:
        results = list(tqdm(p.imap(test_python_code, dataset), total=len(dataset)))
    
    working_codes = [result[0] for result in results if result[0]]
    non_working_codes = [result[1] for result in results if result[1]]
    
    print(f"Number of examples that worked: {len(working_codes)}")
    print(f"Number of examples that didn't work: {len(non_working_codes)}")
    
    return working_codes, non_working_codes

if __name__ == '__main__':
    dataset_path = input("Enter the path to your dataset: ")
    output_filename_working = input("Enter the filename for your new JSON file with working codes: ")
    output_filename_non_working = input("Enter the filename for your new JSON file with non-working codes: ")

    with open(dataset_path, 'r') as f:
        objects = ijson.items(f, 'item')
        dataset = list(objects)

    working_codes, non_working_codes = test_python_codes(dataset)

    with open(output_filename_working, 'w') as f:
        json.dump(working_codes, f, indent=2)

    with open(output_filename_non_working, 'w') as f:
        json.dump(non_working_codes, f, indent=2)
