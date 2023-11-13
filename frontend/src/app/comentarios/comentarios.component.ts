import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';

@Component({
  selector: 'app-comentarios',
  templateUrl: './comentarios.component.html',
  styleUrls: ['./comentarios.component.css'],
  
})
export class ComentariosComponent {

  commentForm: FormGroup;
  comments: any[] = [];
  num_videos_procesados = 0
  num_videos_cargados = 0
  link_video_en_proceso: SafeResourceUrl | undefined;
  text_loading!:string
  url_api_consumer = 'http://127.0.0.1:8000/analizar-comentarios/'

  constructor(private http: HttpClient, private sanitizer: DomSanitizer) {
    this.commentForm = new FormGroup({
      videoUrls: new FormControl('', Validators.required)
    });
  }


  analizarComentarios() {
    const videoUrls = this.commentForm.get('videoUrls')?.value.split(',');
    this.num_videos_cargados = videoUrls.length
    this.comments = [];  // Limpiar el array de comentarios
    this.num_videos_procesados=0
    
    // Funcion recursiva para realizar las peticiones una por una
    const realizarPeticion = (index: number) => {
      if (index < this.num_videos_cargados) {
        
        const url = videoUrls[index];
        this.text_loading = 'Escrapeando...'
        this.num_videos_procesados = index + 1

        this.http.post<any>(this.url_api_consumer, { video_urls: [url] }).subscribe(
          (data) => {
            // this.comments.push(data);

            data.forEach((comentario: any) => {
              this.comments.unshift(comentario);
            });

            // Llamo recursivamente para la siguiente URL
            realizarPeticion(index + 1);
            // this.num_videos_procesados = index + 1
          },
          (error) => {
            console.error(`Error al enviar la solicitud para ${url}.`, error);
            this.comments.push({ error: `Error al analizar comentarios para ${url}` });

            // Llamo recursivamente para la siguiente URL
            realizarPeticion(index + 1);
          }

          );
          
        } else{
          this.text_loading = 'Se han escrapeado'
        }   
    }
    // Inicio la secuencia de peticiones
    realizarPeticion(0);
    
  }
  
  
}
