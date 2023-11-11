$.getJSON("https://api.openweathermap.org/data/2.5/weather?q=New%20York&units=imperial&appid=ff14515ff0b0b23d7f693611f672d5c4",
    function(data) {
        console.log(data)
        let icon =
            "http://openweathermap.org/img/wn/" + data.weather[0].icon + ".png";
        let temp = data.main.temp;
        let weather = data.weather[0].main;

        $('.icon').attr('src', icon);
        $('.weather').append(weather);
        $('.temp').append(temp)
    }
);