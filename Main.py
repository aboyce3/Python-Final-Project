import os, re, zipfile, shutil, smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Language:
    def __init__(self, type, count, wordList,location):
        self.type = type
        self.count = count
        self.wordList = wordList
        self.location = location


def parser():
    listOfProjects = list()
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            fileLocation = os.getcwd() + os.path.join(root,name)[1:]
            listOfProjects.append(parse(fileLocation,name))
    return listOfProjects


def parse(location,name):
    listOfWords = set()
    counter = 0
    commentFound = False
    with open(location,"r") as f:
        for line in f:
            if '"""' in line:
                line = re.sub("(\#)+.*(?=\s)", "", line)
                line = re.sub("\"\s*.*?\s*\"", "", line)
                line = re.sub("(\%)+.*(?=\s)", "", line)
                line = re.sub("(\//.*)", "", line)
                line = re.sub("(\;.*)", "", line)
                line = re.findall("(\s*[a-zA-Z]*\s*)", line)
                for item in line:
                    item = item.rstrip('\t\r\n')
                    item = re.sub("\s+", "", item)
                    item = item.rstrip('\n')
                    if listOfWords.__contains__(item) is False:
                        listOfWords.add(item)
                while '"""' not in line:
                    line = f.next()
            line = re.sub("(\#)+.*(?=\s)", "", line)
            line = re.sub("\"\s*.*?\s*\"", "", line)
            line = re.sub("(\%)+.*(?=\s)", "", line)
            line = re.sub("(\//.*)", "", line)
            line = re.sub("(\;.*)", "", line)
            line = re.findall("(\s*[a-zA-Z]*\s*)", line)
            for item in line:
                item = item.rstrip('\t\r\n')
                item = re.sub("\s+", "", item)
                item = item.rstrip('\n')
                if listOfWords.__contains__(item) is False:
                    listOfWords.add(item)
            listOfWords.pop()
    return Language(name,counter,listOfWords,location)


def generateHTML(project):
    f= open(os.getcwd()+"/index.html","w+")

    cSite = "<html><body><h1>C Project</h1><p>List of words:</p>"
    cSite = cSite + str(project[0].wordList)
    cSite = cSite + "'" + "<p> </p><a href=" + "'" +os.getcwd() + "/a1/main.c" + "'" + "><button>Code</button></a></body></html>"

    clojureSite = "<html><body><h1>Clojure Project</h1><p>List of words:</p>"
    clojureSite = clojureSite + str(project[1].wordList)
    clojureSite = clojureSite + "'" + "<p> </p><a href=" + "'" +os.getcwd() + "/a2/main.clj" + "'" + "><button>Code</button></a></body></html>"

    scalaSite = "<html><body><h1>Scala Project</h1><p>List of words:</p>"
    scalaSite = scalaSite + str(project[2].wordList)
    scalaSite = scalaSite + "'" + "<p> </p><a href=" + "'" +os.getcwd() + "/a3/Main.scala" + "'" + "><button>Code</button></a></body></html>"

    prologSite = "<html><body><h1>Prolog Project</h1><p>List of words:</p>"
    prologSite = prologSite + str(project[3].wordList)
    prologSite = prologSite + "'" + "<p> </p><a href=" + "'" +os.getcwd() + "/a4/main.pl" + "'" + "><button>Code</button></a></body></html>"

    pythonSite = "<html><body><h1>Python Project</h1><p>List of words:</p>"
    pythonSite = pythonSite + str(project[4].wordList)
    pythonSite = pythonSite + "'" + "<p> </p><a href=" + "'" +os.getcwd() + "/a4/Main.py" + "'" + "><button>Code</button></a></body></html>"


    websiteMain = """
    <!DOCTYPE html>
<html>
<title>344</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
<style>
body,h1,h2,h3,h4,h5 {font-family: "Raleway", sans-serif}
</style>
<body class="w3-light-grey">

<div class="w3-content" style="max-width:1400px">

<header class="w3-container w3-center w3-padding-32">
  <h1><b>MY CSC344 Projects</b></h1>
  <p>By Andrew Boyce</p>
</header>

<div class="w3-row">

<div class="w3-col l8 s12">
  <div class="w3-card-4 w3-margin w3-white">
    <img src="https://upload.wikimedia.org/wikipedia/en/thumb/b/bb/Turing_machine_1.JPG/1024px-Turing_machine_1.JPG" alt="Nature" style="width:100%">
    <div class="w3-container">
      <h3><b>Turing Machine</b></h3>
      <h5>C Project, <span class="w3-opacity">May 14, 2019</span></h5>
    </div>

    <div class="w3-container">
      <p>This is my implementaton of a Turing Machine in C</p>
      <div class="w3-row">

        <div class="w3-col m4 w3-hide-small">
          <p><button onclick="window.location.href = './a1/main.c.html';">Click Here</button></p>
        </div>
      </div>
    </div>
  </div>

  <div class="w3-card-4 w3-margin w3-white">
    <img src="https://i.stack.imgur.com/U92yS.png" alt="Nature" style="width:100%">
    <div class="w3-container">
      <h3><b>Nand Logic Conversion</b></h3>
      <h5>Clojure Project, <span class="w3-opacity">May 14, 2019</span></h5>
    </div>

    <div class="w3-container">
      <p>This is my implementaton of an "and", "or", and "not" conversion to nand in Clojure.</p>
      <div class="w3-row">

        <div class="w3-col m4 w3-hide-small">
          <p><button onclick="window.location.href = './a2/main.clj.html';">Click Here</button></p>
        </div>
      </div>
    </div>
  </div>

  <div class="w3-card-4 w3-margin w3-white">
    <img src="https://cdn-images-1.medium.com/max/1400/1*QEDiKhSaOgi6W52S5QUHGg.png" alt="Nature" style="width:100%">
    <div class="w3-container">
      <h3><b>String Pattern Matching</b></h3>
      <h5>Scala Project, <span class="w3-opacity">May 14, 2019</span></h5>
    </div>

    <div class="w3-container">
      <p>This is my implementaton of a Pattern matcher using parser combinators.</p>
      <div class="w3-row">

        <div class="w3-col m4 w3-hide-small">
          <p><button onclick="window.location.href = './a3/Main.scala.html';">Click Here</button></p>
        </div>
      </div>
    </div>
  </div>

  <div class="w3-card-4 w3-margin w3-white">
    <img src="http://danielschlegel.org/wp/wp-content/uploads/2017/10/LaserProblem.png" alt="Nature" style="width:100%">
    <div class="w3-container">
      <h3><b>Laser Beams!</b></h3>
      <h5>Prolog Project, <span class="w3-opacity">May 14, 2019</span></h5>
    </div>

    <div class="w3-container">
      <p>In this project we place mirrors on a 2d grid to reflect a laser beam. This should avoid obstacles and leave enough space for a computer scientist to walk through!</p>
      <div class="w3-row">

        <div class="w3-col m4 w3-hide-small">
          <p><button onclick="window.location.href = './a4/main.pl.html';">Click Here</button></p>
        </div>
      </div>
    </div>
  </div>

  <div class="w3-card-4 w3-margin w3-white">
    <img src="https://cdn-images-1.medium.com/max/2600/1*jd8ZKUWtY1AOMwz2CvZG8A.jpeg" alt="Nature" style="width:100%">
    <div class="w3-container">
      <h3><b>Class Summary</b></h3>
      <h5>Python Project, <span class="w3-opacity">May 14, 2019</span></h5>
    </div>

    <div class="w3-container">
      <p>My final project for csc344! This should scrape each file for key words, the line count, create webpages for each project(including this one) and email it zipped to my professor!</p>
      <div class="w3-row">

        <div class="w3-col m4 w3-hide-small">
          <p><button onclick="window.location.href = './a5/Main.py.html';">Click Here</button></p>
        </div>
      </div>
    </div>
  </div>

  <hr>
</div>

</div><br>

</div>

</body>
</html>

"""
    f.write(websiteMain)
    f.close()
    f1= open(os.getcwd()+"/a1/main.c.html","w+")
    f1.write(cSite)
    f1.close()
    f2= open(os.getcwd()+"/a2/main.clj.html","w+")
    f2.write(clojureSite)
    f2.close()
    f3= open(os.getcwd()+"/a3/Main.scala.html","w+")
    f3.write(scalaSite)
    f3.close()
    f4= open(os.getcwd()+"/a4/main.pl.html","w+")
    f4.write(prologSite)
    f4.close()
    f5= open(os.getcwd()+"/a5/Main.py.html","w+")
    f5.write(pythonSite)
    f5.close()



assignments = parser()
generateHTML(assignments)
email = "andyboyce30@aol.com"
shutil.make_archive('csc344', 'zip', os.getcwd())
msg = MIMEMultipart()
attach = open("csc344.zip", "rb")
msg['From'] = email
msg['To'] = email
part = MIMEApplication(attach.read(), Name="csc344.zip")
msg.attach(part)
part.add_header('Content-Disposition', "attachment; filename= " + "csc344.zip")
server = smtplib.SMTP_SSL('smtp.aol.com',465)
server.login(email, "laxbro4life123")
server.sendmail(email, email, msg.as_string())
server.close()
