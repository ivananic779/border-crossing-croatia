import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent {

  multi = [
    {
      "name": "Germany",
      "series": [
        {
          "name": 1990,
          "value": 62000000
        },
        {
          "name": 2010,
          "value": 73000000
        },
        {
          "name": 2011,
          "value": 89400000
        }
      ]
    },
  
    {
      "name": "USA",
      "series": [
        {
          "name": 1990,
          "value": 250000000
        },
        {
          "name": 2010,
          "value": 309000000
        },
        {
          "name": 2011,
          "value": 311000000
        }
      ]
    },
  
    {
      "name": "France",
      "series": [
        {
          "name": 1990,
          "value": 58000000
        },
        {
          "name": 2010,
          "value": 50000020
        },
        {
          "name": 2011,
          "value": 58000000
        }
      ]
    },
    {
      "name": "UK",
      "series": [
        {
          "name": 1990,
          "value": 57000000
        },
        {
          "name": 2010,
          "value": 62000000
        }
      ]
    }
  ];

  constructor() {
  }
}
