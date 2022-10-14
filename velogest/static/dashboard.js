const selector = document.getElementById('sensor-id');

// déclencher quelquechose lorsque la valeur du select change
selector.addEventListener('change', function () {
    // faire une requête ajax pour récupérer des données
    fetch("/velogest/observations?sensor_id=" + selector.value)
        .then(response => {
            // indicates whether the response is successful (status code 200-299) or not
            if (!response.ok) {
                throw new Error(`Request failed with status ${response.status}`)
            }
            console.log('fetched')
            return response.json()
        })
        .then(data => {
            // ici on traite les données
            var chartData = [
                {
                    x: data.dates,
                    y: data.comptes,
                    type: 'scatter'
                }
            ];

            Plotly.newPlot('chart', chartData);
        })
        .catch(error => console.log(error))
})