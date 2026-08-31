

import os

def generate_files(target_folder, start_num, end_num, target_dir="TinPython", prefix="A3-"):
    """
    สร้างไฟล์ .py ตามช่วงตัวเลขที่กำหนด
    เช่น generate_files(61, 80) จะสร้างไฟล์ตั้งแต่ A1-061.py ถึง A1-080.py
    """

    target = f"{target_folder}/{target_dir}"

    # ตรวจสอบว่าโฟลเดอร์มีอยู่จริงไหม ถ้าไม่มีให้สร้าง
    if not os.path.exists(target):
        os.makedirs(target)

    # วนลูปสร้างไฟล์ตั้งแต่ start_num ถึง end_num
    for i in range(start_num, end_num + 1):
        file_name = f"{prefix}{i:03d}.py" # :03d จะทำให้เป็นเลข 3 หลัก เช่น 021
        file_path = os.path.join(target, file_name)
        
        # ตรวจสอบว่าไฟล์มีอยู่แล้วหรือไม่ เพื่อไม่ให้เขียนทับงานเก่า
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"# File: {file_name}\n") # ใส่ comment หัวไฟล์ไว้เล็กน้อย
            print(f"Created: {file_name}")
        else:
            print(f"Skipped: {file_name} (Already exists)")

if __name__ == "__main__":
    # กำหนดตัวเลขเริ่มต้นและสิ้นสุดที่ต้องการสร้างไฟล์ที่นี่
    generate_files("A3", 1, 30)