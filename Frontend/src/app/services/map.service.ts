import { Injectable } from '@angular/core';
import { environment } from '../enviorement/enviorenment';
import * as L from 'leaflet';
import * as omnivore from '@mapbox/leaflet-omnivore'
import * as turf from '@turf/turf';
import { RoutesService } from './routes.service';
import { Route } from '../models/route';

@Injectable({
  providedIn: 'root'
})
export class MapService {

  constructor(private routesService: RoutesService) { }

  apiToken = environment.MAPBOX_API_KEY;

  defaultCoords: number[] = [40, -80]
  defaultZoom: number = 8

  coordinatesOfDrawnRoute;

  plotRoute(id: number) {
    let map = L.map('map').setView(this.defaultCoords, this.defaultZoom);

    map.maxZoom = 100;

    L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/outdoors-v12/tiles/{z}/{x}/{y}?access_token={accessToken}', {
      maxZoom: 18,
      accessToken: this.apiToken
    }).addTo(map);


    let gpxLayerStyle = {
      "color": "#3949AB",
      "weight": 5,
      "opacity": 0.95
    };

    let customLayer = L.geoJson(null, {
      style: gpxLayerStyle
    });

    this.routesService.getRouteById(id).subscribe((route: Route) => {
      const blob = new Blob([route.gpx.toString()], { type: 'application/xml' });
      const url = window.URL.createObjectURL(blob);
      let gpxLayer = omnivore.gpx(url, null, customLayer)
        .on('ready', function () {
          map.fitBounds(gpxLayer.getBounds());
        }).addTo(map);
    })


  }

  calculateRouteDistance(gpx: String) {
    const blob = new Blob([gpx.toString()], { type: 'application/xml' })
    const url = window.URL.createObjectURL(blob)
    return new Promise((resolve, reject) => {
      const gpxLayer = omnivore.gpx(url);

      gpxLayer.on('ready', () => {
        const gpxToGeoJSONObject = gpxLayer.toGeoJSON();
        const totalDistance = turf.length(gpxToGeoJSONObject, { units: 'kilometers' });
        resolve(totalDistance);
      });

      gpxLayer.on('error', (error) => {
        reject(error);
      });
    })
  }

  public initMapForDrawing() {

    this.coordinatesOfDrawnRoute = null

    let map = L.map('map').setView([44.0165, 21.0059], 7);

    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
      maxZoom: 18,
      id: 'mapbox/streets-v11',
      tileSize: 512,
      zoomOffset: -1,
      accessToken: environment.MAPBOX_API_KEY
    }).addTo(map);

    let drawnItems = L.featureGroup().addTo(map);

    //toolbar za crtanje


    const drawOptions = {
      draw: {
        polyline: true,
        polygon: false,
        circle: false,
        marker: false,
        circlemarker: false,
        rectangle: false
      },
      edit: false,
    };

    const drawControl = new L.Control.Draw(drawOptions);
    map?.addControl(drawControl);

    map?.on(L.Draw.Event.CREATED, (e: any) => {
      const layer = e.layer;
      const coordinates = layer.getLatLngs();
      this.coordinatesOfDrawnRoute = coordinates
      drawnItems?.addLayer(layer);
    });

    map?.on(L.Draw.Event.DELETED, () => {
      drawnItems?.clearLayers();
    });
  }

  getCoordinatesOfDrawnRoute() {
    return this.coordinatesOfDrawnRoute
  }

  getGpxFileFromDrawnRoute(name: string) {
    const gpxData = `<?xml version="1.0" encoding="UTF-8"?>
      <gpx version="1.1" creator="Andjela Glisovic">
        <trk>
          <name>${name}</name>
          <trkseg>
            ${this.coordinatesOfDrawnRoute.map(coord => `<trkpt lat="${coord.lat}" lon="${coord.lng}"></trkpt>`).join('\n')}
          </trkseg>
        </trk>
      </gpx>`;
    return gpxData
  }
}
