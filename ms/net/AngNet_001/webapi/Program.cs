using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

public class Startup {
   public void ConfigureServices(IServiceCollection services) {
      // Add services to the container.
      services.AddControllers();
      services.AddLogging();
      // Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
      services.AddEndpointsApiExplorer();
      services.AddSwaggerGen();
   }//blah

   public void Configure(IApplicationBuilder app, IWebHostEnvironment env) {
      //app.ConfigureExceptionHandler(app.Services.GetRequiredService<ILogger<ExceptionMiddleware>>());

      // Configure the HTTP request pipeline.
      if (env.IsDevelopment()) {
         app.UseSwagger();
         app.UseSwaggerUI();
      }

      app.UseHttpsRedirection();
      app.UseAuthorization();
   }
}

public class Program {
   public static void Main(string[] args) {
      var builder = WebApplication.CreateBuilder(args);
      var startup = new Startup();

      startup.ConfigureServices(builder.Services);

      var app = builder.Build();

      startup.Configure(app, app.Environment);
      app.MapControllers();
      app.Run();
   }
}
