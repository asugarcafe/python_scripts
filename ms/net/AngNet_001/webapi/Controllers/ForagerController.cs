using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using webapi.Service;

namespace webapi.Controllers {
   [ApiController]
   [Route("api/[controller]")]
   public class DiceController : ControllerBase {

      private static readonly string[] Summaries = new[]
      {
        "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
    };

      private readonly ILogger<DiceController> _logger;

      public DiceController(ILogger<DiceController> logger) {
         _logger = logger;
      }

      [HttpGet(Name = "GetWeatherForecast")]
      public IEnumerable<ForagerLocation> Get() {
         Location l = new Location();
         l.Latitude = 40.66215780228344m;
         l.Longitude = -112.00063798237m;
         ForagerLocation f1 = new ForagerLocation();
         f1.Location = l;
         f1.LocationType = ForageLocationType.Plant;
         f1.Notes = "Muberry Tree";

         ///BSR: the easiest way to ramp this up is to use a google maps favorites list


         ForagerLocation[] locs = new ForagerLocation[] { f1 };
         return Enumerable.Select(locs, l => new ForagerLocation());
      }

   }
}
