$(document).ready(function () {
  var week = 52; //1년은 52주
  for (var a = 0; a < week; a++) {
    $(".count_day").append('<div class="week"></div>');
  }

  for (var a = 0; a < 7; a++) {
    $(".week").append('<div class="count"></div>');
  }
});
