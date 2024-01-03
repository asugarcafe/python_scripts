namespace webapi.Service {
   public static class Dice {
      public static int Roll(int Sides, int Rolls) {
         int result = 0;
         var rand = new Random();
         for (int x = 0; x < Rolls; x++) {
            result += rand.Next(1, Sides + 1);
         }
         return result;
      }
   }
}
