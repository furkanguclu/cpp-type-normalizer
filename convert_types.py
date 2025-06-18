import re
import json
import os

# Tip haritasını yükle
with open('type_map.json', 'r', encoding='utf-8') as f:
    type_map = json.load(f)

# Uzun tipleri önce işle (öncelik sırasına göre)
sorted_map = sorted(type_map.items(), key=lambda x: -len(x[0]))

# Regex desenleri hazırla
patterns = [(re.compile(r'\b' + re.escape(old) + r'\b'), new) for old, new in sorted_map]

def replace_types_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        original_code = f.read()

    modified_code = original_code
    for pattern, replacement in patterns:
        modified_code = pattern.sub(replacement, modified_code)

    # Yedekle
    backup_path = file_path + '.bak'
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(original_code)

    # Güncellenmiş hali kaydet
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(modified_code)

    print(f"✓ Updated: {file_path} | Backup: {backup_path}")

def scan_and_replace(directory, extensions=(".c", ".cpp", ".h", ".hpp")):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extensions):
                replace_types_in_file(os.path.join(root, file))

# Script çalıştırıldığında
if __name__ == "__main__":
    scan_and_replace("src")
