import time, os
import speech_recognition as sr 
from gtts import gTTS
from playsound import playsound

# 1. 우리의 목소리를 인식하고(STT)

# 2. 그것을 해석하여 인공지능 스피커는 대답을 만들어내고

# 3. 인공지능 스피커는 그 대답을 소리내어 읽는다(TTS)

# 음성 인식 (듣기, STT)
def listen(recognizer, audio):
    try:
        text= recognizer.recognize_google(audio,language='ko')
        print('[사용자] '+ text)
        answer(text)
    except sr.UnknownValueError: # 음성이 안 들어온 경우
        print('인식 실패') # 음성 인식 실패 한 경우
    except sr.RequestError as e: # 네트워크, 인터넷 문제 ,API 키 문제
        print('요청 실패: {0}'.format(e)) 

# 대답
def answer(input_text):
    answer_text = ''
    if '안녕' in input_text:
        answer_text= '안녕하세요? 반갑습니다.'
    elif '날씨' in input_text:
        answer_text ='오늘의 서울 기온은 20도 입니다. 맑은 하늘이 예상됩니다.'
    elif '환율' in input_text:
        answer_text='원 달러 환율은 1380원입니다.'
    elif '고마워' in input_text:
        answer_text='별 말씀을요.'
    elif '종료' in input_text:
        answer_text='다음에 또 만나요.'
        stop_listening(wait_for_stop=False) # 더 이상 듣지 않음
    else:
        answer_text='다시 한 번 말씀해주시겠어요?'
    speak(answer_text)

# 소리 내어 읽기(tts)
def speak(text):
    print('[AI] ' + text)
    file_name='voice.mp3'
    tts= gTTS(text=text, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name): # voice.mp3 파일 삭제 실행 할 때마다 파일 만들고 삭제를 반복
        os.remove(file_name)

r =sr.Recognizer()
m =sr.Microphone()


speak('무엇을 도와드릴까요?')

# 귀를 계속 열어두고 있다.
# 함수 호출되면 listen 함수 실행

stop_listening = r.listen_in_background(m, listen)

#stop_listening(wait_for_stop=False) # 사용자가 stop 하면 더 이상 듣지 않음

while True:
    time.sleep(0.1)
