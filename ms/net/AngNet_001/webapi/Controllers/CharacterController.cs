using Microsoft.AspNetCore.Mvc;
using webapi.Model.DnD;
using webapi.Service;

namespace webapi.Controllers {
   [ApiController]
   [Route("[controller]")]
   public class CharacterController : Controller {
      private readonly ILogger<CharacterController> _logger;

      public CharacterController(ILogger<CharacterController> logger) {
         _logger = logger;
      }


      public IEnumerable<Skill> GetSkillList() {
         return Skill.GetBaseSkillList();
      }

      public IActionResult Index() {
         return View();
      }
   }
}
