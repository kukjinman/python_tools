#1 subprocess 모듈을 가져옵니다.
import subprocess

#2 실행 파일을 생성하는 함수입니다.
def create_exefile(python_file_path, output_dir='MyOutput'):
    try:
        #3 PyInstaller 명령어를 생성합니다.
        command = f'pyinstaller --onefile --noconsole --distpath {output_dir} --workpath {output_dir}/build --specpath {output_dir}/spec {python_file_path}'
        #4 명령어를 실행합니다.
        subprocess.run(command)
        print(f"{python_file_path}의 실행 파일이 {output_dir}/dist 폴더에 생성되었습니다.")
    except subprocess.CalledProcessError as e:
        print(f"오류 발생: {e}")

#5 실행 파일을 생성할 파이썬 파일을 지정합니다.
create_exefile('../tool1_tkinter/1_tkinter.py')