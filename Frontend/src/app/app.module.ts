import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { SignUpComponent } from './sign-up/sign-up.component';
import { LoginComponent } from './login/login.component';
import { AuthInterceptor } from './_interceptors/auth.interceptor';
import { RoutePageComponent } from './route-page/route-page.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { PopupDialogComponent } from './popup-dialog/popup-dialog.component';
import { MatDialogModule } from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { UserProfileStatisticsComponent } from './user-profile-statistics/user-profile-statistics.component';
import { UserProfileRoutesOverviewComponent } from './user-profile-routes-overview/user-profile-routes-overview.component';
import { UserProfileEditComponent } from './user-profile-edit/user-profile-edit.component';
import { AdminHomeComponent } from './admin-home/admin-home.component';
import { UserListComponent } from './user-list/user-list.component';
import { AdminRoutesOverviewComponent } from './admin-routes-overview/admin-routes-overview.component';
import { AdminRouteAddComponent } from './admin-route-add/admin-route-add.component';
import { MatDatepickerModule } from '@angular/material/datepicker'
import { MatNativeDateModule } from '@angular/material/core';
import { MatInputModule } from '@angular/material/input';
import { MapComponent } from './map/map.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    SignUpComponent,
    LoginComponent,
    RoutePageComponent,
    PopupDialogComponent,
    UserProfileComponent,
    UserProfileStatisticsComponent,
    UserProfileRoutesOverviewComponent,
    UserProfileEditComponent,
    AdminHomeComponent,
    UserListComponent,
    AdminRoutesOverviewComponent,
    AdminRouteAddComponent,
    MapComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule, 
    HttpClientModule,
    FormsModule,
    BrowserAnimationsModule,
    MatDialogModule,
    MatButtonModule,
    MatNativeDateModule,
    MatDatepickerModule,
    MatInputModule
  ],
  providers: [{provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true}],
  bootstrap: [AppComponent]
})
export class AppModule { }
