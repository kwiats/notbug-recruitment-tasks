import { Component } from '@angular/core';
import axios from 'axios';
import { PokemonsService } from './pokemons.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  pokemonsUrl: string[] = [];
  pokemonsName: string[] = [];
  selectedPokemon: any = null;
  showDetailsIndex =-1;

  pokeStats: any[] = [];
  visable: boolean = false;

  constructor(private _apiPokemons: PokemonsService){}


  getPokemons(){
    this.pokemonsUrl = [];
    this.pokemonsName = []
    return axios.get("https://pokeapi.co/api/v2/pokemon?limit=100&offset=0").then((response: any) =>{
      response.data.results.forEach((pokemon: any) => {
        this.pokemonsUrl.push(pokemon.url);
        this.pokemonsName.push(pokemon.name);
      });
    })
  }

  async ngOnInit(){

    await this.getPokemons();
    this.pokeStats = [];
    for (let i = 1; i < this.pokemonsUrl.length; i++) {
      await axios.get(this.pokemonsUrl[i]).then((response: any)=>{
        this.pokeStats.push(response.data);
      });
    }
  }

  onClick(index: number) {
    this.showDetailsIndex = (this.showDetailsIndex === index) ? -1 : index;
  }
}
