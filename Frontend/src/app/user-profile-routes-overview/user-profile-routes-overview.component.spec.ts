import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UserProfileRoutesOverviewComponent } from './user-profile-routes-overview.component';

describe('UserProfileRoutesOverviewComponent', () => {
  let component: UserProfileRoutesOverviewComponent;
  let fixture: ComponentFixture<UserProfileRoutesOverviewComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [UserProfileRoutesOverviewComponent]
    });
    fixture = TestBed.createComponent(UserProfileRoutesOverviewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
