namespace SlideShow {
   partial class Form1 {
      /// <summary>
      ///  Required designer variable.
      /// </summary>
      private System.ComponentModel.IContainer components = null;

      /// <summary>
      ///  Clean up any resources being used.
      /// </summary>
      /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
      protected override void Dispose(bool disposing) {
         if (disposing && (components != null)) {
            components.Dispose();
         }
         base.Dispose(disposing);
      }

      #region Windows Form Designer generated code

      /// <summary>
      ///  Required method for Designer support - do not modify
      ///  the contents of this method with the code editor.
      /// </summary>
      private void InitializeComponent() {
         components = new System.ComponentModel.Container();
         menuStrip1 = new MenuStrip();
         fileToolStripMenuItem = new ToolStripMenuItem();
         exitToolStripMenuItem = new ToolStripMenuItem();
         splitContainer1 = new SplitContainer();
         pictureBox1 = new PictureBox();
         statusStrip1 = new StatusStrip();
         button1 = new Button();
         timer1 = new System.Windows.Forms.Timer(components);
         menuStrip1.SuspendLayout();
         ((System.ComponentModel.ISupportInitialize)splitContainer1).BeginInit();
         splitContainer1.Panel1.SuspendLayout();
         splitContainer1.Panel2.SuspendLayout();
         splitContainer1.SuspendLayout();
         ((System.ComponentModel.ISupportInitialize)pictureBox1).BeginInit();
         SuspendLayout();
         // 
         // menuStrip1
         // 
         menuStrip1.Items.AddRange(new ToolStripItem[] { fileToolStripMenuItem });
         menuStrip1.Location = new Point(0, 0);
         menuStrip1.Name = "menuStrip1";
         menuStrip1.Size = new Size(800, 24);
         menuStrip1.TabIndex = 0;
         menuStrip1.Text = "menuStrip1";
         // 
         // fileToolStripMenuItem
         // 
         fileToolStripMenuItem.DropDownItems.AddRange(new ToolStripItem[] { exitToolStripMenuItem });
         fileToolStripMenuItem.Name = "fileToolStripMenuItem";
         fileToolStripMenuItem.Size = new Size(37, 20);
         fileToolStripMenuItem.Text = "&File";
         fileToolStripMenuItem.Click += fileToolStripMenuItem_Click;
         // 
         // exitToolStripMenuItem
         // 
         exitToolStripMenuItem.Name = "exitToolStripMenuItem";
         exitToolStripMenuItem.Size = new Size(93, 22);
         exitToolStripMenuItem.Text = "E&xit";
         exitToolStripMenuItem.Click += exitToolStripMenuItem_Click;
         // 
         // splitContainer1
         // 
         splitContainer1.Dock = DockStyle.Fill;
         splitContainer1.Location = new Point(0, 24);
         splitContainer1.Name = "splitContainer1";
         // 
         // splitContainer1.Panel1
         // 
         splitContainer1.Panel1.Controls.Add(pictureBox1);
         splitContainer1.Panel1.Controls.Add(statusStrip1);
         // 
         // splitContainer1.Panel2
         // 
         splitContainer1.Panel2.Controls.Add(button1);
         splitContainer1.Size = new Size(800, 426);
         splitContainer1.SplitterDistance = 743;
         splitContainer1.TabIndex = 1;
         // 
         // pictureBox1
         // 
         pictureBox1.Dock = DockStyle.Fill;
         pictureBox1.Location = new Point(0, 0);
         pictureBox1.Name = "pictureBox1";
         pictureBox1.Size = new Size(743, 404);
         pictureBox1.TabIndex = 1;
         pictureBox1.TabStop = false;
         // 
         // statusStrip1
         // 
         statusStrip1.Location = new Point(0, 404);
         statusStrip1.Name = "statusStrip1";
         statusStrip1.Size = new Size(743, 22);
         statusStrip1.TabIndex = 0;
         statusStrip1.Text = "statusStrip1";
         // 
         // button1
         // 
         button1.Dock = DockStyle.Top;
         button1.Location = new Point(0, 0);
         button1.Name = "button1";
         button1.Size = new Size(53, 23);
         button1.TabIndex = 0;
         button1.Text = "Start";
         button1.UseVisualStyleBackColor = true;
         button1.Click += button1_Click;
         // 
         // timer1
         // 
         timer1.Tick += timer1_Tick;
         // 
         // Form1
         // 
         AutoScaleDimensions = new SizeF(7F, 15F);
         AutoScaleMode = AutoScaleMode.Font;
         ClientSize = new Size(800, 450);
         Controls.Add(splitContainer1);
         Controls.Add(menuStrip1);
         MainMenuStrip = menuStrip1;
         Name = "Form1";
         Text = "Form1";
         menuStrip1.ResumeLayout(false);
         menuStrip1.PerformLayout();
         splitContainer1.Panel1.ResumeLayout(false);
         splitContainer1.Panel1.PerformLayout();
         splitContainer1.Panel2.ResumeLayout(false);
         ((System.ComponentModel.ISupportInitialize)splitContainer1).EndInit();
         splitContainer1.ResumeLayout(false);
         ((System.ComponentModel.ISupportInitialize)pictureBox1).EndInit();
         ResumeLayout(false);
         PerformLayout();
      }

      #endregion

      private MenuStrip menuStrip1;
      private ToolStripMenuItem fileToolStripMenuItem;
      private ToolStripMenuItem exitToolStripMenuItem;
      private SplitContainer splitContainer1;
      private PictureBox pictureBox1;
      private StatusStrip statusStrip1;
      private Button button1;
      private System.Windows.Forms.Timer timer1;
   }
}
