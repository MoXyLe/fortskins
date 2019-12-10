function addOrUpdateUrlParam(name, value)
{
  var href = window.location.href;
  var regex = new RegExp("[&\\?]" + name + "=");
  if(regex.test(href))
  {
    regex = new RegExp("([&\\?])" + name + "=\\w+");
    window.location.href = href.replace(regex, "$1" + name + "=" + value);
  }
  else
  {
    if(href.indexOf("?") > -1)
      window.location.href = href + "&" + name + "=" + value;
    else
      window.location.href = href + "?" + name + "=" + value;
  }
}

function refreshAt(hours, minutes, seconds) {
    var now = new Date();
    console.log(now);
    var then = new Date();

    if(now.getHours() > hours ||
       (now.getHours() == hours && now.getMinutes() > minutes) ||
        now.getHours() == hours && now.getMinutes() == minutes && now.getSeconds() >= seconds) {
        then.setDate(now.getDate() + 1);
    }
    then.setHours(hours);
    then.setMinutes(minutes);
    then.setSeconds(seconds);

    var timeout = (then.getTime() - now.getTime());
    setTimeout(function() { window.location.reload(true); }, timeout);
}
// $(document).ready(function () {
//   $('#random_sort').on('click', function random () {
//       $.ajax({
//           type: 'GET',
//           url: '/filter',
//           datatype: 'JSON',
//           data: {
//             url: window.location.href
//           },
//           success: function (data) {
//               $('#placeholder').html("")
//               $('#placeholder').append(data)
//           }
//       })
//   });
// });
