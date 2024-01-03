namespace webapi.Model.DnD {
   public enum AttributeType {
      STR = 1,
      DEX = 2,
      CON = 4,
      INT = 8,
      WIS = 16,
      CHA = 32,
   }
   public class Attribute {
      ///BSR: handle base vs modified attribute value
      ///TODO: handle base vs modified attribute value 

      private int att_value = 0;
      public AttributeType AttributeName { get; set; }

      public Attribute(AttributeType AttributeType) {
         AttributeName = AttributeType;
         att_value = Service.Dice.Roll(6, 3);
      }
      public Attribute(AttributeType AttributeType, int val) {
         AttributeName = AttributeType;
         att_value = val;
      }

      public int Score {
         get { return att_value; }
         set { att_value = value; }
      }
   }

   public class CharacterAttributes {
      public CharacterAttributes() {
         Attribute STR = new Attribute(AttributeType.STR);
         Attribute DEX = new Attribute(AttributeType.DEX);
         Attribute CON = new Attribute(AttributeType.CON);
         Attribute INT = new Attribute(AttributeType.INT);
         Attribute WIS = new Attribute(AttributeType.WIS);
         Attribute CHA = new Attribute(AttributeType.CHA);
      }
   }

}

