import { Component, OnInit } from '@angular/core';
import { RoutesService } from '../services/routes.service';
import { Router } from '@angular/router';
import { Route } from '../models/route';
import { DateUtils } from '../_utils/date-util';
import { UserService } from '../services/user.service';
import { User } from '../models/user';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})

export class HomeComponent implements OnInit {

  routes: Route[];
  searchText: string;
  futureRoutes: Route[];
  searchingUsed: boolean;
  user: User;

  constructor(private router: Router, private routesService: RoutesService, private userService: UserService){
    this.searchText="";
  }

  ngOnInit(): void {
    if(this.isLoggedIn()){
      let userId = parseInt(localStorage.getItem('id_token'))
      this.userService.getUser(userId).subscribe((user:User)=>{
        this.user = user
        if(this.user.role == 'admin')
          this.router.navigate(['adminHome'])
      })
    } 
    this.searchingUsed = false;
    this.routesService.getAllRoutes().subscribe((routes: Route[])=>{
      if(routes){
        this.routes = routes
      }
    })
    this.routesService.getFutureRoutes().subscribe((futureRoutes: Route[])=>{
      if(futureRoutes){
        this.futureRoutes = futureRoutes
      }
    })
  }

  search(){
    this.routesService.searchRoutes(this.searchText).subscribe((routes: Route[])=>{
      if(routes){
        this.routes = routes
        if(this.searchText==''){
          this.searchingUsed = false;
        } else {
          this.searchingUsed = true;
        }
        document.getElementById('routesShown').scrollIntoView({
          behavior: 'smooth'
        });
      }
    })
  }

  formatedDate(date){
    return DateUtils.formatedDate(date)
  }

  openRoute(route){
    this.router.navigate(['route', `${route.id}`]);
  }

  isLoggedIn(){
    return this.userService.isLoggedIn()
  }

  logout(){
    this.userService.logout()
    window.location.reload();
  }

  userProfile(){
    this.router.navigate(['userProfile'])
  }

  signup(){
    this.router.navigate(['signup'])
  }

  login(){
    this.router.navigate(['login'])
  }

  homePage(){
    this.router.navigate([''])
  }
}
