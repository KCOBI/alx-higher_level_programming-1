$ ('DIV#toggle_header').click (function (e) {
  if ($ ('header').hasClass ('red')) {
    $ ('header').removeClass ('red');
    $ ('header').addClass ('green');
  } else {
    $ ('header').removeClass ('green');
    $ ('header').addClass ('red');
  }
});
