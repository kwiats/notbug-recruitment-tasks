import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CarService {

  constructor() { }

  getCars(): any[] {
    const cars = localStorage.getItem('cars');
    if (cars){
      return JSON.parse(cars)
    } else {
      return []
    }
  }

  saveCar(car: any){
    const cars = this.getCars()
    cars.push(car)
    localStorage.setItem('cars', JSON.stringify(cars))
  }

}
