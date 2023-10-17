import { Component, OnInit } from '@angular/core';
import { Router, NavigationEnd } from '@angular/router';
import { UserService } from '../services/user.service';
import { RoutesService } from '../services/routes.service';
import { User } from '../models/user';

@Component({
  selector: 'app-admin-home',
  templateUrl: './admin-home.component.html',
  styleUrls: ['./admin-home.component.css']
})
export class AdminHomeComponent implements OnInit {

  constructor(private router: Router, private userService: UserService, private routesService: RoutesService) { }

  user: User;
  onStart: boolean;

  ngOnInit(): void {
    const currentUrl = this.router.url;
    if (currentUrl != "/adminHome")
      this.onStart = false
    else
      this.onStart = true

    this.router.events.subscribe((event) => {
      if (event instanceof NavigationEnd) {
        const currentUrl = event.url;
        console.log('Current URL:', currentUrl);
        if (currentUrl != "/adminHome")
          this.onStart = false
        else
          this.onStart = true
      }
    });

    if (this.isLoggedIn()) {
      let userId = parseInt(localStorage.getItem('id_token'))
      this.userService.getUser(userId).subscribe((user: User) => {
        this.user = user
      })
    } else {
      this.homePage()
    }
  }

  clickedLink() {
    this.onStart = false;
  }

  logout() {
    this.userService.logout()
    this.router.navigate([''])
  }

  isLoggedIn() {
    return this.userService.isLoggedIn()
  }

  homePage() {
    this.router.navigate(['adminHome'])
  }

  userProfile() {
    this.router.navigate(['userProfile/editProfile'])
  }
}
