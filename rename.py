import os

folder = "รูปสินค้า"

files = sorted(os.listdir(folder))

for i, file in enumerate(files, start=1):
    old_path = os.path.join(folder, file)

    ext = os.path.splitext(file)[1]
    new_name = f"สินค้า-{i:03d}{ext}"

    new_path = os.path.join(folder, new_name)

    os.rename(old_path, new_path)

print("เปลี่ยนชื่อเสร็จแล้ว!")