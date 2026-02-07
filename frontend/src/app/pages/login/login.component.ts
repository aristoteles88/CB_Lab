import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { MatDialog } from '@angular/material/dialog';
import { AlertDialogComponent } from '../../dialogs/alert/alert-dialog.component';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  protected email: string = '';
  protected password: string = '';

  constructor(
    private authService: AuthService,
    private router: Router,
    private dialog: MatDialog
  ) { }

  ngOnInit(): void {
  }

  loginWithPassword(email: string, password: string) {
    this.authService.login(email, password).subscribe(
      (response: any) => {
        localStorage.setItem('access_token', response.access_token);
        this.router.navigate(['/dashboard']);
      },
      (error: any) => {
        const msg = error?.error?.detail || error?.message || 'Erro ao fazer login.';
        this.dialog.open(AlertDialogComponent, { data: { title: 'Login failed', message: msg }, width: '400px' });
      }
    );
  }
}
