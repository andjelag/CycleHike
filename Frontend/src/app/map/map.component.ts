import { Component, OnInit } from '@angular/core';
import * as L from 'leaflet';
import 'leaflet-draw';
import { environment } from '../enviorement/enviorenment';
import { MapService } from '../services/map.service';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {
  // private map: L.Map | undefined;
  // private drawnItems: L.FeatureGroup | undefined;

  constructor(private mapService: MapService){}

  ngOnInit() {
    this.mapService.initMapForDrawing();
    // this.initMap();
    // this.initDrawControl();
  }

  // private initMap() {

  //   this.map = L.map('map').setView([44.0165, 21.0059], 7);

  //   L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
  //     maxZoom: 18,
  //     id: 'mapbox/streets-v11',
  //     tileSize: 512,
  //     zoomOffset: -1,
  //     accessToken: environment.MAPBOX_API_KEY
  //   }).addTo(this.map);

  //   this.drawnItems = L.featureGroup().addTo(this.map);
    
  // }

  // private initDrawControl() {
    
  //   const drawOptions = {
  //     draw: {
  //       polyline: true,
  //       polygon: false,
  //       circle: false,
  //       marker: false,
  //       circlemarker: false,
  //       rectangle: false
  //     },
  //     edit: false,
  //   };

  //   const drawControl = new L.Control.Draw(drawOptions);
  //   this.map?.addControl(drawControl);

  //   this.map?.on(L.Draw.Event.CREATED, (e: any) => {
  //     const layer = e.layer;
  //     const coordinates = layer.getLatLngs();
  //     console.log(coordinates)
  //     this.savePolylineToGPX(coordinates);
  //     this.drawnItems?.addLayer(layer);
  //   });

  //   this.map?.on(L.Draw.Event.DELETED, () => {
  //     this.drawnItems?.clearLayers();
  //   });

  // }

  // private savePolylineToGPX(cords){}
}