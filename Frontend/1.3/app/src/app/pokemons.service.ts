import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class PokemonsService {

  constructor(private _http: HttpClient) { }

  getData(url: string){
    return this._http.get(url)
  }

}
