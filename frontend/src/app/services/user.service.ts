import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private apiUrl = environment.apiUrl;

  getMe() {
    const url = `${this.apiUrl}/users/me/`;
    const token = localStorage.getItem('access_token');
    
    return this.http.get(url, {
      headers: new HttpHeaders({
        'Authorization': `Bearer ${token}`
      })
    });
  }

  listUsers() {
    const url = `${this.apiUrl}/users/`;
    const token = localStorage.getItem('access_token');
    
    return this.http.get(url, {
      headers: new HttpHeaders({
        'Authorization': `Bearer ${token}`
      })
    });
  }

  createNewUser(name: string, email: string, password: string, is_superuser: boolean) {
    const url = `${this.apiUrl}/users/`;
    const token = localStorage.getItem('access_token');
    
    return this.http.post(url, { name, email, password, is_superuser}, {
      headers: new HttpHeaders({
        'Authorization': `Bearer ${token}`
      })
    });
  }

  constructor(private http: HttpClient) { }
}
