import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-list-users',
  templateUrl: './list-users.component.html',
  styleUrls: ['./list-users.component.css']
})
export class ListUsersComponent {
  users: any[] = [];

  constructor(
    public dialogRef: MatDialogRef<ListUsersComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any
  ) {
    this.users = data.users || [];
  }

  closeDialog() {
    this.dialogRef.close();
  }
}
