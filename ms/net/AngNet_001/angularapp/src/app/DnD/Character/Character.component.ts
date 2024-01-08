import { Component, OnInit } from '@angular/core';
import { Character } from './Character';

@Component({
  selector: 'app-character',
  templateUrl: './Character.component.html',
  styleUrls: ['./Character.component.css']
})
export class CharacterComponent implements OnInit {
  public Character: Character;

  constructor() {
    var stats: { [key: string]: number } = {};
    var skills: { [key: string]: number } = {};

    this.Character = new Character('Tamer Akkad', 'Cult Leader', 8, stats, skills);
    console.log(this.Character);
  }

  ngOnInit() {
  }

}
