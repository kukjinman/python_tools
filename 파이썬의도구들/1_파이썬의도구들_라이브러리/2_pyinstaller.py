import subprocess
import os

def create_executable(script_name, output_dir='MyOutput'):
    try:
        # 폴더가 존재하지 않으면 생성
        os.makedirs(output_dir, exist_ok=True)

        # PyInstaller 명령어 설정
        command = f'pyinstaller --onefile --distpath {output_dir} --workpath {output_dir}/build --specpath {output_dir}/spec {script_name}'
        subprocess.run(command, shell=True, check=True)
        print(f"{script_name}의 실행 파일이 {output_dir}/dist 폴더에 생성되었습니다.")
    except subprocess.CalledProcessError as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    create_executable('1_tkinter.py')  # 변환할 파이썬 파일 이름
