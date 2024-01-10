namespace webapi.Model.DnD {
   public class Skill {
      private string _name = string.Empty;
      private string _description = string.Empty;
      private AttributeType _rollAttribute = AttributeType.STR;

      public Skill(string Name, AttributeType RollAttribute, string Description = "") {
         _name = Name;
         _description = Description;
         _rollAttribute = RollAttribute;
      }

      public static List<Skill> GetBaseSkillList() {
         var list = new List<Skill>();
         list.Add(new Skill("Athletics", AttributeType.STR));
         list.Add(new Skill("Acrobatics", AttributeType.DEX));
         list.Add(new Skill("Acrobatics", AttributeType.DEX));
         list.Add(new Skill("Acrobatics", AttributeType.DEX));
         list.Add(new Skill("Arcana", AttributeType.INT));
         list.Add(new Skill("Arcana", AttributeType.INT));
         list.Add(new Skill("Arcana", AttributeType.INT));
         list.Add(new Skill("Arcana", AttributeType.INT));
         list.Add(new Skill("Arcana", AttributeType.INT));
         list.Add(new Skill("Animal Handling", AttributeType.WIS));
         list.Add(new Skill("Animal Handling", AttributeType.WIS));
         list.Add(new Skill("Animal Handling", AttributeType.WIS));
         list.Add(new Skill("Animal Handling", AttributeType.WIS));
         list.Add(new Skill("Animal Handling", AttributeType.WIS));
         list.Add(new Skill("Deception", AttributeType.CHA));
         list.Add(new Skill("Intimidation", AttributeType.CHA));
         list.Add(new Skill("Performance", AttributeType.CHA));
         list.Add(new Skill("Persuasion", AttributeType.CHA));
         return list;
      }
   }
}
