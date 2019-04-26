// 데이터 시각화 기준을 시간 설정하는 "클로저(Closure)" 함수
var timeInit = (function() {
    console.log(arguments);
    // 인자 값을 기준으로 초기 값을 JSON 으로 저장한다.
    var time = {start_time: arguments[0], end_time: arguments[1]};

    return function(interval) {
        time.start_time += interval;
        time.end_time += interval;
        return time; // JSON 형식으로 반환한다.
    }
});

var urlInit = (function() {
    var split_url = arguments[0];

    return function() {return split_url}
});

// 그라파나에 대시보드 패널을 요청하여, 그 결과를 iframe에 삽입한다.
function EmbedGraph(){
    // ifram을 삽입할 div 태그 지정
    var container = document.getElementById('graph-section');

    // 이 함수가 호출될 때마다 기준 시간을 증가 시킨다.(인자 값만큼)
    var time = init(10);
    console.log("==================");
    console.log(time);

    // 분할되어 있는 URL Array를 호출한다.
    var split_url = embed_url();
    console.log("==================");
    console.log(split_url);
    // ["http://class14.encore.com:23000/d-solo/D1JI6ygWz/kmong-data?orgId=1&from=", "009&to=", "251&panelId=12"]

    start_time = time.start_time;
    end_time = time.end_time;
    grafanaSrc = split_url[0] + start_time + split_url[1] + end_time + split_url[2];
    console.log(grafanaSrc);
    // "http://class14.encore.com:23000/d-solo/D1JI6ygWz/kmong-data?orgId=1&from=1556012998009&to=1556015222251&theme=light&panelId=12"

    // 변경할 데이터를 임시로 저장할 iframe을 hidden으로 생성
    var iframe2 = document.createElement('iframe');
    iframe2.src = grafanaSrc;
    iframe2.width = "600";
    iframe2.height = "300";
    iframe2.setAttribute("frameborder", "0");
    iframe2.setAttribute("style", "position:absolute; left:0px;")
    iframe2.style.visibility = 'hidden';
    container.appendChild(iframe2);

    setTimeout(function() {
        container.removeChild(container.getElementsByTagName('iframe')[0]);
        iframe2.setAttribute("style", "position:relative;")
        iframe2.style.visibility = "visible";
    }, 2000);
};

// 스트림 시작 버튼을 클릭하면 새로운 데이터 업데이트
$('#first_start').click(function(){
    stream = setInterval(function(){EmbedGraph();}, 5000);
});

// 스트림 중지 버튼을 클릭하면 데이터 업데이트 일시 중지
$('#first_stop').click(function(){
    clearInterval(stream);
});

// id가 post-form인 폼에서 submit 이벤트가 발생하면 create_chart() 호출
$('#post-form').on('submit', function(event){
    event.preventDefault(); // submit 액션이 동작하지 않도록 이벤트를 취소
    console.log("form submitted!")
    create_chart();
});

// AJAX
function create_chart() {
    console.log('create post is working!')

    $.ajax({
        url : "/create_chart", // the endpoint
        type : "POST", // http method
        data : {
            embed_url : $('#embed_url').val(),
            start_date : $('#start_time_0').val(),
            start_time : $('#start_time_1').val(),
            end_date : $('#end_time_0').val(),
            end_time : $('#end_time_1').val(),
        }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            console.log(json); // log the returned json to the console

            // 응답결과로 전달 받은 json의 시간 정보로 기준 시간 지정한다.
            init = timeInit(json.start_time, json.end_time);
            embed_url = urlInit(json.embed_url);

            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err){
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encounterd an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};