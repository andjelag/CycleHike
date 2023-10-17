import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { User } from '../models/user';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent implements OnInit{

  constructor(private router:Router, private userService: UserService){}

  
  user: User;

  ngOnInit(): void {
    if(this.isLoggedIn()){
      let userId = parseInt(localStorage.getItem('id_token'))
      this.userService.getUser(userId).subscribe((user:User)=>{
        this.user = user
        if(this.user.role == 'admin')
          this.router.navigate(['userProfile/editProfile'])
      })
    } else {
      this.router.navigate([''])
    }
  }

  logout(){
    this.userService.logout()
    this.router.navigate([''])
  }

  isLoggedIn(){
    return this.userService.isLoggedIn()
  }
  
  homePage(){
    if(this.user.role == 'admin')
      this.router.navigate(['adminHome'])
    else
      this.router.navigate([''])
  }

  userProfile(){
    if(this.user.role == 'admin')
      this.router.navigate(['userProfile/editProfile'])
    else
      this.router.navigate(['userProfile'])
  }
}
