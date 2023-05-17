        // Initialize and add the map
        function initMap() {
            // Latitude and longitude of the selected location
            const myLatLng = {
                lat: 51.897692,
                lng: -8.480438
            };
        
            // The map, centered at selected location
            const map = new google.maps.Map(document.getElementById("map"), {
                zoom: 14,
                center: myLatLng
            });
        
            // The marker, positioned at selected location
            const marker = new google.maps.Marker({
                position: myLatLng,
                map: map,
                title: 'Smorrebrod Gastro Bar'
            });
        }
        window.initMap = initMap;