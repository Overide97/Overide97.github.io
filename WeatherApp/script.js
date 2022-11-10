//Using methods here throughout javascript. 

// Creating object called weather using javascript methods
let weather = {
    "apikey": "39b4f1c0087e345a5d4f628830ba7640",
    fetchweather: function(city) {
        fetch(
            "https://api.openweathermap.org/data/2.5/weather?q="
            + city 
            + "&appid=" 
            + this.apikey
/*
Here we used the help document on the website to find what to add to change 
the units to imperial. &units=metric if we want to go to metric system.
*/
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
//Below is where we are getting our data, what the actualy API generates.

//It also shows why we have to use data.weather[0] to get a result.

/*
{"coord":{"lon":-104.9847,"lat":39.7392},
"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],
"base":"stations",
"main":{"temp":280.81,"feels_like":280.81,
        "temp_min":270.68,"temp_max":290.79,"pressure":1006,"humidity":34,
        "sea_level":1006,"grnd_level":831},
"visibility":10000,
"wind":{"speed":0.9,"deg":39,"gust":1.27},
"clouds":{"all":33},"dt":1668007950,
"sys":{"type":1,"id":3449,
"country":"US",
"sunrise":1668001066,
"sunset":1668037791},
"timezone":-25200,
"id":5419384,
"name":"Denver",
"cod":200}
*/

/*
The temperature is automatically set to Kelvin, 
it was changed to imperial above
*/

/*
Herer we are using queryselector to find the id, 
and add text and the proper data to it.
*/
        document.querySelector(".temp").innerText = temp + "° F";
        document.querySelector(".icon").src = "https://openweathermap.org/img/wn/" 
        + icon 
        + "@2x.png";
        document.querySelector(".humidity").innerText = "Humidity: " + humidity + "%";
        document.querySelector(".wind").innerText = "Wind speed " + speed + "km/h";

    },
//This is the search function that will allow us to search different cities
    search: function () {
        this.fetchweather(document.querySelector(".search-bar").value);
    }
};

//This lets us search by clicking the search button.
document
    .querySelector(".city-search")
    .addEventListener("click", function() {
        weather.search();
});

//This is letting us search by waiting for the enter key to be hit.
document
    .querySelector(".search-bar")
    .addEventListener("keyup", function(event){
    if (event.key == "Enter") {
        weather.search();
    }
});

//This is the initial city that loads as soon as the site is pulled up.
weather.fetchweather("oklahoma city")