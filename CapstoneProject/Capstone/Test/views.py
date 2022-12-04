from django.http import HttpResponse
from django.shortcuts import redirect, render
import re
import json
from konlpy.tag import Okt
from keras.utils import pad_sequences
from keras.preprocessing.text import Tokenizer
import pickle
import keras

okt = Okt()
tokenizer  = Tokenizer()


DATA_CONFIGS = 'C:\\Users\\smgsm\\virtualvenv\\CapstoneProject\\Capstone\\Konkpy-Emotion\\data\\CLEAN_DATA\\data_configs.json'
prepro_configs = json.load(open('C:\\Users\\smgsm\\virtualvenv\\CapstoneProject\\Capstone\\Konkpy-Emotion\\data\\CLEAN_DATA\\data_configs.json','rt', encoding='UTF8')) #TODO 데이터 경로 설정

#TODO 데이터 경로 설정
with open('C:\\Users\\smgsm\\virtualvenv\\CapstoneProject\\Capstone\\Konkpy-Emotion\\data\\CLEAN_DATA\\tokenizer.pickle','rb') as handle:
    word_vocab = pickle.load(handle)

prepro_configs['vocab'] = word_vocab

tokenizer.fit_on_texts(word_vocab)

MAX_LENGTH = 8 #문장최대길이



def sentiment_predict(sentence):
    sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣\\s ]','', sentence)
    stopwords = ['은','는','이','가','하','아','것','들','의','있','되','수','보','주','등','한'] # 불용어 추가할 것이 있으면 이곳에 추가
    sentence = okt.morphs(sentence, stem=True) # 토큰화
    sentence = [word for word in sentence if not word in stopwords] # 불용어 제거
    vector  = tokenizer.texts_to_sequences(sentence)
    pad_new = pad_sequences(vector, maxlen = MAX_LENGTH) # 패딩

    #학습한 모델 불러오기
    model = keras.models.load_model('C:\\Users\\smgsm\\virtualvenv\\CapstoneProject\\Capstone\\Konkpy-Emotion\\my_model') #TODO 데이터 경로 설정
    model.load_weights('C:\\Users\\smgsm\\virtualvenv\\CapstoneProject\\Capstone\\Konkpy-Emotion\\data\\DATA_OUT\\KonlpyWeights.h5') #TODO 데이터 경로 설정
    predictions = model.predict(pad_new)
    predictions = float(predictions.squeeze(-1)[1])

    if(predictions > 0.7):
        print("{:.2f}% 확률로 긍정 리뷰입니다.\n".format(predictions * 100))
        return "https://www.youtube.com/results?search_query=%EA%B8%B0%EB%B6%84%EC%A2%8B%EC%9D%80+%EB%85%B8%EB%9E%98"
    else:
        print("{:.2f}% 확률로 부정 리뷰입니다.\n".format((1 - predictions) * 100))
        return round(predictions * 100, 2)

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get("your_name")
        print(name)
        # capstone_konlpy.py에서 sentiment_predict() 함수를 호출하여 감성분석 결과를 출력
        result = sentiment_predict(name)
        # return render(request, "index.html", {"result": result})
        return redirect(result)
    else:
        return render(request, 'index.html')
        # https://www.youtube.com/results?search_query=%EA%B8%B0%EB%B6%84%EC%A2%8B%EC%9D%80+%EB%85%B8%EB%9E%98