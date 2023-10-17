import { Component, OnInit } from '@angular/core';
import { User } from '../models/user';
import { Route } from '../models/route';
import { UserService } from '../services/user.service';
import { DateUtils } from '../_utils/date-util';
import { MapService } from '../services/map.service';
import { trigger, state, style, animate, transition } from '@angular/animations';
import { Peak } from '../models/peak';

@Component({
  selector: 'app-user-profile-statistics',
  templateUrl: './user-profile-statistics.component.html',
  styleUrls: ['./user-profile-statistics.component.css']
})
export class UserProfileStatisticsComponent implements OnInit{
  constructor(private userService:UserService, private mapService: MapService){}
  
  user:User;
  userDoneRoutes:Route[] = new Array<Route>();
  totalDistance:number = 0;
  currentDistanceValue:number = 0;
  currentRoutesDoneValue:number = 0;

  ngOnInit(): void {
    let userId = parseInt(localStorage.getItem('id_token'))
    this.userService.getUser(userId).subscribe((user:User)=>{
      this.user = user
      this.user.routes.forEach((route)=>{
        if(!DateUtils.dateInFuture(route.date)){
          this.userDoneRoutes.push(route)
        }
      })
      for(let i = 0; i < this.userDoneRoutes.length; i++){
        let route = this.userDoneRoutes.at(i)
        this.mapService.calculateRouteDistance(route.gpx).then((distance:number)=>{
          this.totalDistance += distance
          if(i==this.userDoneRoutes.length - 1){
            this.startDistanceAnimation();
            this.startRoutesDoneAnimation();
          }
        })
      }
    })
  }

  startDistanceAnimation() {
    const duration = 2000; 
    const steps = 100; 
    const increment = (this.totalDistance - this.currentDistanceValue) / steps;

    const interval = setInterval(() => {
      this.currentDistanceValue += increment;
      if (this.currentDistanceValue >= this.totalDistance) {
        this.currentDistanceValue = this.totalDistance;
        clearInterval(interval); 
      }
    }, duration / steps);
  }

  startRoutesDoneAnimation() {
    const duration = 2000; 
    const steps = 100; 
    const increment = (this.userDoneRoutes.length - this.currentRoutesDoneValue) / steps;

    const interval = setInterval(() => {
      this.currentRoutesDoneValue += increment;
      if (this.currentRoutesDoneValue >= this.userDoneRoutes.length) {
        this.currentRoutesDoneValue = this.userDoneRoutes.length;
        clearInterval(interval); 
      }
    }, duration / steps);
  }

}
