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
    <html style="font-size: 16px;">
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta charset="utf-8">
        <meta name="keywords" content="90+%, 89% - 80%, 79% - 70%, 69% - 60%, 59% - 50%, APT Name, Description, Associated Groups, Sotware, Techniques">
        <meta name="description" content="">
        <meta name="page_type" content="np-template-header-footer-from-plugin">
        <title>Home</title>
        <link rel="stylesheet" href="nicepage.css" media="screen">
    <link rel="stylesheet" href="Home.css" media="screen">
        <script class="u-script" type="text/javascript" src="jquery.js" defer=""></script>
        <script class="u-script" type="text/javascript" src="nicepage.js" defer=""></script>
        <meta name="generator" content="Nicepage 4.8.2, nicepage.com">
        <link id="u-theme-google-font" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i|Open+Sans:300,300i,400,400i,500,500i,600,600i,700,700i,800,800i">

        <script type="application/ld+json">{
                    "@context": "http://schema.org",
                    "@type": "Organization",
                    "name": "",
                    "logo": "images/raptor.png",
                    "sameAs": [
                                    "https://github.com/redbeardmeric/APTAnalyzer",
                                    "https://attack.mitre.org/"
                    ]
    }</script>
        <meta name="theme-color" content="#478ac9">
        <meta property="og:title" content="Home">
        <meta property="og:type" content="website">
      </head>
      <body data-home-page="Home.html" data-home-page-title="Home" class="u-body u-xl-mode"><header class="u-border-3 u-border-custom-color-1 u-clearfix u-header u-header" id="sec-2f7b"><div class="u-clearfix u-sheet u-valign-middle u-sheet-1">
            <a href="https://nicepage.com" class="u-image u-logo u-image-1" data-image-width="256" data-image-height="256">
              <img src="images/raptor.png" class="u-logo-image u-logo-image-1">
            </a>
            <nav class="u-menu u-menu-dropdown u-offcanvas u-menu-1">
              <div class="menu-collapse" style="font-size: 1rem; letter-spacing: 0px;">
                <a class="u-button-style u-custom-left-right-menu-spacing u-custom-padding-bottom u-custom-text-active-color u-custom-text-color u-custom-text-hover-color u-custom-top-bottom-menu-spacing u-nav-link u-text-active-palette-1-base u-text-hover-palette-2-base" href="#">
                  <svg class="u-svg-link" viewBox="0 0 24 24"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#menu-hamburger"></use></svg>
                  <svg class="u-svg-content" version="1.1" id="menu-hamburger" viewBox="0 0 16 16" x="0px" y="0px" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg"><g><rect y="1" width="16" height="2"></rect><rect y="7" width="16" height="2"></rect><rect y="13" width="16" height="2"></rect>
    </g></svg>
                </a>
              </div>
              <div class="u-custom-menu u-nav-container">
                <ul class="u-nav u-unstyled u-nav-1"><li class="u-nav-item"><a class="u-button-style u-nav-link u-text-active-white u-text-custom-color-1 u-text-hover-white" href="Home.html" style="padding: 10px 20px;">Home</a>
    </li><li class="u-nav-item"><a class="u-button-style u-nav-link u-text-active-white u-text-custom-color-1 u-text-hover-white" href="About.html" style="padding: 10px 20px;">About</a>
    </li></ul>
              </div>
              <div class="u-custom-menu u-nav-container-collapse">
                <div class="u-black u-container-style u-inner-container-layout u-opacity u-opacity-95 u-sidenav">
                  <div class="u-inner-container-layout u-sidenav-overflow">
                    <div class="u-menu-close"></div>
                    <ul class="u-align-center u-nav u-popupmenu-items u-unstyled u-nav-2"><li class="u-nav-item"><a class="u-button-style u-nav-link" href="Home.html">Home</a>
    </li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="About.html">About</a>
    </li></ul>
                  </div>
                </div>
                <div class="u-black u-menu-overlay u-opacity u-opacity-70"></div>
              </div>
            </nav>
          </div></header>
        <section class="u-clearfix u-grey-5 u-section-1" id="sec-c48b">
          <div class="u-clearfix u-expanded-width u-layout-wrap u-layout-wrap-1">
            <div class="u-layout">
              <div class="u-layout-row">
                <div class="u-black u-container-style u-layout-cell u-size-15 u-layout-cell-1">
                  <div class="u-border-3 u-border-custom-color-1 u-container-layout u-container-layout-1">"""

    # Adds the group hyperlinks to list
    index += '''<h2 class="u-align-center u-subtitle u-text u-text-custom-color-1 u-text-1">90+%</h2>'''
    for i in range(len(nine)):
        index += '''<a href="{}.html" data-page-id="{}" class="u-border-1 u-border-active-custom-color-1 u-border-hover-custom-color-1 u-btn u-button-style u-none u-text-custom-color-1 u-btn-1">{}</a>'''.format(nine[i], nine[i], apt.getData(groups_df, nine[i], 'name'))
    index += '''<h2 class="u-align-center u-subtitle u-text u-text-custom-color-1 u-text-2">89% - 80%</h2>'''
    for i in range(len(eight)):
        index += '''<a href="{}.html" data-page-id="{}" class="u-border-1 u-border-active-custom-color-1 u-border-hover-custom-color-1 u-btn u-button-style u-none u-text-custom-color-1 u-btn-1">{}</a>'''.format(eight[i], eight[i], apt.getData(groups_df, eight[i], 'name'))
    index += '''<h2 class="u-align-center u-subtitle u-text u-text-custom-color-1 u-text-3">79% - 70%</h2>'''
    for i in range(len(seven)):
        index += '''<a href="{}.html" data-page-id="{}" class="u-border-1 u-border-active-custom-color-1 u-border-hover-custom-color-1 u-btn u-button-style u-none u-text-custom-color-1 u-btn-1">{}</a>'''.format(seven[i], seven[i], apt.getData(groups_df, seven[i], 'name'))
    index += '''<h2 class="u-align-center u-subtitle u-text u-text-custom-color-1 u-text-4">69% - 60%</h2>'''
    for i in range(len(six)):
        index += '''<a href="{}.html" data-page-id="{}" class="u-border-1 u-border-active-custom-color-1 u-border-hover-custom-color-1 u-btn u-button-style u-none u-text-custom-color-1 u-btn-1">{}</a>'''.format(six[i], six[i], apt.getData(groups_df, six[i], 'name'))
    index += '''<h2 class="u-align-center u-subtitle u-text u-text-custom-color-1 u-text-5">59% - 50%</h2>'''
    for i in range(len(five)):
        index += '''<a href="{}.html" data-page-id="{}" class="u-border-1 u-border-active-custom-color-1 u-border-hover-custom-color-1 u-btn u-button-style u-none u-text-custom-color-1 u-btn-1">{}</a>'''.format(five[i], five[i], apt.getData(groups_df, five[i], 'name'))

    index += """
                  </div>
                </div>
                <div class="u-align-center u-black u-container-style u-layout-cell u-size-45 u-layout-cell-2">
                  <div class="u-border-3 u-border-custom-color-1 u-container-layout u-container-layout-2">
                    <h1 class="u-text u-text-custom-color-1 u-title u-text-6">APT Name</h1>
                    <p class="u-text u-text-custom-color-1 u-text-default u-text-8">This will be the description of the currently selected group.</p>
                    <h2 class="u-subtitle u-text u-text-custom-color-1 u-text-default u-text-9">Associated Groups<br></h2>
                    <p class="u-text u-text-custom-color-1 u-text-default u-text-10">This will list known associates of the currently selected group.</p>
                    <h2 class="u-subtitle u-text u-text-custom-color-1 u-text-default u-text-11">Software</h2>
                    <p class="u-text u-text-custom-color-1 u-text-default u-text-12">This will list the known software used by the currently selected group.</p>
                    <h2 class="u-subtitle u-text u-text-custom-color-1 u-text-default u-text-11">Techniques</h2>
                    <p class="u-text u-text-custom-color-1 u-text-default u-text-12">This will list the techniques used by the currently selected group and how to mitigate the plausibility of these techniques</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        
        
        <footer class="u-black u-border-3 u-border-custom-color-1 u-clearfix u-footer" id="sec-be64"><div class="u-clearfix u-sheet u-sheet-1">
            <div class="u-align-left u-social-icons u-spacing-10 u-social-icons-1">
              <a class="u-social-url" target="_blank" data-type="Github" title="Github" href="https://github.com/redbeardmeric/APTAnalyzer"><span class="u-icon u-social-github u-social-icon u-icon-1"><svg class="u-svg-link" preserveAspectRatio="xMidYMin slice" viewBox="0 0 112 112" style=""><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#svg-2f65"></use></svg><svg class="u-svg-content" viewBox="0 0 112 112" x="0" y="0" id="svg-2f65"><circle fill="currentColor" cx="56.1" cy="56.1" r="55"></circle><path fill="#FFFFFF" d="M88,51.3c0-5.5-1.9-10.2-5.3-13.7c0.6-1.3,2.3-6.5-0.5-13.5c0,0-4.2-1.4-14,5.3c-4.1-1.1-8.4-1.7-12.7-1.8
            c-4.3,0-8.7,0.6-12.7,1.8c-9.7-6.6-14-5.3-14-5.3c-2.8,7-1,12.2-0.5,13.5C25,41.2,23,45.7,23,51.3c0,19.6,11.9,23.9,23.3,25.2
            c-1.5,1.3-2.8,3.5-3.2,6.8c-3,1.3-10.2,3.6-14.9-4.3c0,0-2.7-4.9-7.8-5.3c0,0-5-0.1-0.4,3.1c0,0,3.3,1.6,5.6,7.5c0,0,3,9.1,17.2,6
            c0,4.3,0.1,8.3,0.1,9.5h25.2c0-1.7,0.1-7.2,0.1-14c0-4.7-1.7-7.9-3.4-9.4C76,75.2,88,70.9,88,51.3z"></path></svg></span>
              </a>
              <a class="u-social-url" target="_blank" data-type="Github" title="MITRE Att&amp;ck" href="https://attack.mitre.org/"><span class="u-file-icon u-icon u-social-github u-social-icon u-icon-2"><img src="images/Attck.jpg" alt=""></span>
              </a>
            </div>
          </div></footer>
        <section class="u-backlink u-clearfix u-grey-80">
          <a class="u-link" href="https://nicepage.com/website-templates" target="_blank">
            <span>Website Templates</span>
          </a>
          <p class="u-text">
            <span>created with</span>
          </p>
          <a class="u-link" href="" target="_blank">
            <span>Website Builder Software</span>
          </a>. 
        </section>
      </body>
    </html>"""

    with open('HTMLFiles\Index.html', 'w') as f:
        f.write(index)
        f.close()
            
    if DEBUG:        
        webbrowser.open('HTMLFiles\Index.html', new=2)

    ##### Home/Main Page #####
    home = """
    <!DOCTYPE html>
    <html style="font-size: 16px;">
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta charset="utf-8">
        <meta name="keywords" content="90+%, 89% - 80%, 79% - 70%, 69% - 60%, 59% - 50%, APT Name, Description, Associated Groups, Software, Techniques">
        <meta name="description" content="">
        <meta name="page_type" content="np-template-header-footer-from-plugin">
        <title>Home</title>
        <link rel="stylesheet" href="nicepage.css" media="screen">
    <link rel="stylesheet" href="Home.css" media="screen">
        <script class="u-script" type="text/javascript" src="jquery.js" defer=""></script>
        <script class="u-script" type="text/javascript" src="nicepage.js" defer=""></script>
        <meta name="generator" content="Nicepage 4.8.2, nicepage.com">
        <link id="u-theme-google-font" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i|Open+Sans:300,300i,400,400i,500,500i,600,600i,700,700i,800,800i">
        
        
        <script type="application/ld+json">{
                    "@context": "http://schema.org",
                    "@type": "Organization",
                    "name": "",
                    "logo": "images/raptor.png",
                    "sameAs": [
                                    "https://github.com/redbeardmeric/APTAnalyzer",
                                    "https://attack.mitre.org/"
                    ]
    }</script>
        <meta name="theme-color" content="#478ac9">
        <meta property="og:title" content="Home">
        <meta property="og:type" content="website">
      </head>
      <body class="u-body u-xl-mode"><header class="u-border-3 u-border-custom-color-1 u-clearfix u-header u-header" id="sec-2f7b"><div class="u-clearfix u-sheet u-valign-middle u-sheet-1">
            <a href="https://nicepage.com" class="u-image u-logo u-image-1" data-image-width="256" data-image-height="256">
              <img src="images/raptor.png" class="u-logo-image u-logo-image-1">
            </a>
            <nav class="u-menu u-menu-dropdown u-offcanvas u-menu-1">
              <div class="menu-collapse" style="font-size: 1rem; letter-spacing: 0px;">
                <a class="u-button-style u-custom-left-right-menu-spacing u-custom-padding-bottom u-custom-text-active-color u-custom-text-color u-custom-text-hover-color u-custom-top-bottom-menu-spacing u-nav-link u-text-active-palette-1-base u-text-hover-palette-2-base" href="#">
                  <svg class="u-svg-link" viewBox="0 0 24 24"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#menu-hamburger"></use></svg>
                  <svg class="u-svg-content" version="1.1" id="menu-hamburger" viewBox="0 0 16 16" x="0px" y="0px" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg"><g><rect y="1" width="16" height="2"></rect><rect y="7" width="16" height="2"></rect><rect y="13" width="16" height="2"></rect>
    </g></svg>
                </a>
              </div>
              <div class="u-custom-menu u-nav-container">
                <ul class="u-nav u-unstyled u-nav-1"><li class="u-nav-item"><a class="u-button-style u-nav-link u-text-active-white u-text-custom-color-1 u-text-hover-white" href="Home.html" style="padding: 10px 20px;">Home</a>
    </li><li class="u-nav-item"><a class="u-button-style u-nav-link u-text-active-white u-text-custom-color-1 u-text-hover-white" href="About.html" style="padding: 10px 20px;">About</a>
    </li></ul>
              </div>
              <div class="u-custom-menu u-nav-container-collapse">
                <div class="u-black u-container-style u-inner-container-layout u-opacity u-opacity-95 u-sidenav">
                  <div class="u-inner-container-layout u-sidenav-overflow">
                    <div class="u-menu-close"></div>
                    <ul class="u-align-center u-nav u-popupmenu-items u-unstyled u-nav-2"><li class="u-nav-item"><a class="u-button-style u-nav-link" href="Home.html">Home</a>
    </li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="About.html">About</a>
    </li></ul>
                  </div>
                </div>
                <div class="u-black u-menu-overlay u-opacity u-opacity-70"></div>
              </div>
            </nav>
          </div></header>
        <section class="u-clearfix u-grey-5 u-section-1" id="sec-c48b">
          <div class="u-clearfix u-expanded-width u-layout-wrap u-layout-wrap-1">
            <div class="u-layout">
              <div class="u-layout-row">
                <div class="u-black u-container-style u-layout-cell u-size-15 u-layout-cell-1">
                  <div class="u-border-3 u-border-custom-color-1 u-container-layout u-container-layout-1">"""

    # Adds the group hyperlinks to list
    home += '''<h2 class="u-align-center u-subtitle u-text u-text-custom-color-1 u-text-1">90+%</h2>'''
    for i in range(len(nine)):
        home += '''<a href="{}.html" data-page-id="{}" class="u-border-1 u-border-active-custom-color-1 u-border-hover-custom-color-1 u-btn u-button-style u-none u-text-custom-color-1 u-btn-1">{}</a>'''.format(nine[i], nine[i], apt.getData(groups_df, nine[i], 'name'))
    home += '''<h2 class="u-align-center u-subtitle u-text u-text-custom-color-1 u-text-2">89% - 80%</h2>'''
    for i in range(len(eight)):
        home += '''<a href="{}.html" data-page-id="{}" class="u-border-1 u-border-active-custom-color-1 u-border-hover-custom-color-1 u-btn u-button-style u-none u-text-custom-color-1 u-btn-1">{}</a>'''.format(eight[i], eight[i], apt.getData(groups_df, eight[i], 'name'))
    home += '''<h2 class="u-align-center u-subtitle u-text u-text-custom-color-1 u-text-3">79% - 70%</h2>'''
    for i in range(len(seven)):
        home += '''<a href="{}.html" data-page-id="{}" class="u-border-1 u-border-active-custom-color-1 u-border-hover-custom-color-1 u-btn u-button-style u-none u-text-custom-color-1 u-btn-1">{}</a>'''.format(seven[i], seven[i], apt.getData(groups_df, seven[i], 'name'))
    home += '''<h2 class="u-align-center u-subtitle u-text u-text-custom-color-1 u-text-4">69% - 60%</h2>'''
    for i in range(len(six)):
        home += '''<a href="{}.html" data-page-id="{}" class="u-border-1 u-border-active-custom-color-1 u-border-hover-custom-color-1 u-btn u-button-style u-none u-text-custom-color-1 u-btn-1">{}</a>'''.format(six[i], six[i], apt.getData(groups_df, six[i], 'name'))
    home += '''<h2 class="u-align-center u-subtitle u-text u-text-custom-color-1 u-text-5">59% - 50%</h2>'''
    for i in range(len(five)):
        home += '''<a href="{}.html" data-page-id="{}" class="u-border-1 u-border-active-custom-color-1 u-border-hover-custom-color-1 u-btn u-button-style u-none u-text-custom-color-1 u-btn-1">{}</a>'''.format(five[i], five[i], apt.getData(groups_df, five[i], 'name'))

    home += """
            </div>
                </div>
                <div class="u-align-center u-black u-container-style u-layout-cell u-size-45 u-layout-cell-2">
                  <div class="u-border-3 u-border-custom-color-1 u-container-layout u-container-layout-2">
                    <h1 class="u-text u-text-custom-color-1 u-title u-text-6">APT Name - % Match</h1>
                    <h2 class="u-subtitle u-text u-text-custom-color-1 u-text-default u-text-7">Description</h2>
                    <p class="u-text u-text-custom-color-1 u-text-default u-text-8">The description will describe the current group selected</p>
                    <h2 class="u-subtitle u-text u-text-custom-color-1 u-text-default u-text-9">Associated Groups<br>
                    </h2>
                    <p class="u-text u-text-custom-color-1 u-text-default u-text-10">Associated groups are groups the currentlyselected group works with</p>
                    <h2 class="u-subtitle u-text u-text-custom-color-1 u-text-default u-text-11">Tactics/Techniques</h2>
                    <p class="u-text u-text-custom-color-1 u-text-default u-text-12">Here are the techniques the selected group has been known to use</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        
        
        <footer class="u-black u-border-3 u-border-custom-color-1 u-clearfix u-footer" id="sec-be64"><div class="u-clearfix u-sheet u-sheet-1">
            <div class="u-align-left u-social-icons u-spacing-10 u-social-icons-1">
              <a class="u-social-url" target="_blank" data-type="Github" title="Github" href="https://github.com/redbeardmeric/APTAnalyzer"><span class="u-icon u-social-github u-social-icon u-icon-1"><svg class="u-svg-link" preserveAspectRatio="xMidYMin slice" viewBox="0 0 112 112" style=""><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#svg-2f65"></use></svg><svg class="u-svg-content" viewBox="0 0 112 112" x="0" y="0" id="svg-2f65"><circle fill="currentColor" cx="56.1" cy="56.1" r="55"></circle><path fill="#FFFFFF" d="M88,51.3c0-5.5-1.9-10.2-5.3-13.7c0.6-1.3,2.3-6.5-0.5-13.5c0,0-4.2-1.4-14,5.3c-4.1-1.1-8.4-1.7-12.7-1.8
            c-4.3,0-8.7,0.6-12.7,1.8c-9.7-6.6-14-5.3-14-5.3c-2.8,7-1,12.2-0.5,13.5C25,41.2,23,45.7,23,51.3c0,19.6,11.9,23.9,23.3,25.2
            c-1.5,1.3-2.8,3.5-3.2,6.8c-3,1.3-10.2,3.6-14.9-4.3c0,0-2.7-4.9-7.8-5.3c0,0-5-0.1-0.4,3.1c0,0,3.3,1.6,5.6,7.5c0,0,3,9.1,17.2,6
            c0,4.3,0.1,8.3,0.1,9.5h25.2c0-1.7,0.1-7.2,0.1-14c0-4.7-1.7-7.9-3.4-9.4C76,75.2,88,70.9,88,51.3z"></path></svg></span>
              </a>
              <a class="u-social-url" target="_blank" data-type="Github" title="MITRE Att&amp;ck" href="https://attack.mitre.org/"><span class="u-file-icon u-icon u-social-github u-social-icon u-icon-2"><img src="images/Attck.jpg" alt=""></span>
              </a>
            </div>
          </div></footer>
        <section class="u-backlink u-clearfix u-grey-80">
          <a class="u-link" href="https://nicepage.com/website-templates" target="_blank">
            <span>Website Templates</span>
          </a>
          <p class="u-text">
            <span>created with</span>
          </p>
          <a class="u-link" href="" target="_blank">
            <span>Website Builder Software</span>
          </a>. 
        </section>
      </body>
    </html>"""

    with open('HTMLFiles\Home.html', 'w') as f:
        f.write(index)
        f.close()

    if DEBUG:  
        webbrowser.open('HTMLFiles\Home.html', new=2)

    ##### About Page #####
    about = """<!DOCTYPE html>
    <html style="font-size: 16px;">
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta charset="utf-8">
        <meta name="keywords" content="R.A.P.T.O.R">
        <meta name="description" content="">
        <meta name="page_type" content="np-template-header-footer-from-plugin">
        <title>About</title>
        <link rel="stylesheet" href="nicepage.css" media="screen">
    <link rel="stylesheet" href="About.css" media="screen">
        <script class="u-script" type="text/javascript" src="jquery.js" defer=""></script>
        <script class="u-script" type="text/javascript" src="nicepage.js" defer=""></script>
        <meta name="generator" content="Nicepage 4.8.2, nicepage.com">
        <link id="u-theme-google-font" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i|Open+Sans:300,300i,400,400i,500,500i,600,600i,700,700i,800,800i">
        
        
        
        <script type="application/ld+json">{
                    "@context": "http://schema.org",
                    "@type": "Organization",
                    "name": "",
                    "logo": "images/raptor.png",
                    "sameAs": [
                                    "https://github.com/redbeardmeric/APTAnalyzer",
                                    "https://attack.mitre.org/"
                    ]
    }</script>
        <meta name="theme-color" content="#478ac9">
        <meta property="og:title" content="About">
        <meta property="og:type" content="website">
      </head>
      <body class="u-body u-xl-mode"><header class="u-border-3 u-border-custom-color-1 u-clearfix u-header u-header" id="sec-2f7b"><div class="u-clearfix u-sheet u-valign-middle u-sheet-1">
            <a href="https://nicepage.com" class="u-image u-logo u-image-1" data-image-width="256" data-image-height="256">
              <img src="images/raptor.png" class="u-logo-image u-logo-image-1">
            </a>
            <nav class="u-menu u-menu-dropdown u-offcanvas u-menu-1">
              <div class="menu-collapse" style="font-size: 1rem; letter-spacing: 0px;">
                <a class="u-button-style u-custom-left-right-menu-spacing u-custom-padding-bottom u-custom-text-active-color u-custom-text-color u-custom-text-hover-color u-custom-top-bottom-menu-spacing u-nav-link u-text-active-palette-1-base u-text-hover-palette-2-base" href="#">
                  <svg class="u-svg-link" viewBox="0 0 24 24"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#menu-hamburger"></use></svg>
                  <svg class="u-svg-content" version="1.1" id="menu-hamburger" viewBox="0 0 16 16" x="0px" y="0px" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg"><g><rect y="1" width="16" height="2"></rect><rect y="7" width="16" height="2"></rect><rect y="13" width="16" height="2"></rect>
    </g></svg>
                </a>
              </div>
              <div class="u-custom-menu u-nav-container">
                <ul class="u-nav u-unstyled u-nav-1"><li class="u-nav-item"><a class="u-button-style u-nav-link u-text-active-white u-text-custom-color-1 u-text-hover-white" href="Home.html" style="padding: 10px 20px;">Home</a>
    </li><li class="u-nav-item"><a class="u-button-style u-nav-link u-text-active-white u-text-custom-color-1 u-text-hover-white" href="About.html" style="padding: 10px 20px;">About</a>
    </li></ul>
              </div>
              <div class="u-custom-menu u-nav-container-collapse">
                <div class="u-black u-container-style u-inner-container-layout u-opacity u-opacity-95 u-sidenav">
                  <div class="u-inner-container-layout u-sidenav-overflow">
                    <div class="u-menu-close"></div>
                    <ul class="u-align-center u-nav u-popupmenu-items u-unstyled u-nav-2"><li class="u-nav-item"><a class="u-button-style u-nav-link" href="Home.html">Home</a>
    </li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="About.html">About</a>
    </li></ul>
                  </div>
                </div>
                <div class="u-black u-menu-overlay u-opacity u-opacity-70"></div>
              </div>
            </nav>
          </div></header>
        <section class="u-align-center u-clearfix u-section-1" id="sec-96c2">
          <div class="u-clearfix u-sheet u-valign-middle u-sheet-1">
            <div class="u-expanded-width u-list u-list-1">
              <div class="u-repeater u-repeater-1">
                <div class="u-align-center u-container-style u-list-item u-repeater-item">
                  <div class="u-container-layout u-similar-container u-valign-top u-container-layout-1">
                    <div alt="" class="u-image u-image-circle u-image-1" src="" data-image-width="500" data-image-height="500"></div>
                    <h5 class="u-text u-text-custom-color-1 u-text-1">James Henry</h5>
                    <p class="u-text u-text-custom-color-1 u-text-2">Manager</p>
                  </div>
                </div>
                <div class="u-align-center u-container-style u-list-item u-repeater-item">
                  <div class="u-container-layout u-similar-container u-valign-top u-container-layout-2">
                    <div alt="" class="u-image u-image-circle u-image-2" src="" data-image-width="500" data-image-height="500"></div>
                    <h5 class="u-text u-text-custom-color-1 u-text-3">Tristan Sharpe</h5>
                    <p class="u-text u-text-custom-color-1 u-text-4">Developer</p>
                  </div>
                </div>
                <div class="u-align-center u-container-style u-list-item u-repeater-item">
                  <div class="u-container-layout u-similar-container u-valign-top u-container-layout-3">
                    <div alt="" class="u-image u-image-circle u-image-3" src="" data-image-width="500" data-image-height="500"></div>
                    <h5 class="u-text u-text-custom-color-1 u-text-5">Wesley Venters</h5>
                    <p class="u-text u-text-custom-color-1 u-text-6">Developer</p>
                  </div>
                </div>
                <div class="u-align-center u-container-style u-list-item u-repeater-item">
                  <div class="u-container-layout u-similar-container u-valign-top u-container-layout-4">
                    <div alt="" class="u-image u-image-circle u-image-4" src="" data-image-width="500" data-image-height="500"></div>
                    <h5 class="u-text u-text-custom-color-1 u-text-7">Jaimin Bhagat</h5>
                    <p class="u-text u-text-custom-color-1 u-text-8">Developer</p>
                  </div>
                </div>
                <div class="u-align-center u-container-style u-list-item u-repeater-item">
                  <div class="u-container-layout u-similar-container u-valign-top u-container-layout-5">
                    <div alt="" class="u-image u-image-circle u-image-5" src="" data-image-width="500" data-image-height="500"></div>
                    <h5 class="u-text u-text-custom-color-1 u-text-9">Thomas Mason</h5>
                    <p class="u-text u-text-custom-color-1 u-text-10">Developer</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        <section class="u-clearfix u-section-2" id="sec-9e94">
          <div class="u-clearfix u-sheet u-sheet-1">
            <div class="u-clearfix u-expanded-width u-gutter-0 u-layout-wrap u-layout-wrap-1">
              <div class="u-layout">
                <div class="u-layout-row">
                  <div class="u-align-center u-container-style u-layout-cell u-left-cell u-size-23 u-layout-cell-1">
                    <div class="u-container-layout u-valign-middle u-container-layout-1">
                      <img class="u-image u-image-round u-radius-10 u-image-1" src="images/dinosaur.gif" data-image-width="260" data-image-height="269">
                    </div>
                  </div>
                  <div class="u-align-left u-container-style u-layout-cell u-right-cell u-size-37 u-layout-cell-2">
                    <div class="u-container-layout u-valign-top-xs u-container-layout-2">
                      <h2 class="u-text u-text-custom-color-1 u-text-default u-text-1">R.A.P.T.O.R</h2>
                      <p class="u-text u-text-custom-color-1 u-text-2"> Ranking Advanced Persistent Threat Ontological Report<br>
                        <br><b>
                          <span style="font-weight: 400;">In this age of ubiquitous connectivity, with virtually every device we own or operate we are likely to become the victim of some type of cyber breach and never know the identity of the attacker.&nbsp; While databases of attackers and the methods used by them exist, they require a significant amount of navigating to narrow down the list of potential attackers.&nbsp; The aim of the R.A.P.T.O.R. is to harness these databases, initially Mitre’s Att&amp;ck, to programmatically narrow the list of potential attackers.&nbsp; Based upon input of techniques, sub techniques, and software, through the GUI, an HTML-based report will be generated with a list of matched attackers, the percentage match of the attacker to the user input, and mitigation recommendations, each with hyperlinks to the source information.</span>&nbsp;</b>
                        <br>
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        
        
        <footer class="u-black u-border-3 u-border-custom-color-1 u-clearfix u-footer" id="sec-be64"><div class="u-clearfix u-sheet u-sheet-1">
            <div class="u-align-left u-social-icons u-spacing-10 u-social-icons-1">
              <a class="u-social-url" target="_blank" data-type="Github" title="Github" href="https://github.com/redbeardmeric/APTAnalyzer"><span class="u-icon u-social-github u-social-icon u-icon-1"><svg class="u-svg-link" preserveAspectRatio="xMidYMin slice" viewBox="0 0 112 112" style=""><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#svg-2f65"></use></svg><svg class="u-svg-content" viewBox="0 0 112 112" x="0" y="0" id="svg-2f65"><circle fill="currentColor" cx="56.1" cy="56.1" r="55"></circle><path fill="#FFFFFF" d="M88,51.3c0-5.5-1.9-10.2-5.3-13.7c0.6-1.3,2.3-6.5-0.5-13.5c0,0-4.2-1.4-14,5.3c-4.1-1.1-8.4-1.7-12.7-1.8
            c-4.3,0-8.7,0.6-12.7,1.8c-9.7-6.6-14-5.3-14-5.3c-2.8,7-1,12.2-0.5,13.5C25,41.2,23,45.7,23,51.3c0,19.6,11.9,23.9,23.3,25.2
            c-1.5,1.3-2.8,3.5-3.2,6.8c-3,1.3-10.2,3.6-14.9-4.3c0,0-2.7-4.9-7.8-5.3c0,0-5-0.1-0.4,3.1c0,0,3.3,1.6,5.6,7.5c0,0,3,9.1,17.2,6
            c0,4.3,0.1,8.3,0.1,9.5h25.2c0-1.7,0.1-7.2,0.1-14c0-4.7-1.7-7.9-3.4-9.4C76,75.2,88,70.9,88,51.3z"></path></svg></span>
              </a>
              <a class="u-social-url" target="_blank" data-type="Github" title="MITRE Att&amp;ck" href="https://attack.mitre.org/"><span class="u-file-icon u-icon u-social-github u-social-icon u-icon-2"><img src="images/Attck.jpg" alt=""></span>
              </a>
            </div>
          </div></footer>
        <section class="u-backlink u-clearfix u-grey-80">
          <a class="u-link" href="https://nicepage.com/website-templates" target="_blank">
            <span>Website Templates</span>
          </a>
          <p class="u-text">
            <span>created with</span>
          </p>
          <a class="u-link" href="" target="_blank">
            <span>Website Builder Software</span>
          </a>. 
        </section>
      </body>
    </html>"""

    with open('HTMLFiles\About.html', 'w') as f:
        f.write(about)
        f.close()
            
    if DEBUG:        
        webbrowser.open('HTMLFiles\About.html', new=2)

    ##### Group Pages #####
    for key in groups:
        info = """
        <!DOCTYPE html>
        <html style="font-size: 16px;">
          <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta charset="utf-8">
            <meta name="keywords" content="90+%, 89% - 80%, 79% - 70%, 69% - 60%, 59% - 50%, APT Name, Description, Associated Groups, Software, Techniques">
            <meta name="description" content="">
            <meta name="page_type" content="np-template-header-footer-from-plugin">"""

        info += "<title>{}</title>".format(key)
        
        info += """
            <link rel="stylesheet" href="nicepage.css" media="screen">
        <link rel="stylesheet" href="groupPage.css" media="screen">
            <script class="u-script" type="text/javascript" src="jquery.js" defer=""></script>
            <script class="u-script" type="text/javascript" src="nicepage.js" defer=""></script>
            <meta name="generator" content="Nicepage 4.8.2, nicepage.com">
            <link id="u-theme-google-font" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i|Open+Sans:300,300i,400,400i,500,500i,600,600i,700,700i,800,800i">
            
            
            <script type="application/ld+json">{
                        "@context": "http://schema.org",
                        "@type": "Organization",
                        "name": "",
                        "logo": "images/raptor.png",
                        "sameAs": [
                                        "https://github.com/redbeardmeric/APTAnalyzer",
                                        "https://attack.mitre.org/"
                        ]
        }</script>
            <meta name="theme-color" content="#478ac9">"""

        info += """<meta property="og:title" content="{}">""".format(key)

        info += """
            <meta property="og:type" content="website">
          </head>
          <body class="u-body u-xl-mode"><header class="u-border-3 u-border-custom-color-1 u-clearfix u-header u-header" id="sec-2f7b"><div class="u-clearfix u-sheet u-valign-middle u-sheet-1">
                <a href="https://nicepage.com" class="u-image u-logo u-image-1" data-image-width="256" data-image-height="256">
                  <img src="images/raptor.png" class="u-logo-image u-logo-image-1">
                </a>
                <nav class="u-menu u-menu-dropdown u-offcanvas u-menu-1">
                  <div class="menu-collapse" style="font-size: 1rem; letter-spacing: 0px;">
                    <a class="u-button-style u-custom-left-right-menu-spacing u-custom-padding-bottom u-custom-text-active-color u-custom-text-color u-custom-text-hover-color u-custom-top-bottom-menu-spacing u-nav-link u-text-active-palette-1-base u-text-hover-palette-2-base" href="#">
                      <svg class="u-svg-link" viewBox="0 0 24 24"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#menu-hamburger"></use></svg>
                      <svg class="u-svg-content" version="1.1" id="menu-hamburger" viewBox="0 0 16 16" x="0px" y="0px" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg"><g><rect y="1" width="16" height="2"></rect><rect y="7" width="16" height="2"></rect><rect y="13" width="16" height="2"></rect>
        </g></svg>
                    </a>
                  </div>
                  <div class="u-custom-menu u-nav-container">
                    <ul class="u-nav u-unstyled u-nav-1"><li class="u-nav-item"><a class="u-button-style u-nav-link u-text-active-white u-text-custom-color-1 u-text-hover-white" href="Home.html" style="padding: 10px 20px;">Home</a>
        </li><li class="u-nav-item"><a class="u-button-style u-nav-link u-text-active-white u-text-custom-color-1 u-text-hover-white" href="About.html" style="padding: 10px 20px;">About</a>
        </li></ul>
                  </div>
                  <div class="u-custom-menu u-nav-container-collapse">
                    <div class="u-black u-container-style u-inner-container-layout u-opacity u-opacity-95 u-sidenav">
                      <div class="u-inner-container-layout u-sidenav-overflow">
                        <div class="u-menu-close"></div>
                        <ul class="u-align-center u-nav u-popupmenu-items u-unstyled u-nav-2"><li class="u-nav-item"><a class="u-button-style u-nav-link" href="Home.html">Home</a>
        </li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="About.html">About</a>
        </li></ul>
                      </div>
                    </div>
                    <div class="u-black u-menu-overlay u-opacity u-opacity-70"></div>
                  </div>
                </nav>
              </div></header>
            <section class="u-align-center u-clearfix u-grey-5 u-section-1" id="sec-c48b">
              <div class="u-clearfix u-expanded-width u-layout-wrap u-layout-wrap-1">
                <div class="u-layout">
                  <div class="u-layout-row">
                    <div class="u-black u-container-style u-layout-cell u-size-15 u-layout-cell-1">
                      <div class="u-border-3 u-border-custom-color-1 u-container-layout u-container-layout-1">"""

        # Adds the group hyperlinks to list
        info += '''<h2 class="u-align-center u-subtitle u-text u-text-custom-color-1 u-text-1">90+%</h2>'''
        for i in range(len(nine)):
            info += '''<a href="{}.html" data-page-id="{}" class="u-border-1 u-border-active-custom-color-1 u-border-hover-custom-color-1 u-btn u-button-style u-none u-text-custom-color-1 u-btn-1">{}</a>'''.format(nine[i], nine[i], apt.getData(groups_df, nine[i], 'name'))
        info += '''<h2 class="u-align-center u-subtitle u-text u-text-custom-color-1 u-text-2">89% - 80%</h2>'''
        for i in range(len(eight)):
            info += '''<a href="{}.html" data-page-id="{}" class="u-border-1 u-border-active-custom-color-1 u-border-hover-custom-color-1 u-btn u-button-style u-none u-text-custom-color-1 u-btn-1">{}</a>'''.format(eight[i], eight[i], apt.getData(groups_df, eight[i], 'name'))
        info += '''<h2 class="u-align-center u-subtitle u-text u-text-custom-color-1 u-text-3">79% - 70%</h2>'''
        for i in range(len(seven)):
            info += '''<a href="{}.html" data-page-id="{}" class="u-border-1 u-border-active-custom-color-1 u-border-hover-custom-color-1 u-btn u-button-style u-none u-text-custom-color-1 u-btn-1">{}</a>'''.format(seven[i], seven[i], apt.getData(groups_df, seven[i], 'name'))
        info += '''<h2 class="u-align-center u-subtitle u-text u-text-custom-color-1 u-text-4">69% - 60%</h2>'''
        for i in range(len(six)):
            info += '''<a href="{}.html" data-page-id="{}" class="u-border-1 u-border-active-custom-color-1 u-border-hover-custom-color-1 u-btn u-button-style u-none u-text-custom-color-1 u-btn-1">{}</a>'''.format(six[i], six[i], apt.getData(groups_df, six[i], 'name'))
        info += '''<h2 class="u-align-center u-subtitle u-text u-text-custom-color-1 u-text-5">59% - 50%</h2>'''
        for i in range(len(five)):
            info += '''<a href="{}.html" data-page-id="{}" class="u-border-1 u-border-active-custom-color-1 u-border-hover-custom-color-1 u-btn u-button-style u-none u-text-custom-color-1 u-btn-1">{}</a>'''.format(five[i], five[i], apt.getData(groups_df, five[i], 'name'))

        # Populate group data
        info += """
                      </div>
                    </div>
                    <div class="u-black u-container-style u-layout-cell u-size-45 u-layout-cell-2">
                      <div class="u-border-3 u-border-custom-color-1 u-container-layout u-container-layout-2">"""

        info += """
                        <h1 class="u-align-left u-text u-text-custom-color-1 u-title u-text-6">{}</h1>""".format(apt.getData(groups_df, key, 'name'))

        info += """
                        <p class="u-align-left u-text u-text-custom-color-1 u-text-default u-text-8">{}</p>""".format(apt.getData(groups_df, key, 'description'))

        info += """
                        <h2 class="u-align-left u-subtitle u-text u-text-custom-color-1 u-text-default u-text-9">Associated Groups</h2>
                        <p class="u-align-left u-text u-text-custom-color-1 u-text-default u-text-10">{}</p>""".format(apt.getData(groups_df, key, 'associated groups'))

        # Populate software used by group
        info += """
                         <details>
                             <summary><h2 class="u-align-left u-subtitle u-text u-text-custom-color-1 u-text-default u-text-9">Software</h2></summary>"""
        
        software = apt.getSofwareByGroup(relationships_df, key)
        for i in range(len(software)):
            info += """
                        <details>
                            <summary class="u-align-left u-text u-text-custom-color-1 u-text-9 style="padding-left: 15px;"><span style="padding-left: 20px; display:block">{}</span></summary>
                            <p><span style="padding-left: 40px; display:block">{}</span></p>
                        </details>""".format(apt.getData(software_df, software[i], 'name'), apt.getData(software_df, software[i], 'description'))

        # Populate techniques and how to mitigate these attacks
        info += """</details>
                   <details>
                     <summary><h2 class="u-align-left u-subtitle u-text u-text-custom-color-1 u-text-default u-text-9">Techniques</h2></summary>"""

        techniques = apt.getTechniquesByGroup(relationships_df, key)
        for i in range(len(techniques)):
            info += """
                        <details>
                            <summary class="u-align-left u-text u-text-custom-color-1 u-text-9"><h5 class="u-align-left u-text u-text-custom-color-1 u-text-default u-text-9"><span style="padding-left: 20px; display:block">{}</span></h5></summary>
                            <p><span style="padding-left: 40px; display:block">{}</span></p>""".format(apt.getData(techniques_df, techniques[i], 'name'), apt.getData(techniques_df, techniques[i], 'description'))
            
            mitigations = apt.mitigationsByTechnique(relationships_df, techniques[i])
            if mitigations != []:
                info += """
                    <details>
                        <summary><h6 class="u-align-left u-text u-text-custom-color-1 u-text-default u-text-9"><span style="padding-left: 60px; display:block">Mitigations</span></h6></summary>"""
                for j in range(len(mitigations)):
                    info += """
                            <p><span style="padding-left: 80px; display:block">{} - {}</span></p>""".format(apt.getData(mitigations_df, mitigations[j], 'name'), apt.getData(mitigations_df, mitigations[j], 'description'))
                info += """</details>
                        </details>"""
            else:
                info += """</details>"""

        info += """
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </section>
            
            
            <footer class="u-black u-border-3 u-border-custom-color-1 u-clearfix u-footer" id="sec-be64"><div class="u-clearfix u-sheet u-sheet-1">
                <div class="u-align-left u-social-icons u-spacing-10 u-social-icons-1">
                  <a class="u-social-url" target="_blank" data-type="Github" title="Github" href="https://github.com/redbeardmeric/APTAnalyzer"><span class="u-icon u-social-github u-social-icon u-icon-1"><svg class="u-svg-link" preserveAspectRatio="xMidYMin slice" viewBox="0 0 112 112" style=""><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#svg-2f65"></use></svg><svg class="u-svg-content" viewBox="0 0 112 112" x="0" y="0" id="svg-2f65"><circle fill="currentColor" cx="56.1" cy="56.1" r="55"></circle><path fill="#FFFFFF" d="M88,51.3c0-5.5-1.9-10.2-5.3-13.7c0.6-1.3,2.3-6.5-0.5-13.5c0,0-4.2-1.4-14,5.3c-4.1-1.1-8.4-1.7-12.7-1.8
                c-4.3,0-8.7,0.6-12.7,1.8c-9.7-6.6-14-5.3-14-5.3c-2.8,7-1,12.2-0.5,13.5C25,41.2,23,45.7,23,51.3c0,19.6,11.9,23.9,23.3,25.2
                c-1.5,1.3-2.8,3.5-3.2,6.8c-3,1.3-10.2,3.6-14.9-4.3c0,0-2.7-4.9-7.8-5.3c0,0-5-0.1-0.4,3.1c0,0,3.3,1.6,5.6,7.5c0,0,3,9.1,17.2,6
                c0,4.3,0.1,8.3,0.1,9.5h25.2c0-1.7,0.1-7.2,0.1-14c0-4.7-1.7-7.9-3.4-9.4C76,75.2,88,70.9,88,51.3z"></path></svg></span>
                  </a>
                  <a class="u-social-url" target="_blank" data-type="Github" title="MITRE Att&amp;ck" href="https://attack.mitre.org/"><span class="u-file-icon u-icon u-social-github u-social-icon u-icon-2"><img src="images/Attck.jpg" alt=""></span>
                  </a>
                </div>
              </div></footer>
            <section class="u-backlink u-clearfix u-grey-80">
              <a class="u-link" href="https://nicepage.com/templates" target="_blank">
                <span>Template</span>
              </a>
              <p class="u-text">
                <span>created with</span>
              </p>
              <a class="u-link" href="https://nicepage.com/html-website-builder" target="_blank">
                <span>HTML Website Builder</span>
              </a>. 
            </section>
          </body>
        </html>"""

        file = 'HTMLFiles\{}.html'.format(key)
        with open(file, 'w') as f:
                f.write(info)
                f.close()

        if DEBUG:        
            webbrowser.open(file, new=2)

    ##### Opens Main Webpage #####
    webbrowser.open('HTMLFiles\Index.html', new=2)

if DEBUG:
    htmlReport(groups)
