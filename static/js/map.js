// Map to generate location of Shop
function initMap() {
  const uluru = { lat: 55.931674, lng: -3.179050 };
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 14,
    center: uluru
  });
  // Map info window with details of Opening/ Closing times
  const contentString =
    '<div id="firstHeading">Grandpa"s Pocket Watch Shop</div><hr>' +
    '<h2 id="secondHeading">Opening Times</h2>' +
    '<ul><span style="color: #000;"><li><strong>Monday:</strong>&nbsp;&nbsp;08:30-17:30</li>' +
    '<li><strong>Tuesday:</strong>&nbsp;&nbsp;08:30-17:30</li><li><strong>Wednesday:</strong>&nbsp;&nbsp;09:30-17:30</li>' +
    '<li><strong>Thursday:</strong>&nbsp;&nbsp;08:30-17:30</li><li><strong>Friday:</strong>&nbsp;&nbsp;09:30-17:30</li>' +
    '<li><strong>Saturday:</strong>&nbsp;&nbsp;09:00-14:00</li>' +
    '<li><strong>Sunday:</strong>&nbsp;&nbsp;09:00-14:00</li></ul></span>';
  const infowindow = new google.maps.InfoWindow({
    content: contentString,
    Width: 650
  });
  const marker = new google.maps.Marker({
    position: uluru,
    map,
    title: "Grandpa's Pocket Watch Shop"
  });
  // Icon on Map when clicked opens up info window
  marker.addListener("click", () => {
    infowindow.open(map, marker);
  });
}