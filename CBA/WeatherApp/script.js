let weather = {
    "apikey": "39b4f1c0087e345a5d4f628830ba7640",
    fetchweather: function(city) {
        fetch(
            "https://api.openweathermap.org/data/2.5/weather?q="
            + city 
            + "&appid=" 
            + this.apikey
            + "&units=imperial"
        )
            .then((response) => response.json())
            .then((data) => this.displayweather(data));
    },

    displayweather: function(data) {
        const {name} = data;
        const {icon, description} = data.weather[0];
        const {temp, humidity} = data.main;
        const {speed} = data.wind;
        console.log(name,icon,description,temp,humidity,speed)
        document.querySelector(".city").innerText = "Weather in " 
        + name;
        document.querySelector(".temp").innerText = temp + "° F"; /*kelvin*/
        document.querySelector(".icon").src = "https://openweathermap.org/img/wn/" 
        + icon 
        + "@2x.png";
        document.querySelector(".humidity").innerText = "Humidity: " + humidity + "%";
        document.querySelector(".wind").innerText = "Wind speed " + speed + "km/h";

    },
    
    search: function () {
        this.fetchweather(document.querySelector(".search-bar").value);
    }
};

document
    .querySelector(".search button")
    .addEventListener("click", function() {
        weather.search();
});

document.querySelector(".search-bar").addEventListener("keyup", function(event){
    if (event.key == "Enter") {
        weather.search();
    }
});

weather.fetchweather("oklahoma city")