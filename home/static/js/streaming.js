// 데이터 시각화 기준을 시간 설정하는 "클로져(Closure)" 함수
var timeInit = (function() {
    //console.log(arguments);
    // 인자 값을 기준으로 초기 값을 JSON 으로 저장한다.
    var time = {start_time: arguments[0], end_time: arguments[1]};

    return function(interval) {
        time.start_time += interval;
        time.end_time += interval;
        return time; // JSON 형식으로 반환한다.
    }
});

var urlInit = (function(){
    var split_url = arguments[0];

    return function() {return split_url}
});

// 그라파나에 대시보드 패널을 요청하여, 그 결과를 iframe에 삽입한다.
function EmbedGraph(){
    // iframe을 삽입할 div 태그 지정
    var container = document.getElementById('graph-section');

    // 이 함수가 호출될 때마다 기준 시간을 증가 시킨다.(인자 값만큼)
    var time = init(10);
    //console.log("================");
    //console.log(time);
    
    // 분할되어 있는 URL Array를 호출한다.
    var split_url = embed_url();
    //console.log("================");
    //console.log(split_url);
    // ["http://192.168.103.104:3000/d-solo/D1JI6ygWz/data?orgId=1&from=", "510&to=", "743&panelId=12"]

    start_time = time.start_time;
    end_time = time.end_time;
    grafanaSrc = split_url[0] + start_time + split_url[1] + end_time + split_url[2];
    //console.log(grafanaSrc);
    // "http://192.168.103.104:3000/d-solo/D1JI6ygWz/data?orgId=1&from=1556175235510&to=1556176135743&panelId=12"

    // 변경할 데이터를 임시로 저장할 iframe을 hidden으로 생성
    var iframe2 = document.createElement('iframe');
    iframe2.src = grafanaSrc;
    iframe2.width = "800";
    iframe2.height = "600";
    iframe2.setAttribute("frameborder","0");
    iframe2.setAttribute("style", "position:absolute; left:0px; z-index:1;")
    iframe2.style.visibility = 'hidden';
    container.appendChild(iframe2);

    // 인자 값이 있으면, 그래프를 딜레이 없이 바로 출력.(최초 호출하는 경우)
    if (arguments.length > 0){
        container.removeChild(container.getElementsByTagName('iframe')[0]);
        iframe2.setAttribute("style", "position:relative; z-index:1;")
        iframe2.style.visibility = 'visible';
    } else {
        setTimeout(function(){ 
            container.removeChild(container.getElementsByTagName('iframe')[0]);
            iframe2.setAttribute("style", "position:relative; z-index:1;")
            iframe2.style.visibility = 'visible';
         }, 2000);
    }
};

// 스트림 시작 버튼을 클릭하면 새로운 데이터(실시간 데이터) 업데이트
function toggleOn() {
    //stream = setInterval(function(){EmbedGraph();}, 3000);
    $('#toggle-trigger').bootstrapToggle('on'); // 토글 버튼 변경
}

// 스트림 중지 버튼을 클릭하면 데이터 업데이트 일시 중지
function toggleOff() {
    //clearInterval(stream);
    $('#toggle-trigger').bootstrapToggle('off'); // 토글 버튼 변경
}

$('#toggle-trigger').change(function(){
    if ($(this).prop('checked')){
        //console.log($(this).prop('checked'));
        stream = setInterval(function(){EmbedGraph();}, 3000);
    } else {
        //console.log($(this).prop('checked'));
        clearInterval(stream);
    }
});

// id가 post-form인 폼에서 submit 이벤트가 발생하면 create_chart() 호출
$('#post-form').on('submit', function(event){
    event.preventDefault(); // submit 액션이 동작하지 않도록 이벤트를 취소
    //console.log("form submitted!")
    create_chart();
});

// AJAX(Form Submit Event)
function create_chart() {
    //console.log("create post is working!")
    
    $.ajax({
        url : "/create_chart/", // the endpoint
        type : "POST", // http method
        data : { 
            embed_url : $('#embed_url').val(),
            chart : $('#chart').val(),
            start_time : $('#start_time').val(),
            end_time : $('#end_time').val(),
        }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            //$('#embed_url').val(''); // remove the value from the input

            // 응답결과로 전달 받은 json의 시간 정보로 기준 시간 지정한다.
            init = timeInit(json.start_time, json.end_time);
            embed_url = urlInit(json.embed_url);

            //console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            //console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

// 폼에서 options을 선택하면 Ajax가 동작한다.
$('#chart_select').change(function(){
    //console.log($('#chart_select').val());
    $.ajax({
        url : "/create_chart/", // the endpoint
        type : "POST", // http method
        data : { 
            chart_select : $('#chart_select').val(),
            start_time : $('#start_time').val(),
            end_time : $('#end_time').val(),
        }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            init = timeInit(json.start_time, json.end_time);
            embed_url = urlInit(json.embed_url);
            EmbedGraph('init');

            //console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            //console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
});