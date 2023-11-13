import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BusquedaPorTemaComponent } from './busqueda-por-tema.component';

describe('BusquedaPorTemaComponent', () => {
  let component: BusquedaPorTemaComponent;
  let fixture: ComponentFixture<BusquedaPorTemaComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [BusquedaPorTemaComponent]
    });
    fixture = TestBed.createComponent(BusquedaPorTemaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
