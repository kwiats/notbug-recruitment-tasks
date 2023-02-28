import { Component, OnInit } from '@angular/core';
import { CarService } from '../car.service';

@Component({
  selector: 'app-car-details',
  templateUrl: './car-details.component.html',
  styleUrls: ['./car-details.component.css']
})
export class CarDetailsComponent implements OnInit{

  cars: any[] = [];

  ngOnInit() {
    const data = JSON.parse(localStorage.getItem('cards') || '[]');
    console.log(data)
    this.cars = data
  }

}
