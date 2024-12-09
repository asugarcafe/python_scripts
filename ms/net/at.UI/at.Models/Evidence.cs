

namespace at.Models {
   public class Evidence {

      public Evidence(string description, Enums.Strength credibility, Enums.Strength relevance) {
         Description = description;
         Credibility = credibility;
         Relevance = relevance;
      }  

      public string Description { get; set; }
      public Enums.Strength Credibility { get; set; }
      public Enums.Strength Relevance { get; set; }



      /*
       
      Evidence can have many attributes, including:
      Purposeful: Evidence is designed to answer specific questions. 
      Representative: Evidence is representative of what is, not just an isolated case. 
      Relevant: Evidence is relevant to the situation. 
      Verifiable: Evidence can be verified. 
      Actionable: Evidence can be used to take action. 
      Cumulative: Evidence is corroborated by multiple sources of data. 
      Coherent: Evidence is sound enough to provide guidance for improvement. 
      Integrated: Evidence is presented in the context of other information. 
      Replicable: Similar results are obtained when the same question is addressed using the identical analysis against similar data. 
      Generalizable: Similar patterns are observed across heterogeneous datasets. 
      Robust: Findings are not overly sensitive to subjective choices. 
      Calibrated: The performance of the evidence generating system can be verified. 
      The Rules of Evidence are Validity, Sufficiency, Authenticity, and Currency. 
      
       */
   }
}
