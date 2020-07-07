$('.collapse').collapse()

$('.toast').toast(option)



jQuery(document).ready(function($) {

    function getLocation(location) {
      const source = "https://us1.locationiq.com/v1/search.php";
      let lat, lon, city;
      $.ajax({
        url: source,
        data: {
          key: 'pk.98d5caba4d405a8c28a83739d701d685',
          q: location,
          format: 'json'
        },
        beforeSend: function() {
          $('.spinner').show();
          $('.result').hide();
        },
        success: function(loc) {
          lat = loc[0].lat;
          lon = loc[0].lon;
          city = loc[0].display_name;
          getWeather(lat, lon, city);
        }
      });
    }
  
    function getWeather(lat, lon, city) {
      const source = "https://api.darksky.net/forecast/b9336b84270312124f14740b9b951a32/" + lat + "," + lon;
      let tempF, dewF;
      $.ajax({
        url: source,
        dataType: 'jsonp',
        complete: function() {
          $('.spinner').hide();
          $('.result').fadeIn('slow');
        },
        success: function(weather) {
          tempF = weather.currently.temperature;
          dewF = weather.currently.dewPoint;
          $('.condition').text('The current weather for ' + city + ' is ' + weather.currently.summary);
          $('.temperature span').html(weather.currently.temperature + ' &deg;F');
          $('.humidity span').text((parseFloat(weather.currently.humidity) * 100).toFixed(0) + '%');
          $('.dewpoint span').html(weather.currently.dewPoint + ' &deg;F');
        }
      });
      $('#convert').off('click').on('click', function(e) { // remove the 'click' event and attach it again
        e.preventDefault(); // prevent default behavior of the button
        convertToC(tempF, dewF);
      });
    }
  
    function convertToC(tempF, dewF) {
      if ($('#convert').text().indexOf('Display Celsius') > -1) {
        $('#convert').text('Display Fahrenheit');
        $('.temperature span').html(parseFloat((tempF - 32) * 5 / 9).toFixed(0) + ' &deg;C');
        $('.dewpoint span').html(parseFloat((dewF - 32) * 5 / 9).toFixed(0) + ' &deg;C');
      } else {
        $('#convert').empty().text('Display Celsius');
        $('.temperature span').html(tempF + ' &deg;F');
        $('.dewpoint span').html(dewF + ' &deg;F');
      }
    }
  
    $('#submit').on('click', function(e) {
      const location = $('#country').val();
      getLocation(location);
    });
  });