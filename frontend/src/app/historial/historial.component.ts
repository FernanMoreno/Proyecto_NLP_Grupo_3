import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Location } from '@angular/common';

@Component({
  selector: 'app-historial',
  templateUrl: './historial.component.html',
  styleUrls: ['./historial.component.css']
})
export class HistorialComponent implements OnInit {

  
  private apiUrl = 'http://localhost:5000'; // Ajusta la URL de acuerdo a tu configuración
  comentarios: any[] = [];

  constructor(private http: HttpClient, private location:Location) {}

  ngOnInit(): void {
    this.obtenerComentarios().subscribe(
      (data) => {
        this.comentarios = data;
        // console.log('Comentarios obtenidos:', this.comentarios);
      },
      (error) => {
        console.error('Error al obtener comentarios:', error);
      }
    );
  }

  obtenerComentarios(): Observable<any[]> {
    const url = `${this.apiUrl}/datos`;
    return this.http.get<any[]>(url);
  }


  goBack(): void {
    this.location.back();
  }


 

}
