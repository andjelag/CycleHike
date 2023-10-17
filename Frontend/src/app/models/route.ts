import { Peak } from "./peak";

export class Route{
    id: number;
    name: String;
    capacity: number;
    capacityLeft: number;
    date: Date;
    summary: String;
    description: String;
    gpx: String;
    photo:String;
    price:number;
    peaks: Peak[];
}