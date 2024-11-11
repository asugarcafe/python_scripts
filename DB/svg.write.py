# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:01:03 2024

@author: BeRoberts
"""

#import svgwrite


locs = ['ADMIN', 'Alta', 'ARCH', 'BCR', 
'CCL', 'CUST', 'DBK', 'DRA', 'FAC', 
'GRA', 'HER', 'HOL', 'HUN', 'IT', 'KEA', 
'MAG', 'MCC', 'METRO', 'OXBO', 'RIV', 
'SAN', 'SJO', 'SLC_ARC', 'SLCLS', 'SLCOS', 
'SMC', 'SMI', 'TAY', 'TRA', 'TSV', 'TYL', 
'VEC', 'VIR', 'web', 'WHI', 'WJO', 'WVA']

#Hex	RGB
#373854	(55,56,84) -BLack Purple
#493267	(73,50,103) -Deep Purple
#9e379f	(158,55,159) - Grape Skittles
#e86af0	(232,106,240) - Lilac?
#7bb3ff	(123,179,255) - Inversion


cont = '''
<svg width="180" height="200" xmlns="http://www.w3.org/2000/svg">
  <style>
    .glyph {
      color: white;
      fill: white;
      font: italic 72px sans-serif;
      
    }
    .bg {
      color: white;
      fill: white;
    }
    .black_purple{
      color: #373854;
      fill: #373854;
      font-size:58pt;
    }
    .deep_purple{
      color: #493267;
      fill: #493267;
    }
    .skittles_purple{
      color: #9e379f;
      fill: #9e379f;
    }
    .lilac_purple{
      color: #e86af0;
      fill: #e86af0;
    }
    .inversion_blue{
      color: #7bb3ff;
      fill: #7bb3ff;
      font-size:68pt;
    }
    .glyph_text{
    }


  </style>
  <rect width="180" height="200" x="0" y="0" class="black_purple" />
  <rect width="175" height="195" x="2" y="2" class="skittles_purple" />
  <rect width="180" height="50" x="112" y="0" class="black_purple" />
  <text x="9" y="140" class="black_purple">#{REP}</text>
</svg>'''

folder = 'C:/temp/data/svg/'
for loc in locs:
    with open(folder + loc + ".svg", "w") as f:
        f.write(cont.replace('#{REP}',loc))
        f.close()
