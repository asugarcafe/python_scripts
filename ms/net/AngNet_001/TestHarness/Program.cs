// See https://aka.ms/new-console-template for more information

// Build the circuit
using SpiceSharp.Components;
using SpiceSharp;
using SpiceSharp.Simulations;


// Build the circuit
var ckt = new Circuit(
    new VoltageSource("V1", "in", "0", 1.0),
    new Resistor("R1", "in", "out", 1.0e4),
    new Resistor("R2", "out", "0", 2.0e4)
    );


var ckt_555 = new Circuit(
   );


// Create a DC simulation that sweeps V1 from -1V to 1V in steps of 100mV
var dc = new DC("DC 1", "V1", -1.0, 1.0, 0.2);

// Create exports
var inputExport = new RealVoltageExport(dc, "in");
var outputExport = new RealVoltageExport(dc, "out");
var currentExport = new RealPropertyExport(dc, "V1", "i");

// Catch exported data
dc.ExportSimulationData += (sender, args) => {
   Console.WriteLine(string.Format("{0:00.00} I/O {1:00.000} --C: {2}", inputExport.Value, outputExport.Value, currentExport.Value.ToString("E5")));
   var input = inputExport.Value;
   var output = outputExport.Value;
   var current = currentExport.Value;
};
dc.Run(ckt);

var sta = dc.Statistics;

Console.WriteLine(dc.Status);
int q = Console.Read();