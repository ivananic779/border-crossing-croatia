import { Component, OnInit } from '@angular/core';
import { ApiService } from './services/api.service';
import { ScaleType, LegendPosition } from '@swimlane/ngx-charts';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent implements OnInit {

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
    }
  ];

  chart_view: [number, number];
  scheme_type: ScaleType;
  // Override colors for certain values
  custom_colors: any[];
  legend_title: string;
  legend_position: LegendPosition;

  constructor(
    public apiService: ApiService
  ) {
    this.chart_view = [1920, 1080];
    this.scheme_type = ScaleType.Ordinal;
    this.custom_colors = [
      {
        name: 'Upit 1',
        value: '#00b0ff'
      }
    ];
    this.legend_title = 'Legenda';
    this.legend_position = LegendPosition.Right;
  }

  ngOnInit() {
    this.apiService.getUkupno().subscribe(data => {
      this.multi = [];
      this.multi[0] = data[0];
      this.multi[1] = data[1];
    });
  }  

  test() {
    console.log(this.multi);
    //this.custom_colors[0].value = '#ff0000';
    //this.scheme_type = ScaleType.Linear;
  }  
  
  select(data: any) {
    console.log('Item clicked', JSON.parse(JSON.stringify(data)));
  }

  activate(data: any) {
    console.log('Activate', JSON.parse(JSON.stringify(data)));
  }

  deactivate(data: any) {
    console.log('Deactivate', JSON.parse(JSON.stringify(data)));
  }

}
