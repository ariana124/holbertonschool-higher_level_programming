// Script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and
// displays the value of hello from that fetch in the HTMLs tag DIV#hello
$.ajax({
  type: 'GET',
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  success: function (data) {
    $('div#hello').text(data.hello);
  }
});
