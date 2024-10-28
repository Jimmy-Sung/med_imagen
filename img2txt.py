import os

# 目標目錄 (可以更改為其他目錄)
directory = "/mnt/c/python_code/deep_imagen-main/brain/Training/meningioma"
# 提取目標目錄的最後一層資料夾名稱作為 .txt 檔案的內容
folder_name = os.path.basename(directory)

# 檢查目錄下的所有檔案
for filename in os.listdir(directory):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        # 去掉檔案的副檔名
        basename = os.path.splitext(filename)[0]
        
        # 對應的 .txt 檔名
        txt_filename = f"{basename}.txt"
        
        # 寫入目錄最後一層資料夾名稱至 .txt 檔
        with open(os.path.join(directory, txt_filename), 'w') as txt_file:
            txt_file.write(folder_name)

print("TXT 檔案已創建完成。")
