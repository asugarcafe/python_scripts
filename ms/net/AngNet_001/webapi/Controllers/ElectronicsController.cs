using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using webapi.Model.DnD;

namespace webapi.Controllers {
   [Route("api/[controller]")]
   [ApiController]
   public class ElectronicsController : ControllerBase {
      private readonly ILogger<ElectronicsController> _logger;

      public ElectronicsController(ILogger<ElectronicsController> logger) {
         _logger = logger;
      }

      //[HttpGet]
      //[Route("api/[controller]/BaseSkillList")]
      //public IEnumerable<Skill> GetSkillList() {
      //   return Skill.GetBaseSkillList();
      //}

      [HttpGet]
      [Route("api/[controller]/CalculateResistance")]
      public ActionResult<double> CalculateResistance(bool IsSeries, double[] resistances) {
         try {
            if (resistances == null || resistances.Length == 0) {
               return Ok(0);
            }

            double totalResistance;
            if (IsSeries) {
               totalResistance = resistances.Sum();
            }
            else {
               totalResistance = 1 / resistances.Sum(r => 1 / r);
            }

            return Ok(totalResistance);
         }
         catch (Exception ex) {
            return StatusCode(500, $"An error occurred: {ex.Message}");
         }
      }
   }
}
