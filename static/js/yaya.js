var ctx = document.getElementById('myChart2');

var stars = [135850, 52122, 148825, 16939, 9763];
var frameworks = ['React', 'Angular', 'Vue', 'Hyperapp', 'Omi'];

var myChart2 = new Chart(ctx, {
 type: 'bar',
 data: {
    labels: frameworks,
    datasets: [{
        label: 'Github Stars',
        data: stars
    }]
 },
})

regions = JSON.parse('{{data1|safe}}')// c'est la data récupérée qu'on a travaillé avec
       
var xValues =[]
var data_min = []
var data_max = []
var data_moyenne = []

console.log('hello',regions,typeof(regions))

j=0;
for (i=0;i<regions.length;i++){
    // Au lieu de 11 on va ecrire l'id obtenu apartir de combobox
    if(regions[i].id_region===12){
        xValues[j]= regions[i].month
        data_min[j] = regions[i].valeur_min
        data_max[j] = regions[i].valeur_max
        data_moyenne[j] = regions[i].valeur_moyenne
        j++
        
    }
    
};


console.log('hello',xValues,typeof(xValues))
var ctx1 = document.getElementById('myChart1');
var myChart1 = new Chart(ctx1, {
    
    type: "line",
    data: {
    labels: xValues,
    datasets: [{ 
        data: data_max,// c'est la données ajoutées,representation du max
        borderColor: "red",
        fill: false,
        label:"Température maximale"
        }, { 
        data: data_min,// c'est la données ajoutées,representation du min
        borderColor: "green",
        fill: false,
        label:"Température minimale"
        }, { 
        data: data_moyenne,// c'est la données ajoutées,representation du moyenne
        borderColor: "blue",
        fill: false,
        label:"Température moyenne"
        }]
        },
    options: {
        legend: {
        display: true,
        position: 'bottom',
        labels: {
            fontColor: "black",
        }
    },
        scales: {
            yAxes: [{
            ticks: {
                beginAtZero: true
            }
        }]
        }}
    });