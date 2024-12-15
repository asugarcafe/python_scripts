using System;
using System.IO;
using System.Speech.Synthesis;

namespace tts.filereader {
   internal class Program {
      static void Main(string[] args) {
         Random rnd = new Random();
         bool repeat = true;
         int count = 0;
         int loop = 100;
         // Create an instance of the synthesizer
         using (SpeechSynthesizer synthesizer = new SpeechSynthesizer()) {
            var voices = synthesizer.GetInstalledVoices();
            var voiceList = voices.Select(_ => _.VoiceInfo.Name).ToList();
            while (loop>count || repeat) {
               string sourceFile = "C:\\Repos\\github_asugarcafe\\python_scripts\\General Scripts\\h_scripts\\r_priming.ap.cs.txt";
               List<string> lines = getFileLines(sourceFile);
               lines = lines.OrderBy(_ => rnd.Next()).ToList();
               foreach (string statement in lines) {
                  // Configure the synthesizer (optional)
                  synthesizer.SelectVoice(voiceList[rnd.Next(0, voiceList.Count)]);
                  synthesizer.Volume = 30 - rnd.Next(1, 25);  // 0...100
                  synthesizer.Rate = rnd.Next(-5, 1);      // -10...10

                  Console.WriteLine($"v={synthesizer.Volume}:r={synthesizer.Rate}:s={statement}");
                  // Convert text to speech
                  synthesizer.Speak(statement);

                  Thread.Sleep(400);
                  // Or, to speak asynchronously
                  // synthesizer.SpeakAsync("Hello, welcome to the Text-to-Speech tutorial in C#");
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
