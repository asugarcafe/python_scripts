import { Component, OnInit } from '@angular/core';
import { Character } from './Character'

@Component({
  selector: 'app-character',
  templateUrl: './character.component.html',
  styleUrls: ['./character.component.css']
})
export class CharacterComponent implements OnInit {
  Character: Character;
  constructor() {
    var json = { "STR": 10, "DEX": 10, "CON": 10, "INT": 10, "WIS": 10, "CHA": 10};
    this.Character = new Character("Flibbo Djenkins", "Rogue", 6, json);
  }

  ngOnInit(): void {
  }

}
