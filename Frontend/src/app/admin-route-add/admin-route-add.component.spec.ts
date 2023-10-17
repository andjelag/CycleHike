import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminRouteAddComponent } from './admin-route-add.component';

describe('AdminRouteAddComponent', () => {
  let component: AdminRouteAddComponent;
  let fixture: ComponentFixture<AdminRouteAddComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [AdminRouteAddComponent]
    });
    fixture = TestBed.createComponent(AdminRouteAddComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
