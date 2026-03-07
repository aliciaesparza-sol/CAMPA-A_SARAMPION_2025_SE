// Datos de los puntos de vacunación
const centers = [
    {
        id: 1,
        name: "Edificio Central UJED",
        zone: "Centro",
        address: "Constitución 404 Sur, Zona Centro, C.P. 34000, Durango, Durango",
        coords: [24.0143, -104.6894]
    },
    {
        id: 2,
        name: "UAD Lobos",
        zone: "Norte",
        address: "Av. Universidad Autónoma de Durango 100, Fracc. Jardines de Durango, C.P. 34200, Durango, Durango",
        coords: [24.0313, -104.6538]
    },
    {
        id: 3,
        name: "Universidad Vizcaya",
        zone: "Centro-Poniente",
        address: "Av. Cuauhtémoc 101, Col. Los Ángeles, C.P. 34076, Durango, Durango",
        coords: [24.0236, -104.6730]
    },
    {
        id: 4,
        name: "UTD",
        zone: "Sur",
        address: "Carretera Durango-Mezquital Km 4.5, Gabino Santillán, C.P. 34308, Durango, Durango",
        coords: [23.99026, -104.61765]
    },
    {
        id: 5,
        name: "Universidad Politécnica",
        zone: "Sur-Oriente",
        address: "Carretera Durango-México Km 9.5, Col. El Nayar, C.P. 34300, Durango, Durango",
        coords: [23.9560, -104.5679]
    },
    {
        id: 6,
        name: "Unidad Habitacional Río Dorado",
        zone: "Poniente",
        address: "Fracc. Río Dorado, Durango, Durango",
        coords: [24.0115, -104.6822]
    }
];

// Inicializar el mapa
const map = L.map('map', {
    zoomControl: false
}).setView([24.025, -104.65], 13);

// Añadir control de zoom en una posición más discreta
L.control.zoom({ position: 'bottomright' }).addTo(map);

// Tile layer (Positron de CartoDB - tema claro y limpio)
L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
    subdomains: 'abcd',
    maxZoom: 20
}).addTo(map);

// Icono personalizado de vacuna
const vaccineIcon = L.icon({
    iconUrl: 'https://cdn-icons-png.flaticon.com/512/2864/2864440.png',
    iconSize: [45, 45],
    iconAnchor: [22, 45],
    popupAnchor: [0, -40],
    className: 'orange-marker'
});

// Add CSS for orange markers
const markerStyle = document.createElement('style');
markerStyle.innerHTML = `
    .orange-marker {
        filter: hue-rotate(15deg) brightness(1.1) saturate(1.5) !important;
        drop-shadow: 0 4px 8px rgba(211, 84, 0, 0.4);
    }
    .leaflet-popup-content-wrapper {
        border-top: 5px solid #d35400;
        border-radius: 12px;
    }
    .leaflet-popup-tip {
        background: white;
    }
`;
document.head.appendChild(markerStyle);

const markers = {};

// Poblado de la lista lateral y marcadores
const centerList = document.getElementById('center-list');

centers.forEach(center => {
    // Crear marcador en el mapa
    const marker = L.marker(center.coords, { icon: vaccineIcon }).addTo(map);

    const hours = center.name.includes("Río Dorado") ? "09:00 - 18:00" : "09:00 - 20:00";

    const popupContent = `
        <div style="padding: 5px; font-family: 'Outfit', sans-serif;">
            <h3 style="color: #8b0d2a; margin-bottom: 5px;">${center.name}</h3>
            <p style="font-size: 0.8rem; color: #666; margin-bottom: 4px;"><b>Zona:</b> ${center.zone}</p>
            <p style="font-size: 0.8rem; color: #accent; margin-bottom: 8px;"><b>Horario:</b> ${hours}</p>
            <p style="font-size: 0.85rem; color: #333; line-height: 1.4;">${center.address}</p>
        </div>
    `;

    marker.bindPopup(popupContent);
    markers[center.id] = marker;

    // Crear tarjeta en la sidebar
    const card = document.createElement('div');
    card.className = 'center-card';
    card.innerHTML = `
        <div class="zone">${center.zone}</div>
        <h3>${center.name}</h3>
    `;

    card.addEventListener('click', () => {
        map.flyTo(center.coords, 16, {
            duration: 1.5
        });
        marker.openPopup();
    });

    centerList.appendChild(card);
});

// Ajustar vista para mostrar todos los puntos inicialmente
const group = new L.featureGroup(Object.values(markers));
map.fitBounds(group.getBounds().pad(0.1));
