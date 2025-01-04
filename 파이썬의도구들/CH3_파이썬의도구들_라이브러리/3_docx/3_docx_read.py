from docx import Document

#1 write_문서.docx 파일 객체 가져오기
doc = Document('write_문서.docx')

#2 문서의 모든 문단을 순회하며 문구 교체
for paragraph in doc.paragraphs:
    for run in paragraph.runs:
        #3 'name_var'를 홍길동으로 교체
        if 'name_var' in run.text:
            run.text = run.text.replace('name_var', '홍길동')
        #4 'gender_var'를 남으로 교체
        if 'gender_var' in run.text:
            run.text = run.text.replace('gender_var', '남')

#5 새로운 문서로 저장
doc.save('write_문서_수정됨.docx')

print("문서 제목이 성공적으로 수정되었습니다!")