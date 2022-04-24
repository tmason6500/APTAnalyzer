import webbrowser
import RAPTORFunctions as apt

techniques_df, tactics_df, groups_df, software_df, mitigations_df, gfr_df, relationships_df = apt.buildDataFrames()

# This is just for dummy testing for DEBUG
groups = {'G0130':95, 'G0100':55, 'G0006':61, 'G0080':62, 'G0035':70, 'G0125':55, 'G0032':83}

DEBUG = True

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
          <li><a href="index.html">Print All</a></li>
          <li><a href="about.html">About</a></li>
          <li class="left"><a href="index.html"><img src="./images/raptor.png" id="logo"></a></li>
        </ul>
      </div>
      <div class="groupmenu">
        <div>"""

  # Adds the group hyperlinks to list
  index += """
          <h2>90+%</h2>"""
  for i in range(len(nine)):
    index += """
            <p><a href="{}.html">{}</a></p>""".format(nine[i], apt.getData(groups_df, nine[i], 'name'))
  index += """
          <h2>80% - 89%</h2>"""
  for i in range(len(eight)):
    index += """
            <p><a href="{}.html">{}</a></p>""".format(eight[i], apt.getData(groups_df, eight[i], 'name'))
  index += """
          <h2>70% - 79%</h2>"""
  for i in range(len(seven)):
    index += """
            <p><a href="{}.html">{}</a></p>""".format(seven[i], apt.getData(groups_df, seven[i], 'name'))      
  index += """
          <h2>60% - 69%</h2>"""
  for i in range(len(six)):
    index += """
            <p><a href="{}.html">{}</a></p>""".format(six[i], apt.getData(groups_df, six[i], 'name'))
  index += """
          <h2>50% - 59%</h2>"""
  for i in range(len(five)):
    index += """
            <p><a href="{}.html">{}</a></p>""".format(five[i], apt.getData(groups_df, five[i], 'name'))
  index += """
        </div>
      </div>
      <div class="groupinfo">
        <div>
          <h1>APT Name</h1>
            <p>The descrition of the APT will be here.</p>
          <h2>Associated Groups</h2>
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
    <title>{}</title>""".format(apt.getData(groups_df, key, 'name'))
    info += """
  </head>
  <body>
    <div class="container">
      <div class="navmenu">
        <ul>
          <li><a href="index.html">Print All</a></li>
          <li><a href="about.html">About</a></li>
          <li class="left"><a href="index.html"><img src="./images/raptor.png" id="logo"></a></li>
        </ul>
      </div>
      <div class="groupmenu">
        <div>"""
    # Adds the group hyperlinks to list
    info += """
          <h2>90+%</h2>"""
    for i in range(len(nine)):
      info += """
            <p><a href="{}.html">{}</a></p>""".format(nine[i], apt.getData(groups_df, nine[i], 'name'))
    info += """
          <h2>80% - 89%</h2>"""
    for i in range(len(eight)):
      info += """
            <p><a href="{}.html">{}</a></p>""".format(eight[i], apt.getData(groups_df, eight[i], 'name'))
    info += """
          <h2>70% - 79%</h2>"""
    for i in range(len(seven)):
      info += """
            <p><a href="{}.html">{}</a></p>""".format(seven[i], apt.getData(groups_df, seven[i], 'name'))      
    info += """
          <h2>60% - 69%</h2>"""
    for i in range(len(six)):
      info += """
            <p><a href="{}.html">{}</a></p>""".format(six[i], apt.getData(groups_df, six[i], 'name'))
    info += """
          <h2>50% - 59%</h2>"""
    for i in range(len(five)):
      info += """
            <p><a href="{}.html">{}</a></p>""".format(five[i], apt.getData(groups_df, five[i], 'name'))

        # Populate group data
    info += """
    </div>
      </div>
      <div class="groupinfo">
        <div>
          <h1>{}</h1>""".format(apt.getData(groups_df, key, 'name'))

    info += """
            <p>{}</p>""".format(apt.getData(groups_df, key, 'description'))

    info += """
          <h2>Associated Groups</h2>
            <p>{}</p>""".format(apt.getData(groups_df, key, 'associated groups'))

      # Populate software used by group
    info += """
          <button id ="button1" class="collapsible">Software</button>
            <div class="content">"""
        
    software = apt.getSofwareByGroup(relationships_df, key)
    for i in range(len(software)):
      info += """
              <button id="button2" class="collapsible">{}</button>
                <div class="content">
                  <p>{}</p>
                </div>""".format(apt.getData(software_df, software[i], 'name'), apt.getData(software_df, software[i], 'description'))

      # Populate techniques and how to mitigate these attacks
    info += """
            </div>
          <button id ="button1" class="collapsible">Techniques</button>
            <div class="content">"""

    techniques = apt.getTechniquesByGroup(relationships_df, key)
    for i in range(len(techniques)):
      info += """
            <button id="button2" class="collapsible">{}</button>
              <div class="content">
                <p>{}</p>""".format(apt.getData(techniques_df, techniques[i], 'name'), apt.getData(techniques_df, techniques[i], 'description'))
      mitigations = apt.mitigationsByTechnique(relationships_df, techniques[i])    
      if mitigations != []:
        info += """
                <button id="button3" class="collapsible">Mitigations</button>
                  <div class="content">"""
        for j in range(len(mitigations)):
            info += """
                    <p>{} - {}</p>""".format(apt.getData(mitigations_df, mitigations[j], 'name'), apt.getData(mitigations_df, mitigations[j], 'description'))
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

    if DEBUG:        
      webbrowser.open(file, new=2)

      ##### Opens Main Webpage #####
    webbrowser.open('HTMLFiles/Index.html', new=2)

if DEBUG:
  htmlReport(groups)