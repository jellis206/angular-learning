import { Component, OnInit } from '@angular/core';
import {Recipe} from "../recipe.model";

@Component({
  selector: 'app-recipe-list',
  templateUrl: './recipe-list.component.html',
  styleUrls: ['./recipe-list.component.css']
})
export class RecipeListComponent implements OnInit {
  recipes: Recipe[] = [
    new Recipe('test recipe', 'a test recipe',
      'https://assets.bonappetit.com/photos/59382129bc13c9448b53deb6/3:4/w_1920%2Cc_limit/Salmon%2520Burger_20170522%2520WEB10249.jpg')
  ];

  constructor() { }

  ngOnInit(): void {
  }

}
