import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';
import { combineLatest } from 'rxjs';

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
  pagination = false
  numTotalComentarios:any = 0
  itemsPerPage = 15; // Número de comentarios por página
  currentPage = 1; // Página actual

  constructor(private http: HttpClient, private sanitizer: DomSanitizer) {
    this.commentForm = new FormGroup({
      videoUrls: new FormControl('', Validators.required)
    });
  }


  nextPage() {
    if (this.currentPage * this.itemsPerPage < this.comments.length) {
      this.currentPage++;
    }
  }

  previousPage() {
    if (this.currentPage > 1) {
      this.currentPage--;
    }
  }

  //funcion para saber cuantas paginas de comenterios hay
  getTotalPages(): number {
    let numTotalPages =  Math.ceil(this.comments.length / this.itemsPerPage);
    return numTotalPages
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
              // valido que la data no sea undefined para ejecutar el foreach
              if (data){
                data.forEach((comentario: any) => {
                  this.comments.unshift(comentario);
                  
                });
                // Llamo recursivamente para la siguiente URL
                realizarPeticion(index + 1);

              } else{
                //la url no tenia comentarios para escrapear
                console.warn(`La respuesta para ${url} es null o undefined.`);
                // Llamo recursivamente para la siguiente URL
                realizarPeticion(index + 1);
              }
              this.numTotalComentarios = this.comments.length
              console.log(this.numTotalComentarios)
          },
          (error) => {

            if (error.status === 404) {
              // Manejar el caso específico de URL no encontrada
              this.comments.push({ error: `La URL ${url} no existe o no está disponible.` });
              console.log(`La URL ${url} no existe o no está disponible.` )
            } else {
              this.comments.push({ error: `Error al analizar comentarios para ${url}` });
              console.log( `Error al analizar comentarios para ${url}`)
            }
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
    console.log(this.comments)
    
  }
  
  
}
