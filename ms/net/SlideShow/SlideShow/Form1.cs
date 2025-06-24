namespace SlideShow {
   public partial class Form1 : Form {

      private bool isRunning = false;

      public Form1() {
         InitializeComponent();
      }

      private void fileToolStripMenuItem_Click(object sender, EventArgs e) {

      }

      private void exitToolStripMenuItem_Click(object sender, EventArgs e) {
         Application.Exit();
      }

      private void button1_Click(object sender, EventArgs e) {
         isRunning = !isRunning;
         if (isRunning) {
            button1.Text = "Stop";
         }
         else {
            button1.Text = "Start";
         }
      }

      private void timer1_Tick(object sender, EventArgs e) {

      }
   }
}
