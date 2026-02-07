import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user.service';
import { MatDialog } from '@angular/material/dialog';
import { ListUsersComponent } from '../../dialogs/list-users/list-users.component';
import { AlertDialogComponent } from '../../dialogs/alert/alert-dialog.component';
import { CreateUserComponent } from 'src/app/dialogs/create-user/create-user.component';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  user: any = null;
  users: any[] = [];
  
  constructor(
    private userService: UserService,
    private dialog: MatDialog
  ) { }

  ngOnInit(): void {
    this.userService.getMe().subscribe(
      (response: any) => {
        this.user = response;
      },
      (error: any) => {
        const msg = error?.error?.detail || error?.message || 'Falha ao recuperar informações do usuário';
        this.dialog.open(AlertDialogComponent, { data: { title: 'Erro', message: msg }, width: '400px' });
      }
    );
  }

  loadUsers() {
    this.userService.listUsers().subscribe(
      (response: any) => {
        this.users = response;
        this.openUsersModal();
      },
      (error: any) => {
        const msg = error?.error?.detail || error?.message || 'Falha ao listar usuários';
        this.dialog.open(AlertDialogComponent, { data: { title: 'Erro', message: msg }, width: '400px' });
      }
    );
  }

  openUsersModal() {
    this.dialog.open(ListUsersComponent, {
      width: '600px',
      data: { users: this.users }
    });
  }

  createUser() {
      this.dialog.open(CreateUserComponent, {
        width: '600px'
      }).afterClosed().subscribe(result => {
        if (result) {
          this.loadUsers();
        }
      });
  }

  logout() {
    localStorage.removeItem('access_token');
    window.location.href = '/login';
  }

}
