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

  table_list = [
    'ukupno',
    'autobusi',
    'osobni_autmobili',
    'avioni',
    'teretna_vozila',
    'plovila',
    'vlakovi',
    'ukupno_prijevozna_sredstva',
    'cestovni',
    'pomorski',
    'rijecni',
    'zeljeznicki',
    'zracni'
  ];

  query_types = [
    'neto',
  ];

  requestOptions = [
    {
      name: 'Primjer',
      table: 'ukupno',
      date_from: '2021-05-14',
      date_to: '2021-09-30'
    }
  ];

  chart_view: [number, number];
  scheme_type: ScaleType;
  legend_title: string;
  legend_position: LegendPosition;

  constructor(
    public apiService: ApiService
  ) {
    this.chart_view = [1600, 900];
    this.scheme_type = ScaleType.Ordinal;
    this.legend_title = 'Legenda';
    this.legend_position = LegendPosition.Right;
  }

  ngOnInit() {
    this.getData();
  }

  getData() {
    this.apiService.getUkupno().subscribe(data => {
      this.multi = [];
      let i = 0;
      data.forEach((element: { name: string; series: { name: number; value: number; }[]; }) => {
        this.multi[i] = element;
        i++;
      });
    });
  }

  add_new_line() {
    console.log(this.requestOptions);
  }

  remove_line(data: any) {
    console.log('Remove', JSON.parse(JSON.stringify(data)));
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
