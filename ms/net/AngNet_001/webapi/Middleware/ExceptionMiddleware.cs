using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Diagnostics;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;

public class ExceptionMiddleware {
   private readonly RequestDelegate _next;
   private readonly ILogger<ExceptionMiddleware> _logger;

   public ExceptionMiddleware(RequestDelegate next, ILogger<ExceptionMiddleware> logger) {
      _next = next;
      _logger = logger;
   }

   public async Task InvokeAsync(HttpContext context) {
      try {
         await _next(context);
      }
      catch (Exception ex) {
         _logger.LogError($"Unexpected error: {ex}");
         context.Response.StatusCode = 500;
         context.Response.ContentType = "application/json";

         await context.Response.WriteAsync("Internal Server Error");
      }
   }
}

public static class ExceptionMiddlewareExtensions {
   public static void ConfigureExceptionHandler(this IApplicationBuilder app, ILogger<ExceptionMiddleware> logger) {
      app.UseMiddleware<ExceptionMiddleware>(logger);
   }
}
