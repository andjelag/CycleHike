import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RoutePageComponent } from './route-page.component';

describe('RoutePageComponent', () => {
  let component: RoutePageComponent;
  let fixture: ComponentFixture<RoutePageComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [RoutePageComponent]
    });
    fixture = TestBed.createComponent(RoutePageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
