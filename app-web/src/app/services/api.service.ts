import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry, tap } from 'rxjs/operators';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  apiUrl = environment.apiUrl;

  constructor(
    private http: HttpClient
  ) {

  }

  // ------------------------------------------------------------

  public getGraph(_request_options: string | { name: string; table: string; date_from: string; date_to: string; }[]): Observable<any> {
    return this.http.post<any>(this.apiUrl + '/get_graph', _request_options)
      .pipe(
        retry(3),
        catchError(this.handleError)
      );
  }

  public getGraphData(_table: string, _date_from: string, _date_to: string): Observable<any> {
    return this.http.post<any>(this.apiUrl + '/get_graph_data', { table: _table, date_from: _date_from, date_to: _date_to })
      .pipe(
        retry(3),
        catchError(this.handleError)
      );
  }

  // same request as above, but console log the response
  public getGraph_log(_request_options: string | { name: string; table: string; date_from: string; date_to: string; }[]): Observable<any> {
    return this.http.post<any>(this.apiUrl + '/get', _request_options)
      .pipe(
        retry(3),
        catchError(this.handleError),
        tap(data => console.log(data))
      );
  }

  private handleError(error: HttpErrorResponse) {
    if (error.status === 0) {
      // A client-side or network error occurred. Handle it accordingly.
      console.error('An error occurred:', error.error);
    } else {
      // The backend returned an unsuccessful response code.
      // The response body may contain clues as to what went wrong.
      console.error(
        `Backend returned code ${error.status}, body was: `, error.error);
    }
    // Return an observable with a user-facing error message.
    return throwError(
      'Something bad happened; please try again later.');
  }

}
