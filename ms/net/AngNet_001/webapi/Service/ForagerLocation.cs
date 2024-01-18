namespace webapi.Service {

   [Flags]
   public enum ForageLocationType {
      Water = 1,
      Fungus = 2,
      Plant = 4,
      Meat = 8,
      Metal = 16,
      Plastic = 32,
   }

   public class ForagerLocation {
      public ForageLocationType LocationType { get; set; } = ForageLocationType.Water;
      public Location Location { get; set; }
      public string Notes { get; set; }

      public ForagerLocation() { }

   }
}
