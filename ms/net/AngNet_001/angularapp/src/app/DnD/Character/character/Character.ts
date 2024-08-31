

export class Character {
  public STR: number;
  public DEX: number;
  public CON: number;
  public INT: number;
  public WIS: number;
  public CHA: number;

  public HP: number;
  public Name: string;
  public Career: string;

  ///TODO: add backpack of gear
  ///TODO: add skill scores
  ///TODO: add gear
  // tslint:disable-next-line: max-line-length
  constructor(Name: string,
    Career: string,
    Hp: number,
    Stats: { [key: string]: number }) {

    this.Name = Name;
    this.Career = Career;
    this.HP = Hp;

    this.STR = Stats['STR'];
    this.DEX = Stats['DEX'];
    this.CON = Stats['CON'];
    this.INT = Stats['INT'];
    this.WIS = Stats['WIS'];
    this.CHA = Stats['CHA'];
  }
}
