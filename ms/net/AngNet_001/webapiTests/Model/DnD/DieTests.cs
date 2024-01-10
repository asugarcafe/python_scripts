using Microsoft.VisualStudio.TestTools.UnitTesting;
using webapi.Model.DnD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace webapi.Model.DnD.Tests {
   [TestClass()]
   public class DieTests {
      [TestMethod()]
      public void RollTest() {
         Die d = new Die(6);
         for(int x=0; x< 100; x++) {
            int roll = d.Roll();
            if(roll <1 || roll >6)
               Assert.Fail(roll.ToString());
         }
      }
   }
}