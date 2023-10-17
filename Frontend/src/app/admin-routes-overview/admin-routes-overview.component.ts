import { Component, OnInit } from '@angular/core';
import { Route } from '../models/route';
import { RoutesService } from '../services/routes.service';
import { Router } from '@angular/router';
import { DateUtils } from '../_utils/date-util';
import { MatDialog } from '@angular/material/dialog';
import { PopupDialogComponent } from '../popup-dialog/popup-dialog.component';
import { User } from '../models/user';
import { MapService } from '../services/map.service';
import { GpxParser } from '../_utils/gpx-parser';
import { Peak } from '../models/peak';

@Component({
  selector: 'app-admin-routes-overview',
  templateUrl: './admin-routes-overview.component.html',
  styleUrls: ['./admin-routes-overview.component.css']
})
export class AdminRoutesOverviewComponent implements OnInit {

  constructor(private router: Router, private routesService: RoutesService, private dialog: MatDialog, private mapService:MapService) { }

  futureRoutes: Route[] = new Array<Route>();
  doneRoutes: Route[] = new Array<Route>();

  editRouteShow = false;
  routeToEdit;
  capacity: string;
  price: string;
  gpx: string = ""; // new file loaded
  

  fileGpxChosenLabel: string = "";
  filePhotoChosenLabel: string = "";

  nameErrorMessage: string = "";
  gpxErrorMessage: string = "";
  dateErrorMessage: string = "";
  capacityErrorMessage: string = "";
  priceErrorMessage: string = "";
  summaryErrorMessage: string = "";
  descriptionErrorMessage: string = "";

  peaks = new Array();
  peaksErrorMessages = new Array();
  errorInPeaks: boolean = false;
  

  ngOnInit(): void {
    this.routesService.getAllRoutes().subscribe((routes: Route[]) => {
      routes.forEach((route) => {
        if (DateUtils.dateInFuture(route.date)) {
          this.futureRoutes.push(route)
        } else {
          this.doneRoutes.push(route)
        }
      })
    })

  }

  cancelRoute(routeId) {
    this.routesService.cancelRoute(routeId).subscribe((res) => {
      if (res['message'] == "Ok") {
        this.openDialog("", "Uspešno ste obrisali akciju.", true)
      }
      else {
        this.openDialog("", "Došlo je do greške. Pokušajte kasnije.")
      }
    })
  }

  openDialog(title: string, content: string, refreshDatAfter: boolean = false, changeView: boolean=false): any {
    const dialogRef = this.dialog.open(PopupDialogComponent, {
      width: '500px',
      data: { dialogTitle: title, dialogContent: content }
    });

    if (refreshDatAfter) {
      dialogRef.afterClosed().subscribe(() => {
        this.futureRoutes = new Array<Route>();
        this.doneRoutes = new Array<Route>();
        this.ngOnInit();
      })
    }

    if (changeView) {
      dialogRef.afterClosed().subscribe(() => {
        this.futureRoutes = new Array<Route>();
        this.doneRoutes = new Array<Route>();
        this.ngOnInit();
        this.editRouteShow = false;
      })
    }
  }

  formatedDate(date) {
    return DateUtils.formatedDate(date)
  }

  openRoute(route) {
    this.router.navigate(['route', `${route.id}`]);
  }


  //////// edit
  openEditRoute(id) {
    this.editRouteShow = true;
    this.routesService.getRouteById(id).subscribe((route: Route) => {
      this.routeToEdit = route
      this.routeToEdit.date = new Date(route.date).toISOString().slice(0, 16);
      this.capacity = route.capacity.toString()
      this.price = route.price.toString()
      this.routeToEdit.peaks.forEach(peak => {
        this.peaks.push({name:peak.name, elevation:peak.elevation.toString()})
        this.peaksErrorMessages.push({ name: "", elevation: "" });
      });
      this.mapService.initMapForDrawing()
    })
  }

  addPeak() {
    this.peaks.push({ name: '', elevation: null });
    this.peaksErrorMessages.push({ name: "", elevation: "" });
  }

  removePeak(index) {
    this.peaks.splice(index, 1)
  }

  editRoute(id) {
    if(this.routeToEdit.name==""){
      this.nameErrorMessage="Polje ne sme biti prazno"
    }else{
      this.nameErrorMessage = ""
    }
    if(this.routeToEdit.summary==""){
      this.summaryErrorMessage="Polje ne sme biti prazno"
    }
    else{
      this.summaryErrorMessage = ""
    }
    if(this.routeToEdit.description==""){
      this.descriptionErrorMessage="Polje ne sme biti prazno"
    }
    else{
      this.descriptionErrorMessage = ""
    }
    if(this.routeToEdit.date==null){
      this.dateErrorMessage="Morate uneti datum i vreme akcije"
    }else if(!DateUtils.dateInFuture(this.routeToEdit.date)){
      this.dateErrorMessage = "Datum mora biti u buducnosti!"
    }
    else{
      this.dateErrorMessage = ""
    }
    if(this.price == null || this.price == undefined || this.price == ""){
      this.priceErrorMessage = "Polje ne sme biti prazno"
    }
    else if(Number.isNaN(Number(this.price))){
      this.priceErrorMessage = "Polje mora biti validan broj"
    }
    else if(Number(this.price) < 0){
      this.priceErrorMessage = "Cena mora biti pozitivan broj"
    }
    else {
      this.priceErrorMessage = ""
    }
    if(this.capacity == null || this.capacity == undefined || this.capacity == ""){
      this.capacityErrorMessage = "Polje ne sme biti prazno"
    }
    else if(Number.isNaN(Number(this.capacity)) || !Number.isInteger(Number(this.capacity))){
      this.capacityErrorMessage = "Polje mora biti validan ceo broj"
    }
    else if(Number(this.capacity) < 0){
      this.capacityErrorMessage = "Broj mesta mora biti pozitivan broj"
    }
    else{
      this.capacityErrorMessage = ""
    }
    if(this.routeToEdit.gpx == "" && this.mapService.getCoordinatesOfDrawnRoute() == null && this.gpx == ""){
      this.gpxErrorMessage = "Ruta se mora ucrtati ili se za nju mora obezbediti gpx fajl"
    }
    else if(this.gpx != "" && !GpxParser.gpxIsValid(this.gpx)){
      this.gpxErrorMessage = "Prilozeni fajl nije u ispravnom formatu"
    }
    else{ 
      this.gpxErrorMessage = ""
    }
    this.errorInPeaks = false;
    for (let i = 0; i < this.peaks.length; i++) {
      console.log('obradjuje se element')
      this.peaksErrorMessages[i].name = ""
      this.peaksErrorMessages[i].elevation = ""
      if (this.peaks[i].name == "") {
        this.peaksErrorMessages[i].name = "Polje za ime ne sme biti prazno. "
      } 
      if (this.peaks[i].elevation == null || this.peaks[i].elevation == "") {
        this.peaksErrorMessages[i].elevation = "Polje za visinu ne sme biti prazno"
      }
      else if (Number.isNaN(Number(this.peaks[i].elevation))) {
        this.peaksErrorMessages[i].elevation = "Polje za visinu mora biti validan broj"
      }
      else if (Number(this.peaks[i].elevation) < 0) {
        this.peaksErrorMessages[i].elevation = "Polje za visinu mora biti pozitivan broj"
      }
      if(this.peaksErrorMessages[i].name != "" || this.peaksErrorMessages[i].elevation != "")
        this.errorInPeaks = true;
    }

    if(this.gpxErrorMessage == "" && this.dateErrorMessage == "" && this.nameErrorMessage == "" && this.priceErrorMessage == "" && this.summaryErrorMessage == "" && this.capacityErrorMessage == "" && this.descriptionErrorMessage==""  && !this.errorInPeaks){
      if (this.routeToEdit.id == id) { 
        if(this.gpx == "" && this.mapService.getCoordinatesOfDrawnRoute() != null){
          this.routeToEdit.gpx = this.mapService.getGpxFileFromDrawnRoute(this.routeToEdit.name)
        }else if(this.gpx != ""){
          this.routeToEdit.gpx = this.gpx;
        }
        this.routeToEdit.peaks = new Array<Peak>();
        this.peaks.forEach(peak => {
          this.routeToEdit.peaks.push({name: peak.name, elevation: Number(peak.elevation)})        
      });
        this.routeToEdit.capacity = Number(this.capacity)
        this.routeToEdit.price = Number(this.price)
        this.routesService.editRoute(this.routeToEdit).subscribe((res) => {
          if(res['message']=="Error"){
            this.openDialog("", "Došlo je do greške. Molimo pokušajte kasnije")
          }else if(res['message']=="Capacity minimum"){
            this.openDialog("", "Nije moguće smanjiti kapacitet ispod broja trenutno prijavljenih!")
          }else{
            this.openDialog("", "Uspešno ste izmenili akciju.", false, true)
          }
        })
      } else {
        let dialogRef = this.openDialog("", "Došlo je do greške. Molimo pokušajte kasnije")
      }
    }
  }

  filePhotoUpload() {
    const inputNode: any = document.querySelector('#filePhoto');
    if (typeof (FileReader) !== 'undefined') {
      const reader = new FileReader();

      reader.onload = (e: any) => {
        this.routeToEdit.photo = e.target.result;
      };
      console.log(this.routeToEdit.photo);
      reader.readAsDataURL(inputNode.files[0]);
      this.filePhotoChosenLabel = inputNode.files[0].name;
    }
  }

  fileGpxUpload() {
    const inputNode: any = document.querySelector('#fileGpx');
    if (typeof (FileReader) !== 'undefined') {
      const reader = new FileReader();

      reader.onload = (e: any) => {
        this.routeToEdit.gpx = e.target.result as string;
      };
      console.log(this.routeToEdit.gpx);
      reader.readAsText(inputNode.files[0]);
      this.fileGpxChosenLabel = inputNode.files[0].name;
    }
  }

}
