namespace webapi.Model.DnD {
   public class Die {
      private int _sides = 0;
      private Random _random = new Random();
      public Die(int NumberOfSides) {

         _sides = NumberOfSides;
      }

      public int Roll(int NumberofRoles = 1) {
         int result = 0;
         for(int x=0;x< NumberofRoles;x++)
            result += _random.Next (_sides)+1;
         return result;
      }
   }
}
