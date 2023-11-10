import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormControl, FormGroup, Validators } from '@angular/forms';


@Component({
  selector: 'app-comentarios',
  templateUrl: './comentarios.component.html',
  styleUrls: ['./comentarios.component.css']
})
export class ComentariosComponent {

  commentForm: FormGroup;
  comments: any[] = [];

  constructor(private http: HttpClient) {
    this.commentForm = new FormGroup({
      videoUrls: new FormControl('', Validators.required)
    });
  }

  analizarComentarios() {
    const videoUrls = this.commentForm.get('videoUrls')?.value.split(',');

    this.http.post<any>('http://127.0.0.1:8000/analizar-comentarios/', { video_urls: videoUrls }).subscribe(
      (data) => {
        this.comments = data;
        console.log(this.comments)
      },
      (error) => {
        console.error('Error al enviar la solicitud.', error);
        this.comments = [];
      }
    );
  }

}
