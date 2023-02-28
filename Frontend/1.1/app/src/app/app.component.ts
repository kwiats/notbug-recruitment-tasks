import { Component} from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'car app'
  newCar = {make: '', model: '', year: '', parts: []};
  newPart = {part: '', cost: 0}
  showDetailsIndex = -1;
  cars: any[] = [];

  saveCar(){
    const savedCars = JSON.parse(localStorage.getItem('cars') || '[]');
    savedCars.push(this.newCar)
    localStorage.setItem('cars', JSON.stringify(savedCars));

    console.log(savedCars);

    this.newCar = {make: '', model: '', year: '', parts: []};
  }

  getCars() {
    const data = JSON.parse(localStorage.getItem('cars') || '[]');

    this.cars = data
  }

  deleteCar(index: number){
    this.cars.splice(index, 1);
    localStorage.setItem('cars', JSON.stringify(this.cars));
  }

  showDetails(index: number){
    console.log(this.showDetailsIndex)
    this.showDetailsIndex = (this.showDetailsIndex === index) ? -1 : index;
    this.newPart = {part: '', cost: 0};
  }

  addPart(index: number) {
    if (this.cars[index].parts){
      this.cars[index].parts.push(this.newPart);
    }else{
      this.cars[index].parts = [this.newPart];
    }
    localStorage.setItem('cars', JSON.stringify(this.cars));
    this.newPart = {part: '', cost: 0};
    this.showDetailsIndex = -1;
  }

  deletePart(car_index: number , part_index: number) {
    this.cars[car_index].parts.splice(part_index, 1);
    localStorage.setItem('cars', JSON.stringify(this.cars));
  }

  ngOnInit() {
    this.getCars();
  }


}
