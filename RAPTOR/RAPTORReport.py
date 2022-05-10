import webbrowser
import RAPTORFunctions as apt

# apt.techniques_df, apt.tactics_df, apt.groups_df, apt.software_df, apt.mitigations_df, apt.gfr_df, apt.relationships_df = apt.buildDataFrames()

# This is just for dummy testing for DEBUG
groups = {'G0130':95, 'G0100':55, 'G0006':61, 'G0080':62, 'G0035':70, 'G0125':55, 'G0032':83}

DEBUG = False

# Create html report using dictionary {GroupID:Percent}
def htmlReport(groups: dict):
  # Populating Groups by % and linking to data
  nine = []
  eight = []
  seven = []
  six = []
  five = []
  for key in groups:
    # 90+% Groups
    if groups[key] >= 90:
      nine.append(key)
    # 89% - 80% Groups
    elif groups[key] >= 80 and groups[key] < 90:
      eight.append(key)
    # 79% - 70% Groups
    elif groups[key] >= 70 and groups[key] < 80:
      seven.append(key)
    # 69% - 60% Groups
    elif groups[key] >= 60 and groups[key] < 70:
      six.append(key)
    # 59% - 50% Groups
    elif groups[key] >= 50 and groups[key] < 60:
      five.append(key)

  index = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="RAPTOR.css">
    <link rel="shortcut icon" href="./images/favicon.ico" type="image/x-icon">
    <title>R.A.P.T.O.R.</title>
  </head>
  <body>
    <div class="container">
      <div class="navmenu">
        <ul>
          <li class="left"><a href="index.html"><img src="./images/raptor.png" id="logo"></a></li>
          <li></li>
          <li></li>
          <li>R.</li>
          <li>A.</li>
          <li>P.</li>
          <li>T.</li>
          <li>O.</li>
          <li>R.</li>
          <li></li>
          <li></li>
          <li class="right"><a href="about.html">[About]</a></li>
        </ul>
      </div>
      <div class="groupmenu">
        <div>"""

  # Adds the group hyperlinks to list
  index += """
          <h2>90+%</h2>"""
  for i in range(len(nine)):
    index += """
            <p><a href="{}.html">{}</a></p>""".format(nine[i], apt.getData(apt.groups_df, nine[i], 'name'))
  index += """
          <h2>80% - 89%</h2>"""
  for i in range(len(eight)):
    index += """
            <p><a href="{}.html">{}</a></p>""".format(eight[i], apt.getData(apt.groups_df, eight[i], 'name'))
  index += """
          <h2>70% - 79%</h2>"""
  for i in range(len(seven)):
    index += """
            <p><a href="{}.html">{}</a></p>""".format(seven[i], apt.getData(apt.groups_df, seven[i], 'name'))      
  index += """
          <h2>60% - 69%</h2>"""
  for i in range(len(six)):
    index += """
            <p><a href="{}.html">{}</a></p>""".format(six[i], apt.getData(apt.groups_df, six[i], 'name'))
  index += """
          <h2>50% - 59%</h2>"""
  for i in range(len(five)):
    index += """
            <p><a href="{}.html">{}</a></p>""".format(five[i], apt.getData(apt.groups_df, five[i], 'name'))
  index += """
        </div>
      </div>
      <div class="groupinfo">
        <div>
          <h1>APT Name</h1>
            <p>The description of the APT will be here.</p>
          <h2 id="spacer">Associated Groups</h2>
            <p>Known associated groups will be here.</p>
            <button id ="button1" class="collapsible">Software</button>
              <div class="content">
                <p>Software(s) known to be used by the group will be here.</p>
              </div>
            <button id ="button1" class="collapsible">Techniques</button>
              <div class="content">
                <p>Technique(s) known to be used by the group will be here.</p>
              </div>
        </div> 
      </div>
      <div class="footer">
        <ul>
          <li><a href="https://github.com/redbeardmeric/APTAnalyzer"><img src="./images/Github.png"></a></li>
          <li><a href="https://attack.mitre.org/"><img src="./images/Attck.png"></a></li>
        </ul>
      </div>
    </div>
    <script>
      var coll = document.getElementsByClassName("collapsible");
      var i;
      for (i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function(){
          this.classList.toggle("active");
          var content = this.nextElementSibling;
          if (content.style.maxHeight){
            content.style.maxHeight = null;
          } else {
            content.style.maxHeight = 1000000 + "px";
          } 
        });
      }
    </script>
  </body>
</html>"""

  with open('./HTMLFiles/index.html', 'w') as f:
    f.write(index)
    f.close()
            
  if DEBUG:        
    webbrowser.open('./HTMLFiles/index.html', new=2)

  ##### Group Pages #####
  for key in groups:
    info = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="RAPTOR.css">
    <link rel="shortcut icon" href="./images/favicon.ico" type="image/x-icon">
    <title>{}</title>""".format(apt.getData(apt.groups_df, key, 'name'))
    info += """
  </head>
  <body>
    <div class="container">
      <div class="navmenu">
        <ul>
          <li class="left"><a href="index.html"><img src="./images/raptor.png" id="logo"></a></li>
          <li></li>
          <li></li>
          <li>R.</li>
          <li>A.</li>
          <li>P.</li>
          <li>T.</li>
          <li>O.</li>
          <li>R.</li>
          <li></li>
          <li></li>
          <li class="right"><a href="about.html">[About]</a></li>
        </ul>
      </div>
      <div class="groupmenu">
        <div>"""
    # Adds the group hyperlinks to list
    info += """
          <h2>90+%</h2>"""
    for i in range(len(nine)):
      info += """
            <p><a href="{}.html">{}</a></p>""".format(nine[i], apt.getData(apt.groups_df, nine[i], 'name'))
    info += """
          <h2>80% - 89%</h2>"""
    for i in range(len(eight)):
      info += """
            <p><a href="{}.html">{}</a></p>""".format(eight[i], apt.getData(apt.groups_df, eight[i], 'name'))
    info += """
          <h2>70% - 79%</h2>"""
    for i in range(len(seven)):
      info += """
            <p><a href="{}.html">{}</a></p>""".format(seven[i], apt.getData(apt.groups_df, seven[i], 'name'))      
    info += """
          <h2>60% - 69%</h2>"""
    for i in range(len(six)):
      info += """
            <p><a href="{}.html">{}</a></p>""".format(six[i], apt.getData(apt.groups_df, six[i], 'name'))
    info += """
          <h2>50% - 59%</h2>"""
    for i in range(len(five)):
      info += """
            <p><a href="{}.html">{}</a></p>""".format(five[i], apt.getData(apt.groups_df, five[i], 'name'))

        # Populate group data
    info += """
    </div>
      </div>
      <div class="groupinfo">
        <div>
          <h1>{}</h1>""".format(apt.getData(apt.groups_df, key, 'name'))

    info += """
            <p>{}</p>""".format(apt.getData(apt.groups_df, key, 'description'))

    info += """
          <h2 id="spacer">Associated Groups</h2>
            <p>{}</p>""".format(apt.getData(apt.groups_df, key, 'associated groups'))

      # Populate software used by group
    info += """
          <button id ="button1" class="collapsible">Software</button>
            <div class="content">"""
        
    software = apt.getSoftwareByGroup(apt.relationships_df, key)
    for i in range(len(software)):
      info += """
              <button id="button2" class="collapsible">{}</button>
                <div class="content">
                  <p>{}</p>
                </div>""".format(apt.getData(apt.software_df, software[i], 'name'), apt.getData(apt.software_df, software[i], 'description'))

      # Populate techniques and how to mitigate these attacks
    info += """
            </div>
          <button id ="button1" class="collapsible">Techniques</button>
            <div class="content">"""

    techniques = apt.getTechniquesByGroup(apt.relationships_df, key)
    for i in range(len(techniques)):
      info += """
            <button id="button2" class="collapsible">{}</button>
              <div class="content">
                <p>{}</p>""".format(apt.getData(apt.techniques_df, techniques[i], 'name'), apt.getData(apt.techniques_df, techniques[i], 'description'))
      mitigations = apt.mitigationsByTechnique(apt.relationships_df, techniques[i])    
      if mitigations != []:
        info += """
                <button id="button3" class="collapsible">Mitigations</button>
                  <div class="content1">"""
        for j in range(len(mitigations)):
            info += """
                    <p>{} - {}</p>""".format(apt.getData(apt.mitigations_df, mitigations[j], 'name'), apt.getData(apt.mitigations_df, mitigations[j], 'description'))
        info += """
                  </div>
              </div>"""  
      else:
        info += """
              </div>"""

    info += """
          </div>
        </div>
      </div>
      <div class="footer">
        <ul>
          <li><a href="https://github.com/redbeardmeric/APTAnalyzer"><img src="./images/Github.png"></a></li>
          <li><a href="https://attack.mitre.org/"><img src="./images/Attck.png"></a></li>
        </ul>
      </div>
    </div>
    <script>
      var coll = document.getElementsByClassName("collapsible");
      var i;
      for (i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function(){
          this.classList.toggle("active");
          var content = this.nextElementSibling;
          if (content.style.maxHeight){
            content.style.maxHeight = null;
          } else {
            content.style.maxHeight = 1000000 + "px";
          } 
        });
      }
    </script>
  </body>
</html>"""

    file = './HTMLFiles/{}.html'.format(key)
    with open(file, 'w') as f:
      f.write(info)
      f.close()

  about = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="RAPTOR.css">
    <link rel="shortcut icon" href="./images/favicon.ico" type="image/x-icon">
    <title>R.A.P.T.O.R.</title>
  </head>
  <body>
    <div class="container">
      <div class="navmenu">
        <ul>
          <li class="left"><a href="index.html"><img src="./images/raptor.png" id="logo"></a></li>
          <li></li>
          <li></li>
          <li>R.</li>
          <li>A.</li>
          <li>P.</li>
          <li>T.</li>
          <li>O.</li>
          <li>R.</li>
          <li></li>
          <li></li>
          <li class="right"><a href="about.html">[About]</a></li>
        </ul>
      </div>
      <div class="aboutpage">
        <div>
        <ul class="aboutus">
          <li>
            <h3>James Henry</h3>
            Project Lead
          </li>
          <li>
            <h3>Jaimin Bhagat</h3>
            GUI Development
          </li>
          <li>
            <h3>Thomas Mason</h3>
            Data Development
          </li>
          <li>
            <h3>Tristan Sharpe</h3>
            HTML Development
          </li>
          <li>
            <h3>Welsley Venters</h3>
            Report Development
          </li>
        </ul>
      </div>
      <div>
        <ul class="blurb">
          <li></li>
          <li><img src="./images/dinosaur.gif"></li>
          <li>
            <h2>R.A.P.T.O.R</h2>
            <p>Ranking Advanced Persistent Threat Ontological Report</p> 
            <p>In this age of ubiquitous connectivity, with virtually every device we own or operate we are likely to become the victim of some type of cyber breach and never know the identity of the attacker.&nbsp; While databases of attackers and the methods used by them exist, they require a significant amount of navigating to narrow down the list of potential attackers.&nbsp; The aim of the R.A.P.T.O.R. is to harness these databases, initially Mitre’s Att&amp;ck, to programmatically narrow the list of potential attackers. Based upon input of techniques, sub techniques, and software, through the GUI, an HTML-based report will be generated with a list of matched attackers, the percentage match of the attacker to the user input, and mitigation recommendations, each with hyperlinks to the source information.</p>
          </li>
          <li></li>
        </ul>
      </div>
      </div>
      <div class="footer">
        <ul>
          <li><a href="https://github.com/redbeardmeric/APTAnalyzer"><img src="./images/Github.png"></a></li>
          <li><a href="https://attack.mitre.org/"><img src="./images/Attck.png"></a></li>
        </ul>
      </div>
    </div>
    <script>
      var coll = document.getElementsByClassName("collapsible");
      var i;
      for (i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function(){
          this.classList.toggle("active");
          var content = this.nextElementSibling;
          if (content.style.maxHeight){
            content.style.maxHeight = null;
          } else {
            content.style.maxHeight = 1000000 + "px";
          } 
        });
      }
    </script>
  </body>
</html>"""

  file = './HTMLFiles/about.html'
  with open(file, 'w') as f:
    f.write(about)
    f.close()

  if DEBUG:        
    webbrowser.open(file, new=2)

  ##### Opens Main Webpage #####
  #webbrowser.open('HTMLFiles/index.html', new=2)

if DEBUG:
  htmlReport(groups)
