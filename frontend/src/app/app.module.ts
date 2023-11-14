import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; // Agrega esta línea
import { HttpClientModule } from '@angular/common/http';


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ComentariosComponent } from './comentarios/comentarios.component';
import { HomeComponent } from './home/home.component';
import { BusquedaPorTemaComponent } from './busqueda-por-tema/busqueda-por-tema.component';
import { NavComponent } from './nav/nav.component';


@NgModule({
  declarations: [
    AppComponent,
    ComentariosComponent,
    HomeComponent,
    BusquedaPorTemaComponent,
    NavComponent
  ],
  imports: [BrowserModule, AppRoutingModule, FormsModule, HttpClientModule, CommonModule, ReactiveFormsModule], 
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
