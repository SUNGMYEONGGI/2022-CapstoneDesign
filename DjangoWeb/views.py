from django.http import HttpResponse
from django.shortcuts import redirect, render
#from capstone_konlpy import sentiment_predict

def index(request):
    if request.method == "POST":
        name = request.POST.get("your_name")
        print(name)
        # capstone_konlpy.py에서 sentiment_predict() 함수를 호출하여 감성분석 결과를 출력
        #sentiment_predict(name)
        
        
        return render(request, "DjangoWeb\index.html", {"name": name})
    elif request.method == "GET":
        print('Case 3')
        return render(request, 'DjangoWeb\index.html')