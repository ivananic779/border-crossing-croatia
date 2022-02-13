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
      "name": "",
      "series": [
        {
          "name": new Date('2020-01-01'),
          "value": 0
        },
        {
          "name": new Date('2020-01-01'),
          "value": 0
        },
        {
          "name": new Date('2020-01-01'),
          "value": 0
        }
      ]
    }
  ];

  table_list = [
    'Ukupno ljudi',
    'Autobusi',
    'Osobni automobili',
    'Avioni',
    'Teretna vozila',
    'Plovila',
    'Vlakovi',
    'Ukupno prijevozna sredstva',
    'Cestovni',
    'Pomorski',
    'Rijecni',
    'Zeljeznicki',
    'Zracni'
  ];

  graph_types = [
    'Neto ukupno',
    'Neto domaci',
    'Neto strani',
    'Ulaz ukupno',
    'Ulaz domaci',
    'Ulaz strani',
    'Izlaz ukupno',
    'Izlaz domaci',
    'Izlaz strani'
  ];

  requestOptions = [
    {
      name: '',
      table: '',
      date_from: '',
      date_to: '',
      query_type: ''
    }
  ];

  displayRequestOptionsDialog = false;

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
    this.getRequestOptionsFromStorage();
  }

  ngOnInit() {
    this.getData();
  }

  setRequestOptionsToStorage() {
    localStorage.setItem('requestOptions', JSON.stringify(this.requestOptions));
  }

  getRequestOptionsFromStorage() {
    if (localStorage.getItem('requestOptions') != null) {
      let requestOptions = localStorage.getItem('requestOptions');
      if (requestOptions) {
        this.requestOptions = JSON.parse(requestOptions);
      }
    }
  }

  getData() {
    this.apiService.getUkupno(this.requestOptions).subscribe(data => {
      this.multi = [];
      let i = 0;
      // check data has been returned
      if (data.length > 0) {
        data.forEach((element: { name: string; series: { name: Date; value: number; }[]; }) => {
          element.series.forEach((element2: { name: Date; value: number; }) => {
            // element2.name looks like '12-31', make a date object without a year of it
            let str1 = element2.name.toString();
            // flip dates in str1
            str1 = str1.split('-').reverse().join('-');
            let str2 = '1970-' + str1;
            let date = new Date(str2);
            // remove year from date object
            date.setFullYear(1980);
            // add the date object to the series
            element2.name = date;
          });
          this.multi[i] = element;
          i++;
        });
      } else {
        this.multi = [];
      }
    });
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

  refresh() {
    this.setRequestOptionsToStorage();
    this.getData();
  }

  set_previous_graph_type(_request_option: { name: string; table: string; date_from: string; date_to: string; query_type: string; }) {
    if (this.requestOptions.length > 0) {
      _request_option.query_type = this.requestOptions[this.requestOptions.length - 1].query_type;
    } else {
      _request_option.query_type = '';
    }

    return _request_option;
  }

  // Adds a new request option
  add_new_line() {
    let new_request_option = {
      name: '',
      table: '',
      date_from: '',
      date_to: '',
      query_type: ''
    };

    new_request_option = this.set_previous_graph_type(new_request_option);

    this.requestOptions.push(new_request_option);
  }

  // Removes a request option
  remove_line(data: any) {
    this.requestOptions.splice(this.requestOptions.indexOf(data), 1);
  }

  // Deletes all request options
  delete_all_lines() {
    this.requestOptions = [];
    this.requestOptions = [
      {
        name: '',
        table: '',
        date_from: '',
        date_to: '',
        query_type: ''
      }
    ];

    this.getData();
  }

  edit_line() {
    this.refresh();
    this.displayRequestOptionsDialog = true;
  }
}
