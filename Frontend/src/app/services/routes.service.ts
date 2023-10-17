import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { Route } from '../models/route';
import { Peak } from '../models/peak';

@Injectable({
  providedIn: 'root'
})
export class RoutesService {

  constructor(private http: HttpClient) { }
  
  uri = "http://localhost:5000/routes"

  searchRoutes(searchText:string){
    const body = {
      searchText:searchText
    }
    return this.http.post(`${this.uri}/getRoutes`, body)
  }

  getAllRoutes(){
    return this.http.get(`${this.uri}/getAllRoutes`)
  }

  getFutureRoutes(){
    return this.http.get(`${this.uri}/getFutureRoutes`)
  }

  getRouteById(id:number){
    const body = {id:id}
    return this.http.post(`${this.uri}/getRouteById`, body)
  }

  registerUserForRoute(routeId: number, userId: number){
    const body = {
      routeId: routeId,
      userId: userId
    }
    return this.http.post(`${this.uri}/registerUserForRoute`, body)
  }

  cancelRouteForUser(routeId: number, userId: number){
    const body = {
      routeId: routeId,
      userId: userId
    }
    return this.http.post(`${this.uri}/cancelRouteForUser`, body)
  }

  cancelRoute(id){
    const body = {
      id:id
    }
    return this.http.post(`${this.uri}/cancelRoute`, body)
  }

  addRoute(name:string, summary:string, description:string, date:Date, capacity:number, gpx:string, photo:string, price:number, peaks: Peak[]){
    const body = {
      name:name,
      capacity:capacity,
      summary: summary,
      description: description,
      date: date,
      photo: photo,
      gpx: gpx,
      price: price,
      peaks: peaks
    }
    return this.http.post(`${this.uri}/addRoute`, body)
  }

  editRoute(route: Route){
    const body = {
      id: route.id,
      name:route.name,
      capacity:route.capacity,
      summary: route.summary,
      description: route.description,
      date: route.date,
      photo: route.photo,
      gpx: route.gpx,
      price: route.price,
      peaks: route.peaks
    }
    return this.http.post(`${this.uri}/editRoute`, body)
  }
}
