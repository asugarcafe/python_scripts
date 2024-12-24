using System;
using System.IO;
using System.Speech.Synthesis;
using System.Threading.Tasks;

namespace tts.filereader {
   internal class Program {
      static void Main(string[] args) {
         Random rnd = new Random();
         Func<bool> randomBool = () => { return rnd.Next(2) == 1; };
         
         string ts_text = "C:\\Repos\\github_asugarcafe\\python_scripts\\General Scripts\\h_scripts\\r_time.distortion.cs.txt";
         Dictionary<string,Tuple<bool,bool>> sourcefile = new Dictionary<string, Tuple<bool, bool>>();
         //sourcefile.Add("C:\\Repos\\github_asugarcafe\\python_scripts\\General Scripts\\h_scripts\\r_priming.ap.cs.txt", new Tuple<bool, bool>(true,false));
         sourcefile.Add("C:\\Repos\\github_asugarcafe\\python_scripts\\General Scripts\\h_scripts\\r_reading.comprehension.pegs.txt", new Tuple<bool, bool>(false, false));
         //sourcefile.Add(ts_text, new Tuple<bool, bool>(true, true));

         var tasks = new List<Task>();

         foreach (var file in sourcefile) {

            Action runLoop = () => {
               RunTTSLoop(file.Key, randomize: file.Value.Item1, fastRate: file.Value.Item2);
            };
            Action runRandom = () => {
               RunTTSLoop(file.Key, randomize: (randomBool()) ? file.Value.Item1 : !file.Value.Item1, fastRate: (randomBool()) ? file.Value.Item2 : !file.Value.Item2);
            };

            tasks.Add(Task.Factory.StartNew(runLoop));
            if(file.Key == ts_text)
               tasks.Add(Task.Factory.StartNew(runRandom));
         }

         //RunTTSLoop(sourcefile[0]);
         while (!(Console.KeyAvailable && Console.ReadKey(true).Key == ConsoleKey.Escape)) {
            // do something
         }

         Console.WriteLine("exiting,..");
         Task.WaitAll(tasks.ToArray(), TimeSpan.FromSeconds(30));
      }

      public static void RunTTSLoop(string sourceFile, int loop = 1, bool repeat = false, bool randomize = true, bool fastRate = false) {
         Random rnd = new Random();
         Func<bool> randomBool = () => { return rnd.Next(2) == 1; };
         Func<bool> randomCrit = () => { return rnd.Next(10) == 1; };
         int count = 0;
         // Create an instance of the synthesizer
         using (SpeechSynthesizer synthesizer = new SpeechSynthesizer()) {
            var voices = synthesizer.GetInstalledVoices();
            var voiceList = voices.Select(_ => _.VoiceInfo.Name).ToList();
            while (loop > count || repeat) {
               //string sourceFile = "C:\\Repos\\github_asugarcafe\\python_scripts\\General Scripts\\h_scripts\\r_priming.ap.cs.txt";
               List<string> lines = getFileLines(sourceFile);
               if (randomize)
                  lines = lines.OrderBy(_ => rnd.Next()).ToList();


               foreach (string statement in lines) {
                  // Configure the synthesizer (optional)
                  synthesizer.SelectVoice(voiceList[rnd.Next(0, voiceList.Count)]);
                  synthesizer.Volume = (randomCrit()) ? 65 - rnd.Next(1, 25) : 30 - rnd.Next(1, 25);  // 0...100
                  synthesizer.Rate = (fastRate || randomCrit()) ? rnd.Next(2, 8) : rnd.Next(-7, 1);      // -10...10

                  Console.WriteLine($"v={synthesizer.Volume}:r={synthesizer.Rate}:s={statement}");

                  // Convert text to speech
                  synthesizer.Speak(statement);

                  // Or, to speak asynchronously
                  // synthesizer.SpeakAsync(statement);
                  Thread.Sleep(250);
                  count++;
               }
            }
         }
      }

      static List<string> getFileLines(string fullFilePath) {
         return File.ReadAllLines(fullFilePath).ToList();
      }
   }
}
