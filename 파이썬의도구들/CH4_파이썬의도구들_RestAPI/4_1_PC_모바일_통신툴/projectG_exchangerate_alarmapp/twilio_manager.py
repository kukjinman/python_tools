from twilio.rest import Client

#7 send_whatsapp_message() 함수
def send_whatsapp_message(current_rate, alarm_rate):
    #8 Twilio API를 사용하기 위한 인증 정보 설정
    account_sid = 'account_sid 값'
    auth_token = 'auth_token 값'
    client = Client(account_sid, auth_token)

    #9 client.messages.create() 메서드를 사용하여 메시지 전송
    message = client.messages.create(
        from_='whatsapp:+{twilio_number}',
        to='whatsapp:+{phone_number}',
        body=f' 환율 알림: 현재 환율은 {current_rate}이 설정한 알림 환율 {alarm_rate}을 넘었습니다!'
    )

