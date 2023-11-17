import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ComentariosComponent } from './comentarios/comentarios.component';
import { BusquedaPorTemaComponent } from './busqueda-por-tema/busqueda-por-tema.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'con-enlaces', component: ComentariosComponent },
  { path: 'por-tema', component: BusquedaPorTemaComponent },
  { path: '', redirectTo: 'home', pathMatch: 'full' }
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
