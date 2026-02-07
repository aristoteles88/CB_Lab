import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef, MatDialog } from '@angular/material/dialog';
import { UserService } from 'src/app/services/user.service';
import { AlertDialogComponent } from '../alert/alert-dialog.component';

@Component({
  selector: 'app-create-user',
  templateUrl: './create-user.component.html',
  styleUrls: ['./create-user.component.css']
})
export class CreateUserComponent {
  protected name: string = '';
  protected email: string = '';
  protected password: string = '';
  protected is_superuser: boolean = false;

  constructor(
    public dialogRef: MatDialogRef<CreateUserComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any,
    private userService: UserService,
    private dialog: MatDialog
  ) {}

  createUser() {
    this.userService.createNewUser(this.name, this.email, this.password, this.is_superuser).subscribe(
      (response: any) => {
        this.dialogRef.close(true);
        this.dialog.open(AlertDialogComponent, { data: { title: 'Sucesso', message: 'Usuário criado com sucesso.' }, width: '400px' });
      },
      (error: any) => {
        const msg = error?.error?.detail || error?.message || 'Falha ao criar usuário';
        this.dialog.open(AlertDialogComponent, { data: { title: 'Erro', message: msg }, width: '400px' });
      }
    );
  }

  closeDialog() {
    this.dialogRef.close();
  }
}
