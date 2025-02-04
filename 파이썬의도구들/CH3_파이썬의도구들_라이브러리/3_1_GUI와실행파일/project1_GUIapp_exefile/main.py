# 2_pyinstller.py 에서 가져온 코드
import subprocess

def create_exefile(python_file_path, output_dir='MyOutput'):
    try:
        command = f'pyinstaller --onefile --distpath {output_dir} --workpath {output_dir}/build --specpath {output_dir}/spec {python_file_path}'
        subprocess.run(command)
        print(f"{python_file_path}의 실행 파일이 {output_dir}/dist 폴더에 생성되었습니다.")
    except subprocess.CalledProcessError as e:
        print(f"오류 발생: {e}")

#0 완성품1 project_login_gui.py 실행 파일 생성
create_exefile('project_login_gui.py')