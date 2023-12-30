import os
   
folder = "D:/DCIM/100GOPRO"

# 앞에 붙는 f는 포멧이고, 앞에 붙여줘야 한다.
for count, filename in enumerate(os.listdir(folder)): # 파일들이 리스트 안에 들어있다.
    src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
    dst =f"{folder}/move/{filename}"

    if filename.endswith(".THM"):
        # 여기서 rename()이라는 거는 경로 전체를 변경하는 거다! 만약, 'move'라는 폴더가 없다면 실행이 안 된다.(오류 발생!)
        # renames()를 사용하면 'move'라는 폴더가 없더라도 만들어서 실행해준다.
        os.rename(src, dst) 
        print("done")

'''
import os

# 검색할 디렉토리
directory = "/path/to/your/directory"

# 디렉토리 내의 모든 파일과 폴더를 가져옵니다
files_in_directory = os.listdir(directory)

# .jpg 확장자를 가진 파일만 선택합니다
jpg_files = [file for file in files_in_directory if file.endswith(".jpg")]
'''
