import { Component, OnInit } from '@angular/core';
import { UserService } from '../services/user.service';
import { User } from '../models/user';
import { DateUtils } from '../_utils/date-util';
import { Route } from '../models/route';
import { Router } from '@angular/router';
import { RoutesService } from '../services/routes.service';

@Component({
  selector: 'app-user-profile-routes-overview',
  templateUrl: './user-profile-routes-overview.component.html',
  styleUrls: ['./user-profile-routes-overview.component.css']
})
export class UserProfileRoutesOverviewComponent implements OnInit {

  constructor(private router:Router, private userService: UserService, private routesSerivice: RoutesService){}

  user:User;
  userFutureRoutes:Route[] = new Array<Route>();
  userDoneRoutes:Route[] = new Array<Route>();

  ngOnInit(): void {
    let userId = parseInt(localStorage.getItem('id_token'))
    this.userService.getUser(userId).subscribe((user:User)=>{
      this.user = user
      this.user.routes.forEach((route)=>{
        if(DateUtils.dateInFuture(route.date)){
          this.userFutureRoutes.push(route)
        }else{
          this.userDoneRoutes.push(route)
        }
      })
    })
  }

  // cancelRoute(routeId){
  //   this.routesSerivice.cancelRouteForUser(routeId, this.user.id).subscribe((res)=>{
  //     //open dialog
  //   })
  // }

  formatedDate(date){
    return DateUtils.formatedDate(date)
  }

  openRoute(route){
    this.router.navigate(['route', `${route.id}`]);
  }
}
