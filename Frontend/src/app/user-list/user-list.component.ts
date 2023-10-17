import { Component, OnInit } from '@angular/core';
import { UserService } from '../services/user.service';
import { User } from '../models/user';
import { MatDialog } from '@angular/material/dialog';
import { PopupDialogComponent } from '../popup-dialog/popup-dialog.component';

@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.css']
})
export class UserListComponent implements OnInit {

  constructor(private userService: UserService, private dialog: MatDialog) { }

  usersApproved: User[] = new Array<User>();
  usersNotYetApproved: User[] = new Array<User>();

  ngOnInit(): void {
    this.userService.getAllUsers().subscribe((users: User[]) => {
      users.forEach(user => {
        if (user.status == "A")
          this.usersApproved.push(user)
        else
          this.usersNotYetApproved.push(user)
      });
    })
  }

  approveUser(id) {
    this.userService.approveUser(id).subscribe((res) => {
      if (res['message'] == "Ok") {
        this.openDialog("", "Uspešno ste odobrili članarinu.", true)
      }
      else {
        this.openDialog("", "Došlo je do greške. Pokušajte kasnije.")
      }
    })
  }

  deactivateUser(id) {
    this.userService.deactivateUser(id).subscribe((res) => {
      if (res['message'] == "Ok") {
        this.openDialog("", "Uspešno ste poništili članarinu.", true)
      }
      else {
        this.openDialog("", "Došlo je do greške. Pokušajte kasnije.")
      }
    })
  }

  openDialog(title: string, content: string, refreshDatAfter: boolean = false): void {
    const dialogRef = this.dialog.open(PopupDialogComponent, {
      width: '500px',
      data: { dialogTitle: title, dialogContent: content }
    });

    if (refreshDatAfter) {
      dialogRef.afterClosed().subscribe(() => {
        this.usersApproved = new Array<User>();
        this.usersNotYetApproved = new Array<User>();
        this.ngOnInit();
      })
    }
  }
}
