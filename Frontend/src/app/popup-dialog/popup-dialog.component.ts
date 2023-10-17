import { Component, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { Router } from '@angular/router';

@Component({
  selector: 'app-popup-dialog',
  templateUrl: './popup-dialog.component.html',
  styleUrls: ['./popup-dialog.component.css']
})
export class PopupDialogComponent {
  //dialogTitle: string;
  dialogContent: string;
  redirectAfter: boolean;
  router: Router;

  constructor(
    public dialogRef: MatDialogRef<PopupDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any,
  ) {
    //this.dialogTitle = data.dialogTitle;
    this.dialogContent = data.dialogContent;
  }

  closeDialog(): void {
    this.dialogRef.close();
  }
}
