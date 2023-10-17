import { Component, OnInit } from '@angular/core';
import { DateUtils } from '../_utils/date-util';
import { PopupDialogComponent } from '../popup-dialog/popup-dialog.component';
import { MatDialog } from '@angular/material/dialog';
import { RoutesService } from '../services/routes.service';
import { Router } from '@angular/router';
import { MapService } from '../services/map.service';
import { GpxParser } from '../_utils/gpx-parser'
import { Peak } from '../models/peak';

@Component({
  selector: 'app-admin-route-add',
  templateUrl: './admin-route-add.component.html',
  styleUrls: ['./admin-route-add.component.css']
})
export class AdminRouteAddComponent implements OnInit {

  constructor(private dialog: MatDialog, private routesService: RoutesService, private router: Router, private mapService: MapService) { }

  name: string = "";
  capacity: string;
  date: Date | null = null;
  gpx: string = "";
  photo: string = "";
  price: string;
  summary: string = "";
  description: string = "";

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
  
  peaksToSend: Peak[];

  ngOnInit(): void {
    this.mapService.initMapForDrawing()

    this.peaks.push({ name: "", elevation: null });
    this.peaksErrorMessages.push({ name: "", elevation: "" });
  }

  addPeak() {
    this.peaks.push({ name: '', elevation: null });
    this.peaksErrorMessages.push({ name: "", elevation: "" });
  }

  removePeak(index) {
    this.peaks.splice(index, 1)
  }

  addRoute() {
    if (this.name == "") {
      this.nameErrorMessage = "Polje ne sme biti prazno"
    } else {
      this.nameErrorMessage = ""
    }
    if (this.summary == "") {
      this.summaryErrorMessage = "Polje ne sme biti prazno"
    }
    else {
      this.summaryErrorMessage = ""
    }
    if (this.description == "") {
      this.descriptionErrorMessage = "Polje ne sme biti prazno"
    }
    else {
      this.descriptionErrorMessage = ""
    }
    if (this.date == null) {
      this.dateErrorMessage = "Morate uneti datum i vreme akcije"
    } else if (!DateUtils.dateInFuture(this.date)) {
      this.dateErrorMessage = "Datum mora biti u buducnosti!"
    }
    else {
      this.dateErrorMessage = ""
    }
    if (this.price == null || this.price == undefined || this.price == "") {
      this.priceErrorMessage = "Polje ne sme biti prazno"
    }
    else if (Number.isNaN(Number(this.price))) {
      this.priceErrorMessage = "Polje mora biti validan broj"
    }
    else if (Number(this.price) < 0) {
      this.priceErrorMessage = "Cena mora biti pozitivan broj"
    }
    else {
      this.priceErrorMessage = ""
    }
    if (this.capacity == null || this.capacity == undefined || this.capacity == "") {
      this.capacityErrorMessage = "Polje ne sme biti prazno"
    }
    else if (Number.isNaN(Number(this.capacity)) || !Number.isInteger(Number(this.capacity))) {
      this.capacityErrorMessage = "Polje mora biti validan ceo broj"
    }
    else if (Number(this.capacity) < 0) {
      this.capacityErrorMessage = "Broj mesta mora biti pozitivan broj"
    }
    else {
      this.capacityErrorMessage = ""
    }
    if (this.gpx == "" && this.mapService.getCoordinatesOfDrawnRoute() == null) {
      this.gpxErrorMessage = "Ruta se mora ucrtati ili se za nju mora obezbediti gpx fajl"
    }
    else if (this.gpx != "" && !GpxParser.gpxIsValid(this.gpx)) {
      this.gpxErrorMessage = "Prilozeni fajl nije u ispravnom formatu"
    }
    else {
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

    if (this.gpxErrorMessage == "" && this.dateErrorMessage == "" && this.nameErrorMessage == "" && this.priceErrorMessage == "" && this.summaryErrorMessage == "" && this.capacityErrorMessage == "" && this.descriptionErrorMessage == "" && !this.errorInPeaks) {
      if (this.photo == "") {
        this.photo = "../../assets/mountain_logo.webp"
      }
      if (this.gpx == "") {
        this.gpx = this.mapService.getGpxFileFromDrawnRoute(this.name)
      }
      this.peaksToSend = new Array<Peak>();
      this.peaks.forEach(peak => {
        this.peaksToSend.push({name: peak.name, elevation: Number(peak.elevation)})        
      });
      this.routesService.addRoute(this.name, this.summary, this.description, this.date, Number(this.capacity), this.gpx, this.photo, Number(this.price), this.peaksToSend).subscribe((res) => {
        if (res['message'] == "Ok") {
          this.openDialog("", "Uspešno ste dodali novu akciju!", true)
          // dodavanje u kalendar 
        } else {
          this.openDialog("", "Došlo je do greške! Pokusajte ponovo kasnije. ")
        }
      })
    }
  }

  filePhotoUpload() {
    const inputNode: any = document.querySelector('#filePhoto');
    if (typeof (FileReader) !== 'undefined') {
      const reader = new FileReader();

      reader.onload = (e: any) => {
        this.photo = e.target.result;
      };
      console.log(this.photo);
      reader.readAsDataURL(inputNode.files[0]);
      this.filePhotoChosenLabel = inputNode.files[0].name;
    }
  }

  fileGpxUpload() {
    const inputNode: any = document.querySelector('#fileGpx');
    if (typeof (FileReader) !== 'undefined') {
      const reader = new FileReader();

      reader.onload = (e: any) => {
        this.gpx = e.target.result as string;
      };
      console.log(this.gpx);
      reader.readAsText(inputNode.files[0]);
      this.fileGpxChosenLabel = inputNode.files[0].name;
    }
  }

  openDialog(title: string, content: string, redirectAfter: boolean = false): void {
    const dialogRef = this.dialog.open(PopupDialogComponent, {
      width: '500px',
      data: { dialogTitle: title, dialogContent: content }
    });

    if (redirectAfter) {
      dialogRef.afterClosed().subscribe(() => {
        this.router.navigate(['/adminHome/routesOverviewForAdmin'])
      })
    }
  }
}
