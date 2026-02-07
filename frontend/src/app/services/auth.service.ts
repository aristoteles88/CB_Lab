import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = environment.apiUrl;
  
  constructor(private http: HttpClient) {}

  login(email: string, password: string) {
    const url = `${this.apiUrl}/token`;
    // Formata como um formulário URL-encoded
    const body = new URLSearchParams();
    body.set('username', email);
    body.set('password', password);
    
    return this.http.post(url, body.toString(), {
      headers: new HttpHeaders({
        'Content-Type': 'application/x-www-form-urlencoded'
      })
    });
  }
}
