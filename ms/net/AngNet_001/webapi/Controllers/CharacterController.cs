using Microsoft.AspNetCore.Mvc;
using webapi.Model.DnD;
using webapi.Service;

namespace webapi.Controllers {
   [ApiController]
   [Route("api/[controller]")]
   public class CharacterController : Controller {
      private readonly ILogger<CharacterController> _logger;

      public CharacterController(ILogger<CharacterController> logger) {
         _logger = logger;
      }

      [HttpGet]
      [Route("api/[controller]/BaseSkillList")]
      public IEnumerable<Skill> GetSkillList() {
         return Skill.GetBaseSkillList();
      }

      [HttpGet]
      [Route("api/[controller]/")]
      public IActionResult Index() {
         return View();
      }
   }
}
