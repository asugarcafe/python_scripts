namespace webapi.Service {
   public class Location {
      public decimal Latitude { get; set; } = 0;
      public decimal Longitude { get; set; } = 0;
      public string Address { get; set; }
      public string City { get; set; }
      public string CountryCode { get; set; }
      public string County {  get; set; }
      public string PostalCode { get; set; }
      public string State { get; set; }

   }
}
