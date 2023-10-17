import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminRoutesOverviewComponent } from './admin-routes-overview.component';

describe('AdminRoutesOverviewComponent', () => {
  let component: AdminRoutesOverviewComponent;
  let fixture: ComponentFixture<AdminRoutesOverviewComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [AdminRoutesOverviewComponent]
    });
    fixture = TestBed.createComponent(AdminRoutesOverviewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
