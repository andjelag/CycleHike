import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import * as moment from "moment";

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) { }

  uri = "http://localhost:5000/"

  register(email:string, password:string, forename:string, surname:string, photo:string, phone:string){
    const body = {
      email:email,
      password:password,
      forename:forename,
      surname:surname,
      photo:photo,
      phone:phone
    }
    return this.http.post(`${this.uri}/register`, body);
  }

  getUser(id:number){
    const body = {
      id: id
    }
    return this.http.post(`${this.uri}/getUser`, body)
  }

  updateUser(id:number, forename:string, surname:string, phone:string, photo:string){
    const body = {
      id:id,
      forename:forename,
      surname:surname,
      phone: phone,
      photo: photo
    }
    return this.http.post(`${this.uri}/updateUserInfo`, body)
  }

  changePassword(id:number, oldPassword:string, newPassword:string){
    const body = {
      id:id,
      newPassword:newPassword,
      oldPassword:oldPassword
    }
    return this.http.post(`${this.uri}/updateUserPassword`, body)
  }

  login(email:string, password:string ) {
    const body = {email:email, password: password}
    return this.http.post(`${this.uri}/login`, body);
  }
      
  setSession(authResult) {
    let array = authResult.expiresIn.split(":");
    let seconds = (parseInt(array[0], 10) * 60 * 60) + (parseInt(array[1], 10) * 60) + parseInt(array[2], 10)
    const expiresAt = moment().add(seconds,'second');
    localStorage.setItem('id_token', authResult.userId);
    localStorage.setItem("expires_at", JSON.stringify(expiresAt.valueOf()) );
  }          

  logout() {
    localStorage.removeItem("id_token");
    localStorage.removeItem("expires_at");
  }

  public isLoggedIn() {
      return moment().isBefore(this.getExpiration());
  }

  isLoggedOut() {
      return !this.isLoggedIn();
  }

  getExpiration() {
      const expiration = localStorage.getItem("expires_at");
      const expiresAt = JSON.parse(expiration);
      return moment(expiresAt);
  }    

  getAllUsers(){
    return this.http.get(`${this.uri}/getAllUsers`)
  }

  approveUser(id:number){
    const body = {
      id:id
    }
    return this.http.post(`${this.uri}/approveUser`, body)
  }

  deactivateUser(id:number){
    const body = {
      id:id
    }
    return this.http.post(`${this.uri}/deactivateUser`, body)
  }
}
