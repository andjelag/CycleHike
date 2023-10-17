import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UserProfileStatisticsComponent } from './user-profile-statistics.component';

describe('UserProfileStatisticsComponent', () => {
  let component: UserProfileStatisticsComponent;
  let fixture: ComponentFixture<UserProfileStatisticsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [UserProfileStatisticsComponent]
    });
    fixture = TestBed.createComponent(UserProfileStatisticsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
