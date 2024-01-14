import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { BackstoryComponent } from './DnD/Character/backstory/backstory.component';
import { CharacterComponent } from './DnD/Character/character/character.component';
import { SkillComponent } from './DnD/Character/skill/skill.component';

@NgModule({
  declarations: [
    AppComponent,
    BackstoryComponent,
    CharacterComponent,
    SkillComponent
  ],
  imports: [
    BrowserModule, HttpClientModule
  //  ,Character
  //  ,Skill
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
