import speech_recognition as sr

# 마이크로부터 음성 듣기
r = sr.Recognizer()
with sr.Microphone() as source:
    print("듣고 있어요")
    audio =r.listen(source) # 마이크로부터 음성 듣기

# 파일로부터 음성 불러오기(wav, aiff/aiff-c, flac 가능 mp3 불가)
#r= sr.Recognizer()
#with sr.AudioFile('sample.wav') as source:
    #audio =r.record(source)


try:
    # 구글 API로 인식
    #(녹음-> 구글에 보냄 => 음성인식-> 텍스트 변환)
    #text =r.recognize_google(audio, language='en-US') # 영어에 맞춰 text를 변환해줘 
   
    #print(text)

    # 한글 문장
    # 긴 문장 끊김 없이 말해야됨
    text= r.recognize_google(audio,language='ko')
    print(text)

except sr.UnknownValueError: # 음성이 안 들어온 경우
    print('인식 실패') # 음성 인식 실패 한 경우
except sr.RequestError as e: # 네트워크, 인터넷 문제 ,API 키 문제
    print('요청 실패: {0}'.format(e)) 