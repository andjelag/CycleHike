import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { RoutePageComponent } from './route-page/route-page.component';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { UserProfileStatisticsComponent } from './user-profile-statistics/user-profile-statistics.component';
import { UserProfileRoutesOverviewComponent } from './user-profile-routes-overview/user-profile-routes-overview.component';
import { UserProfileEditComponent } from './user-profile-edit/user-profile-edit.component';
import { AdminHomeComponent } from './admin-home/admin-home.component';
import { AdminRouteAddComponent } from './admin-route-add/admin-route-add.component';
import { AdminRoutesOverviewComponent } from './admin-routes-overview/admin-routes-overview.component';
import { UserListComponent } from './user-list/user-list.component';
import { MapComponent } from './map/map.component';

const routes: Routes = [
  {path: "", component: HomeComponent},
  {path:"login", component: LoginComponent},
  {path:"signup", component: SignUpComponent},
  {path:"route/:id", component:RoutePageComponent},
  {path:'adminHome', component: AdminHomeComponent,children: [
    { path: 'userList', component: UserListComponent},
    { path: 'routesOverviewForAdmin', component: AdminRoutesOverviewComponent},
    { path: 'addRoute', component: AdminRouteAddComponent},
  ]},
  {path:'userProfile', component:UserProfileComponent,children: [
    { path: '', redirectTo: 'statistics', pathMatch: 'full' },
    { path: 'statistics', component: UserProfileStatisticsComponent },
    { path: 'routesOverview', component: UserProfileRoutesOverviewComponent },
    { path: 'editProfile', component: UserProfileEditComponent },
  ]},
  {path:'map', component:MapComponent},
  {path:'**', component: HomeComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
