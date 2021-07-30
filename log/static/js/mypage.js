$(document).ready(function () {
  var week = 52; //1년은 52주
  for (var a = 0; a < week; a++) {
    $(".count_day").append('<div class="week"></div>');
  }

  for (var a = 0; a < 7; a++) {
    $(".week").append('<div class="day"></div>');
  }
  $(".week:nth-child(" + 1 + ")").css({});
  /*프로필 레벨 */
  console.log(post_count);
  var user_level = document.querySelector(".myprofile_rank");
  var next_level = document.querySelector(".next_level");
  var left_num = document.querySelector(".left_num_text");

  user_level.innerHTML = "등급 : " + membership;
  next_level.innerHTML = "다음등급";
  if (post_count >= 0 && post_count < 15) {
    left_num.innerHTML = "까지 앞으로 " + (15 - post_count) + "개!";
    $(".myprofile_rank").css({
      color: "#AD5600",
    });
  } else if (post_count >= 15 && post_count < 30) {
    left_num.innerHTML = "까지 앞으로 " + (30 - post_count) + "개!";

    $(".myprofile_rank").css({
      color: "#435F7A",
    });
  } else if (post_count >= 30 && post_count < 45) {
    left_num.innerHTML = "까지 앞으로 " + (45 - post_count) + "개!";
    $(".myprofile_rank").css({
      color: "#EA9A01",
    });
  } else if (post_count >= 45 && post_count < 60) {
    left_num.innerHTML = "까지 앞으로 " + (60 - post_count) + "개!";

    $(".myprofile_rank").css({
      color: " #3CA382",
    });
  } else if (post_count >= 60 && post_count < 75) {
    left_num.innerHTML = "까지 앞으로 " + (75 - post_count) + "개!";
    $(".myprofile_rank").css({
      color: "#00B4FC",
    });
  } else if (post_count >= 75) {
    left_num.innerHTML = "Ruby";

    $(".myprofile_rank").css({
      color: "#FF0060",
    });
  }
  console.log(dates);
  /*잔디밭 색칠하기*/

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
    console.log(sum / 7);
    var final_nth = 0;
    var week_nth = Math.floor(sum / 7) + Math.floor(mypost_dates[i + 1] / 7); //몇 번째 주차의
    if ((sum % 7) + (mypost_dates[i + 1] % 7) > 7) {
      week_nth += 1;
      final_nth = (sum % 7) + (mypost_dates[i + 1] % 7) - 7;
      console.log(1);
    } else {
      final_nth = (sum % 7) + (mypost_dates[i + 1] % 7);
      console.log(sum % 7);
      console.log(mypost_dates[i + 1]);
      console.log(final_nth);
    }

    $(
      ".week:nth-child(" + week_nth + ") .day:nth-child(" + final_nth + ")"
    ).css({
      "background-color": "#a1d177",
    });
  }

  console.log(mypost_dates);

  //만약 기록했던 글로 이동하고 싶다면,? a태그 href 바꾸는 법.
  // $("#linkMyBlog").attr("href", "http://ozit.tistory.com")
});
