import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UserService } from '../services/user.service';
import { User } from '../models/user';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(private router: Router, private userService: UserService) { }

  email: string;
  password: string;
  message: string;

  emailErrorMessage: string;
  passwordErrorMessage: string;

  ngOnInit(): void {
    if (this.userService.isLoggedIn()) {
      this.homePage()
    }
    this.message = ""
    this.email = ''
    this.password = ''
  }

  loginUser() {
    if (this.email == '') {
      this.emailErrorMessage = "Polje ne sme biti prazno!"
    } else {
      this.emailErrorMessage = ''
    }
    if (this.password == '') {
      this.passwordErrorMessage = "Polje ne sme biti prazno!"
    }
    else {
      this.passwordErrorMessage = ''
    }
    if (this.emailErrorMessage == '' && this.passwordErrorMessage == '') {
      this.userService.login(this.email, this.password).subscribe((res: any) => {
        if (res['message'] == "Invalid credentials.") {
          this.message = "Korisnik nije pronadjen. Proverite podatke"
        } else {
          this.userService.setSession(res)
          if (res.userId) {
            this.userService.getUser(res.userId).subscribe((user: User) => {
              if (user.role == 'admin')
                this.router.navigate(['adminHome'])
              else
                this.homePage()
            })
          }
        }
      });
    }
  }

  signup() {
    this.router.navigate(['signup'])
  }

  login() {
    this.router.navigate(['login'])
  }

  homePage() {
    this.router.navigate([''])
  }
}
