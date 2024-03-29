#TTS(Text To Speech)
#STT(Speech To Text)

from gtts import gTTS
from playsound import playsound

# 영어문장
#text = 'Imagine that you have just arrived at a hotel after a tiring 7-hour overnight flight.'
file_name = 'sample.mp3'
#tts_en = gTTS(text=text, lang='en')
#tts_en.save(file_name)

# playsound(file_name) # .mp3 파일 재생

# 한글 문장

#text = '안녕하세요 AI Speaker 입니다. 오늘 하루는 어때요?'
#tts_ko =gTTS(text=text, lang='ko')
#tts_ko.save(file_name)
#playsound(file_name) # .mp3 파일 재생

# 긴 문장(파일에서 불러와서 이용)

with open('sample.txt','r',encoding='utf8') as f:
    text= f.read() 

tts_ko =gTTS(text=text, lang='ko')
tts_ko.save(file_name)
playsound(file_name) # .mp3 파일 재생
