from pyxl_manager import read_certification_list_v2
from gmail_smtplib_manager import requestTo_send_email

file_path = 'resource/파이썬수료증리스트_v2.xlsx'

print("project start")

#0 수료증 인원 정보 리스트를 불러오기
certification_list = read_certification_list_v2(file_path)

#2 수료증 인원 정보 리스트를 순회
for item in certification_list:
    print()
    print(item)
    print(item[0], item[1], item[2], item[3])

    #3 이메일 발송 요청
    # def requestTo_send_email(from_address, password, to_address, subject, body, attached_file_path):
    requestTo_send_email("kukjinman2@gmail.com","앱 비밀번호",
                         item[3], "파이썬 수료증 발급 안내",
                         f"안녕하세요. {item[2]}님! 파이썬 수료증 첨부파일입니다.",
                         f"certificate_{item[2]}.docx")

    print("=====================================================")

print("project end")
