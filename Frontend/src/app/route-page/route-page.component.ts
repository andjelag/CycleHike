import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { UserService } from '../services/user.service';
import { Route } from '../models/route';
import { RoutesService } from '../services/routes.service';
import { DateUtils } from '../_utils/date-util';
import { MapService } from '../services/map.service';
import { MatDialog } from '@angular/material/dialog';
import { PopupDialogComponent } from '../popup-dialog/popup-dialog.component';
import { User } from '../models/user';

@Component({
  selector: 'app-route-page',
  templateUrl: './route-page.component.html',
  styleUrls: ['./route-page.component.css']
})
export class RoutePageComponent implements OnInit{

  constructor(private router:Router, private _routePath:ActivatedRoute, private userService: UserService, private routesService: RoutesService, private mapService:MapService, public dialog: MatDialog){}

  route: Route;
  id:number;
  routeIsInFuture:boolean;
  routeCapacityFull:boolean;
  user: User;
  userIsAdmin: boolean;
  distance:number;

  ngOnInit(): void {
    this.id = this._routePath.snapshot.params['id'];
    this.routesService.getRouteById(this.id).subscribe((route:Route) => {
      this.route = route;
      this.routeIsInFuture = DateUtils.dateInFuture(route.date);
      this.routeCapacityFull = route.capacityLeft == 0
      this.mapService.calculateRouteDistance(route.gpx).then((totalDistance:number)=>{ this.distance = totalDistance})
    })
    if(this.isLoggedIn()){
      let userId = parseInt(localStorage.getItem('id_token'))
      this.userService.getUser(userId).subscribe((user:User)=>{
        this.user = user
        this.userIsAdmin = user.role == 'admin'
      })
    } 
  }

  ngAfterViewInit(){
    this.mapService.plotRoute(this.id)
  }

  downloadFile(){
    const blob = new Blob([this.route.gpx.toString()], {type:'application/xml'});
    const url = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.target = '_blank';
    link.download = this.route.name+".gpx";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }

  registerUserForRoute(){
    let userId = parseInt(localStorage.getItem('id_token'))
    console.log(userId)
    this.routesService.registerUserForRoute(this.route.id, userId).subscribe((res)=>{
      if(res['message']=="Ok"){
        this.openDialog("", "Uspešno ste se prijavili za akciju!")
      }
      else if(res['message']=="Error"){
        this.openDialog("", "Došlo je do greške, pokušajte ponovo")
      }
      else if(res['message']=="Exists already"){
        this.openDialog("", "Već ste prijavljeni za akciju!")
      }
    })
  }

  openDialog(title: string, content: string): void {
    this.dialog.open(PopupDialogComponent, {
      width: '300px', 
      data: { dialogTitle: title, dialogContent: content } 
    });
  }

  formatedDate(date:Date){
    return DateUtils.formatedDate(date)
  }

  dateInFuture(date:Date){
    return DateUtils.dateInFuture(date);
  }

  isLoggedIn(){
    return this.userService.isLoggedIn()
  }

  logout(){
    return this.userService.logout()
  }

  userProfile(){
    if(this.user.role == 'admin')
      this.router.navigate(['userProfile/editProfile'])
    else
      this.router.navigate(['userProfile'])
  }

  signup(){
    this.router.navigate(['signup'])
  }

  login(){
    this.router.navigate(['login'])
  }

  homePage(){
    if(this.user?.role == 'admin')
      this.router.navigate(['adminHome'])
    else
      this.router.navigate([''])
  }
}
