from docx import Document

# 전역 변수로 템플릿 경로와 출력 경로 설정
TEMPLATE_PATH = '초등학교상장만들기.docx'
OUTPUT_PATH = '수료증_templete.docx'

def replace_awardInfo(student_name, award, date, grade, class_num):
    # 템플릿 문서 열기
    doc = Document(TEMPLATE_PATH)

    # 문서의 모든 단락을 순회하며 문구 교체
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            # print(run.text)
            if '학생이름' in run.text:
                run.text = run.text.replace('학생이름', student_name)
            if '상명' in run.text:
                run.text = run.text.replace('상명', award)
            if '날짜' in run.text:
                run.text = run.text.replace('날짜', date)
            if '학년' in run.text:
                run.text = run.text.replace('학년', str(grade) + "학년")
            if '반' in run.text:
                run.text = run.text.replace('반', str(class_num) + "반")

    # 수정된 문서 저장
    doc.save(OUTPUT_PATH)

# 함수 호출 예시
student_name = '홍길동'
award = '최우수상'
date = '2024년 11월 3일'
grade = 4
class_num = 2

replace_awardInfo(student_name, award, date, grade, class_num)