from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Grafana
from .forms import PostForm
import json, datetime, time, re

def index(request):
    return render(request, 'home/index.html')

def services(request):
    form = PostForm()
    return render(request, 'home/services.html', {'form': form})

def document(request):
    # if request.method == 'POST':
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.author = request.user
    #         post.save()
    #         return HttpResponseRedirect('/')
    # else:
    form = PostForm()
    #print(form)
    return render(request, 'home/document.html', {'form': form})

@csrf_exempt
def create_chart(request):

    if request.method == 'POST':
        # embed_url = request.POST.get('embed_url')
        chart_select = request.POST.get('chart_select')

        # "2019-04-25 10:33"
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        response_data = {}

        # Grafana 모델 객체를 만들어서 DB에 내용을 저장한다.
        # post = Grafana(embed_url=embed_url, start_time=start_time, end_time=end_time)
        post = Grafana(chart=chart_select, start_time=start_time, end_time=end_time)
        post.save()

        # [ URL 정제 ]
        # embed_url = "http://192.168.103.104:3000/d-solo/D1JI6ygWz/data?orgId=1&from=1556001374510&to=1556002815743&panelId=12"
        # from과 to 파라미터에 해당하는 값을 찾아서 제거한다. 
        # 그라파나의 경우 timestamp 정보 뒤에 임의의 숫자 3자리를 붙이고 있으므로 이는 제외하고 정규표현식으로 찾는다.

        # ['1556001374', '1556002815']
        # url_time = re.findall('[0-9]{10}', embed_url) 
        url_time = re.findall('[0-9]{10}', chart_select) 

        # 'http://192.168.103.104:3000/d-solo/D1JI6ygWz/data?orgId=1&from=|510&to=|743&panelId=12'
        # url_replace = (embed_url.replace(url_time[0], "|")).replace(url_time[1], "|") 
        url_replace = (chart_select.replace(url_time[0], "|")).replace(url_time[1], "|") 

        # ['http://192.168.103.104:3000/d-solo/D1JI6ygWz/data?orgId=1&from=', '510&to=', '743&panelId=12']
        embed_url_list = url_replace.split("|") 

        # [ 날짜&시간 형식 변경 ]
        # String to Datetime
        # timedate 형식 : "2019-04-25 10:33"
        start_convert = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M")
        end_convert = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M")

        # unixtime 형식 : 1556159660
        # Datetime to Unixtime
        start_unix = int(time.mktime(start_convert.timetuple()))
        end_unix = int(time.mktime(end_convert.timetuple()))

        response_data['embed_url'] = embed_url_list
        response_data['start_time'] = start_unix
        response_data['end_time'] = end_unix

        #print("=" * 40)
        #print(response_data)

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )