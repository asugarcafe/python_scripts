using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace at.Models {
   public static class Enums {

      public enum LikelyHood {
         HardProof = -1000,
         Compelling = -1,
         Neutral = 0,
         Undefined = 0,
         NotApplicable = 0,
         Inconsistent = 1,
         RulesOut = 1000
      } 

      public enum Strength {
         High = 100,
         Medium = 10,
         Low = 1
      }

   }
}
