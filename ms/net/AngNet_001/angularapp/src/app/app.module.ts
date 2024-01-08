import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { Character } from './DnD/Character/Character';

import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent,
    Character
  ],
  imports: [
    BrowserModule, HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
