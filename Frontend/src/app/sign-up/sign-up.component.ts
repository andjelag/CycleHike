import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UserService } from '../services/user.service';
import { MatDialog } from '@angular/material/dialog';
import { PopupDialogComponent } from '../popup-dialog/popup-dialog.component';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css']
})
export class SignUpComponent {

  constructor(private router:Router, private userService: UserService, public dialog:MatDialog){}

  emailErrorMessage: string;
  passwordErrorMessage: string;
  passwordCheckErrorMessage: string;
  surnameErrorMessage: string;
  forenameErrorMessage: string;
  phoneErrorMessage: string;

  fileChosenLabel:string;

  email: string;
  password: string;
  passwordCheck: string;
  surname: string;
  forename: string;
  phone: string;
  photo: string;
  message: string;
  erregex: RegExp=/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
  pregex1: RegExp= /^[a-zA-Z]/;
  pregex2: RegExp= /(?=.*[A-Z])/;
  pregex3: RegExp=/(?=.*[@$!.%*?&])/;
  pregex4: RegExp=/[A-Za-z\d@$.!%*?&]{8,12}$/;
  pregex5: RegExp=/(?=.*\d)/;

  ngOnInit(): void {
    if(this.userService.isLoggedIn()){
      this.homePage()
    }
    this.message=""
    this.fileChosenLabel="Slika nije izabrana"
    this.emailErrorMessage=""

    this.email = "";
    this.password = "";
    this.passwordCheck = "";
    this.surname = "";
    this.forename = "";
    this.phone = "";
    this.photo = "";
  }

  fileUpload(){
    const inputNode: any = document.querySelector('#file');
    if (typeof (FileReader) !== 'undefined') {
      const reader = new FileReader();
  
      reader.onload = (e: any) => {
        this.photo = e.target.result;
      };
      console.log(this.photo);
      reader.readAsDataURL(inputNode.files[0]);
      this.fileChosenLabel = inputNode.files[0].name;
    }
  }

  registerUser(){
    if(this.email==''){
      this.emailErrorMessage = "Polje ne sme biti prazno!"
    }else if(!this.erregex.test(this.email)){
      this.emailErrorMessage = "Mail mora biti u formatu korisnik@mail.com"
    }else{
      this.emailErrorMessage = ''
    }
    if(this.surname==''){
      this.surnameErrorMessage = "Polje ne sme biti prazno!"
    }
    else{
      this.surnameErrorMessage = ''
    }
    if(this.forename==''){
      this.forenameErrorMessage = "Polje ne sme biti prazno!"
    }
    else{
      this.forenameErrorMessage = ''
    }
    if(this.password==''){
      this.passwordErrorMessage = "Polje ne sme biti prazno!"
    }
    else if(!this.pregex1.test(this.password)){
      this.passwordErrorMessage='Lozinka mora da počinje slovom!';
    }
    else if(!this.pregex2.test(this.password)){
      this.passwordErrorMessage='Lozinka mora da sadrzi veliko slovo!';
    }
    else if(!this.pregex5.test(this.password)){
      this.passwordErrorMessage='Lozinka mora da sadrži broj!';
    }
    else if(!this.pregex3.test(this.password)){
      this.passwordErrorMessage='Lozinka mora da sadrži specijalan karakter!';
    }
    else if(!this.pregex4.test(this.password)){
      this.passwordErrorMessage='Lozinka mora ima 8 - 12 karaktera!';
    }
    else{
      this.passwordErrorMessage = ''
    }
    if(this.passwordCheck==''){
      this.passwordCheckErrorMessage = "Polje ne sme biti prazno!"
    }
    else if(this.password!=this.passwordCheck){
      this.passwordCheckErrorMessage='Lozinke se ne poklapaju!'
    }else{
      this.passwordCheckErrorMessage = ''
    }
    if(this.phone=='')
    {
      this.phoneErrorMessage = "Polje ne sme biti prazno!"
    }else{
      this.phoneErrorMessage = ''
    }
    
    if(this.emailErrorMessage == '' && this.surnameErrorMessage == '' && this.forenameErrorMessage == '' && this.passwordErrorMessage == '' && this.passwordCheckErrorMessage == '' && this.phoneErrorMessage == '')
    {
      if(this.photo==''){
        this.photo="../assets/user_icon.png";
      }
      this.userService.register(this.email, this.password, this.forename, this.surname, this.photo, this.phone).subscribe((res)=>{
        if(res['message']=="Ok"){
          this.openDialog("", "Uspešno ste se registrovali! Nalog ce biti aktivan najkasnije dva radna dana od uplate članarine, koju možete uplatiti uživo u kancelarijama društva ili na račun.", true)
          // dodavanje u kalendar 
        }else if(res['message']=="Email already exists."){
          this.openDialog("", "Vec postoji nalog sa datim emailom! Pokusajte da se prijavite. ")
        }
      })
    }
  }

  openDialog(title: string, content: string, redirectAfter:boolean = false): void {
    const dialogRef = this.dialog.open(PopupDialogComponent, {
      width: '500px', 
      data: { dialogTitle: title, dialogContent: content } 
    });

    if(redirectAfter){
      dialogRef.afterClosed().subscribe(()=>{
        this.router.navigate([''])
      })
    }

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
