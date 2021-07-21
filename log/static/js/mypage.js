$(document).ready(function () {
  var week = 52; //1년은 52주
  for (var a = 0; a < week; a++) {
    $(".count_day").append('<div class="week"></div>');
  }

  for (var a = 0; a < 7; a++) {
    $(".week").append('<div class="day"></div>');
  }
  /*프로필 레벨 */

  var user_level = document.querySelector(".myprofile_rank");
  var next_level = document.querySelector(".next_level");
  var left_num = document.querySelector(".left_num_text");
  var count = "{{count|safe}}";
  if (count >= 0 && count < 15) {
    user_level.innerHTML = "등급 : Bronze";
    next_level.innerHTML = "Silver";
    left_num.innerHTML = "까지 앞으로" + 15 - count + "개!";
    $(".left_name").css({
      color: "#435f7a",
    });
  } else if (count >= 15 && count < 30) {
    user_level.innerHTML = "등급 : Silver";
    next_level.innerHTML = "Gold";
    left_num.innerHTML = "까지 앞으로" + 30 - count + "개!";
    $(".left_name").css({
      color: "#eb9a01",
    });
  } else if (count >= 30 && count < 45) {
    user_level.innerHTML = "등급 : Gold";
    next_level.innerHTML = "Platinum";
    left_num.innerHTML = "까지 앞으로" + 45 - count + "개!";
    $(".left_name").css({
      color: "#2a9e7b",
    });
  } else if (count >= 45 && count < 60) {
    user_level.innerHTML = "등급 : Platinum";
    next_level.innerHTML = "Diamond";
    left_num.innerHTML = "까지 앞으로" + 60 - count + "개!";
    $(".left_name").css({
      color: "#00b4fc",
    });
  } else if (count >= 60 && count < 75) {
    user_level.innerHTML = "등급 : Diamond";
    next_level.innerHTML = "Ruby";
    left_num.innerHTML = "까지 앞으로" + 75 - count + "개!";
    $(".left_name").css({
      color: "#ff0061",
    });
  } else if (count >= 75) {
    user_level.innerHTML = "등급 : Ruby";
    next_level.innerHTML = "Silver";
    left_num.innerHTML = "Ruby";
    $(".left_name").css({
      color: "#ff0061",
    });
  }

  /*잔디밭 색칠하기*/
  /*
  var dates = "{{dates|safe}}"; // [월, 일 ,월, 일 ...]형식이며 두 개씩세트
  var count = "{{count|safe}}";
  //각 1월, 2월, 3월, 4월 .. 날짜 수 배열.
  var date_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

  const split_date = dates.split(",");

  const str1 = split_date.join(); //다시 문자열로 변환
  const str2 = str1.substring(1, str1.length - 1); //양끝[] 문자 빼기
  const mypost_dates = str2.split(", "); // 띄어쓰기 + , 다시 split

  for (var i = 0; i < mypost_dates.length - 1; i += 2) {
    mypost_dates[i] = mypost_dates[i].substring(1, mypost_dates[i].length - 1);
    mypost_dates[i + 1] = mypost_dates[i + 1].substring(
      1,
      mypost_dates[i + 1].length - 1
    ); // 양끝 작은 따옴표 제거
    mypost_dates[i] = parseInt(mypost_dates[i]); // 계산을 위해 숫자로 변환.
    mypost_dates[i + 1] = parseInt(mypost_dates[i + 1]); // 계산을 위해 숫자로 변환.
  }
  for (var i = 0; i < mypost_dates.length - 1; i += 2) {
    var month_sum = mypost_dates[i] - 1;
    var sum = 0;
    for (var k = 0; k < month_sum; k++) {
      sum += date_in_month[k];
    }
    var week_nth = sum / 7 + 1; //몇 번째 주차의
    var final_nth = (sum % 7) + mypost_dates[i + 1]; //몇 번째 일에 post올림을 기록.
    $(
      ".week:nth-child(" + week_nth + ") .day:nth-child(" + final_nth + ")"
    ).css({
      "background-color": "#a1d177;",
    });
  }

  console.log(mypost_dates);
*/
  //만약 기록했던 글로 이동하고 싶다면,? a태그 href 바꾸는 법.
  // $("#linkMyBlog").attr("href", "http://ozit.tistory.com")
});
