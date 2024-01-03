namespace webapi.Model.DnD {

   [Flags]
   enum PlayableClasses {
      None = 0,
      Barbarian = 1,
      Bard = 2,
      Cleric = 4,
      Druid = 8,
      Fighter = 16,
      Monk = 32,
      Paladin = 64,
      Ranger = 128,
      Rogue = 256,
      Sorcerer = 512,
      Warlocl = 1024,
      Wizard  = 2048,
   }
   public class Profession {
      private int professions = 0;

      public Profession(int CharacterProfessions) {
         professions = CharacterProfessions;
      }
   }
}
