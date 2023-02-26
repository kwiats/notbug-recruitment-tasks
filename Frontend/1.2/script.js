const { from } = require("rxjs");
const { filter, map, reduce } = require("rxjs/operators");

let persons = [
  {
    id: 1,
    name: "Jan Kowalski",
  },
  {
    id: 2,
    name: "John Doe",
  },
  {
    id: 3,
    name: "Jarek Kaczka",
  },
];

let ages = [
  {
    person: 1,
    age: 18,
  },
  {
    person: 2,
    age: 24,
  },
  {
    person: 3,
    age: 666,
  },
];

let locations = [
  {
    person: 1,
    country: "Poland",
  },
  {
    person: 3,
    country: "Poland",
  },
  {
    person: 1,
    country: "USA",
  },
];

from(locations)
  .pipe(
    filter((location) => location.country === "Poland"),
    map((location) => location.person),
    map((personId) => ages.find((age) => age.person === personId).age),
    reduce(
      (x, age, index) => {
        x.sum += age;
        x.count = index + 1;
        return x;
      },
      { sum: 0, count: 0 }
    )
  )
  .subscribe((result) => {
    const avgAge = result.sum / result.count;
    console.log(`Average age of persons from Poland is ${avgAge}`);
  });
