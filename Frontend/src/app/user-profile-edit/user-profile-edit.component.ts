import { Component, OnInit } from '@angular/core';
import { UserService } from '../services/user.service';
import { User } from '../models/user';
import { PopupDialogComponent } from '../popup-dialog/popup-dialog.component';
import { MatDialog } from '@angular/material/dialog';

@Component({
  selector: 'app-user-profile-edit',
  templateUrl: './user-profile-edit.component.html',
  styleUrls: ['./user-profile-edit.component.css']
})
export class UserProfileEditComponent implements OnInit {
  constructor(private userService: UserService,public dialog:MatDialog){}

  user:User;
  photo: string;
  fileChosenLabel: string;

  passwordCheckErrorMessage: string;
  newPasswordErrorMessage: string;
  surnameErrorMessage: string;
  forenameErrorMessage: string;
  phoneErrorMessage: string;
  oldPasswordErrorMessage: string;
  
  pregex1: RegExp= /^[a-zA-Z]/;
  pregex2: RegExp= /(?=.*[A-Z])/;
  pregex3: RegExp=/(?=.*[@$!.%*?&])/;
  pregex4: RegExp=/[A-Za-z\d@$.!%*?&]{8,12}$/;
  pregex5: RegExp=/(?=.*\d)/;

  newPassword: string;
  passwordCheck: string;
  oldPassword: string;

  ngOnInit(): void {
    this.photo=''
    let userId = parseInt(localStorage.getItem('id_token'))
      this.userService.getUser(userId).subscribe((user:User)=>{
        this.user = user
      })
  }

  fileUpload(){
    const inputNode: any = document.querySelector('#file');
    if (typeof (FileReader) !== 'undefined') {
      const reader = new FileReader();
  
      reader.onload = (e: any) => {
        this.photo = e.target.result;
        console.log(this.photo);
      };
      reader.readAsDataURL(inputNode.files[0]);
      this.fileChosenLabel = inputNode.files[0].name;
    }
 }

  editUser(){
    if(this.user.surname==''){
      this.surnameErrorMessage = "Polje ne sme biti prazno!"
    }
    else{
      this.surnameErrorMessage = ''
    }
    if(this.user.forename==''){
      this.forenameErrorMessage = "Polje ne sme biti prazno!"
    }
    else{
      this.forenameErrorMessage = ''
    }
    
    if(this.user.phone=='')
    {
      this.phoneErrorMessage = "Polje ne sme biti prazno!"
    }else{
      this.phoneErrorMessage = ''
    }
    
    if(this.surnameErrorMessage == '' && this.forenameErrorMessage == '' && this.phoneErrorMessage == '')
    {
      if(this.photo==''){
        this.photo=this.user.photo;
      }
      this.userService.updateUser(this.user.id, this.user.forename, this.user.surname, this.user.phone, this.photo).subscribe((res)=>{
        if(res['message']=="Ok"){
          this.openDialog("", "Uspešno ste izmenili podatke.", true)
        }else if(res['message']=="User doesn't exist."){
          this.openDialog("", "Došlo je do greške. Pokušajte ponovo kasnije.")
        }
      })
    }
  }

  changePassword(){
    if(this.newPassword==''){
      this.newPasswordErrorMessage = "Polje ne sme biti prazno!"
    }
    else if(!this.pregex1.test(this.newPassword)){
      this.newPasswordErrorMessage='Lozinka mora da počinje slovom!';
    }
    else if(!this.pregex2.test(this.newPassword)){
      this.newPasswordErrorMessage='Lozinka mora da sadrzi veliko slovo!';
    }
    else if(!this.pregex5.test(this.newPassword)){
      this.newPasswordErrorMessage='Lozinka mora da sadrži broj!';
    }
    else if(!this.pregex3.test(this.newPassword)){
      this.newPasswordErrorMessage='Lozinka mora da sadrži specijalan karakter!';
    }
    else if(!this.pregex4.test(this.newPassword)){
      this.newPasswordErrorMessage='Lozinka mora ima 8 - 12 karaktera!';
    }
    else{
      this.newPasswordErrorMessage = ''
    }
    if(this.passwordCheck==''){
      this.passwordCheckErrorMessage = "Polje ne sme biti prazno!"
    }
    else if(this.newPassword!=this.passwordCheck){
      this.passwordCheckErrorMessage='Lozinke se ne poklapaju!'
    }else{
      this.passwordCheckErrorMessage = ''
    }

    if(this.newPasswordErrorMessage == '' && this.passwordCheckErrorMessage == ''){
      this.userService.changePassword(this.user.id, this.oldPassword, this.newPassword).subscribe((res)=>{
        if(res['message']=="Ok"){
          this.openDialog("", "Uspešno ste promenili lozinku.", true)
        }else {
          this.oldPasswordErrorMessage = "Neispravna lozinka!"
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
        window.location.reload()
      })
    }

  }
}
