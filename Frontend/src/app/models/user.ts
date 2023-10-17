import { Route } from "./route";

export class User{
    id: number;
    forename: string;
    surname: string;
    email: string;
    password: string;
    phone: string;
    photo: string;
    role: string;
    routes: Route[];
    status: string;
}