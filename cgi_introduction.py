{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "together-boulder",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "1--->What is CGI programming?What is Python CGI?\n",
    "ans->Advertisements. The Common Gateway Interface, or CGI, is a set of standards that define how information is exchanged \n",
    "     between the web server and a custom script.\n",
    "---->Python CGI stands for Common Gateway Interface. An HTTP server invokes a Python CGI script so it can process user input \n",
    "     that a user may submit through an HTML <FORM> or <ISINDEX> element. Such a script usually lives in the server's special\n",
    "     cgi-bin directory. ... Python CGI module handles situations and helps debug scripts.\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "changed-rendering",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "alleged-forth",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "2--->How do I run a Python script on Windows Apache?\n",
    "ans->Apache run python script\n",
    "1---->Install python yum install python.\n",
    "2---->Check python version python -V.\n",
    "3---->Create a test script cd /home/USERNAME/public_html mkdir cgi-bin nano cgi-bin/test.py.\n",
    "4---->Now add the following python test script in the file:\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cardiac-minutes",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "modern-drinking",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "3--->explain CGI Architecture\n",
    "ans->CGI (Common Gateway Interface) is a standard way of running programs from a Web server. Often, CGI programs are \n",
    "     used to generate pages dynamically or to perform some other action when someone fills out an HTML form and clicks \n",
    "     the submit button. ... A reader sends a URL that causes the AOLserver to use CGI to run a program.\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "desirable-measure",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "liked-banking",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\n4--->write hello world program using CGI program\\nans->\\n'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''\n",
    "4--->write hello world program using CGI program\n",
    "ans->\n",
    "'''\n",
    "#!/usr/bin/python\n",
    "print \"Content-type:text/html\\r\\n\\r\\n\"\n",
    "print '<html>'\n",
    "print '<head>'\n",
    "print '<title>Hello Word - First CGI Program</title>'\n",
    "print '</head>'\n",
    "print '<body>'\n",
    "print '<h2>Hello Word! This is my first CGI program</h2>'\n",
    "print '</body>'\n",
    "print '</html>'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "unavailable-trail",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "forced-creativity",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "5--->what is CGI Enviorment variable?what is difference between GET and POST method?\n",
    "ans->These methods are GET Method and POST Method. ... The GET method has size limitation: only 1024 characters can be \n",
    "     sent in a request string. The GET method sends information using QUERY_STRING header and will be accessible in your \n",
    "     CGI Program through QUERY_STRING environment variable\n",
    "---->Both GET and POST method is used to transfer data from client to server in HTTP protocol but Main difference between \n",
    "     POST and GET method is that GET carries request parameter appended in URL string while POST carries request parameter \n",
    "     in message body which makes it more secure way of transferring data from client to\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "numerical-circulation",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "oriented-bronze",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "6--->what is cookies?How It Works?\n",
    "ans->Cookies are created to identify you when you visit a new website. The web server — which stores the website's data — \n",
    "     sends a short stream of identifying info to your web browser. Browser cookies are identified and read by “name-value” \n",
    "     pairs. These tell cookies where to be sent and what data to recall.\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "advisory-custody",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "alive-sterling",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''\n",
    "7--->how to set and Retrieve Cookies?exaplin with coding snippets\n",
    "ans->It is very easy to send cookies to browser. These cookies are sent along with HTTP Header before to Content-type field. \n",
    "     Assuming you want to set UserID and Password as cookies. Setting the cookies is done as follows −\n",
    "'''\n",
    "Example\n",
    "#!/usr/bin/python\n",
    "print \"Set-Cookie:UserID = XYZ;\\r\\n\"\n",
    "print \"Set-Cookie:Password = XYZ123;\\r\\n\"\n",
    "print \"Set-Cookie:Expires = Tuesday, 31-Dec-2007 23:12:40 GMT\";\\r\\n\"\n",
    "print \"Set-Cookie:Domain = www.tutorialspoint.com;\\r\\n\"\n",
    "print \"Set-Cookie:Path = /perl;\\n\"\n",
    "print \"Content-type:text/html\\r\\n\\r\\n\"\n",
    "...........Rest of the HTML Content....\n",
    "\n",
    "#From this example, you must have understood how to set cookies. We use Set-Cookie HTTP header to set cookies.\n",
    "\n",
    "#It is optional to set cookies attributes like Expires, Domain, and Path. It is notable that cookies are set before sending magic line \"Content-type:text/html\\r\\n\\r\\n."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "sound-collect",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "vanilla-leone",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\n8--->write python program to upload file using cookies\\nans->\\n'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''\n",
    "8--->write python program to upload file using cookies\n",
    "ans->\n",
    "'''\n",
    "import requests\n",
    " \n",
    "files = {'file' : open('filename', 'rb')}\n",
    " \n",
    "res = requests.post('url' , files= files)\n",
    " \n",
    "print(res.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "corresponding-purple",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "iraqi-employer",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "9--->write python CGI program structure\n",
    "ans->\n",
    "'''\n",
    "#!/usr/bin/python\n",
    "\n",
    "print \"Content-type:text/html\\r\\n\\r\\n\"\n",
    "print '<html>'\n",
    "print '<head>'\n",
    "print '<title>Hello World - First CGI Program</title>'\n",
    "print '</head>'\n",
    "print '<body>'\n",
    "print '<h2>Hello World! This is my first CGI program</h2>'\n",
    "print '</body>'\n",
    "print '</html>'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "muslim-triple",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "included-marking",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "10--->Write a Python program which passes two values to hello_get.py program using GET method.\n",
    "ans->\n",
    "'''\n",
    "#!/usr/bin/python\n",
    "# Import modules for CGI handling\n",
    "import cgi, cgitb\n",
    "# Create instance of FieldStorage\n",
    "form = cgi.FieldStorage()\n",
    "# Get data from fields\n",
    "first_name = form.getvalue('first_name')\n",
    "last_name = form.getvalue('last_name')\n",
    "print \"Content-type:text/html\\r\\n\\r\\n\"\n",
    "print \"<html>\"\n",
    "print \"<head>\"\n",
    "print \"<title>Hello - Second CGI Program</title>\"\n",
    "print \"</head>\"\n",
    "print \"<body>\"\n",
    "print \"<h2>Hello %s %s</h2>\" % (first_name, last_name)\n",
    "print \"</body>\"\n",
    "print \"</html>\"\n",
    "\n",
    "...................................................................\n",
    "\n",
    "<form action = \"/cgi-bin/hello_get.py\" method = \"get\">\n",
    "First Name: <input type = \"text\" name = \"first_name\"> <br />\n",
    "Last Name: <input type = \"text\" name = \"last_name\" />\n",
    "<input type = \"submit\" value = \"Submit\" />\n",
    "</form>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "hindu-congress",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "decreased-collapse",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "11--->What is Cgitb in Python?\n",
    "ans->The cgitb module provides a special exception handler for Python scripts. (Its name is a bit misleading. \n",
    "     It was originally designed to display extensive traceback information in HTML for CGI scripts. It was later generalized \n",
    "     to also display this information in plain text.)\n",
    "'''\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "demonstrated-request",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "satisfied-rings",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "12--->Write a Python programfor Passing Checkbox Data to CGI Program\n",
    "ans->\n",
    "'''\n",
    "#Here is example HTML code for a form with one checkbox −\n",
    "<form action = \"/cgi-bin/checkbox.cgi\" method = \"POST\" target = \"_blank\">\n",
    "<input type = \"checkbox\" name = \"maths\" value = \"on\" /> Maths\n",
    "<input type = \"checkbox\" name = \"physics\" value = \"on\" /> Physics\n",
    "<input type = \"submit\" value = \"Select Subject\" />\n",
    "</form>\n",
    "\n",
    "............................................................................\n",
    "\n",
    "#Below is checkbox.py script to handle input given by web browser.\n",
    "#!/usr/bin/python\n",
    "# Import modules for CGI handling\n",
    "import cgi, cgitb\n",
    "# Create instance of FieldStorage\n",
    "form = cgi.FieldStorage()\n",
    "# Get data from fields\n",
    "if form.getvalue('maths'):\n",
    "    math_flag = \"ON\"\n",
    "else:\n",
    "    math_flag = \"OFF\"\n",
    "if form.getvalue('physics'):\n",
    "    physics_flag = \"ON\"\n",
    "else:\n",
    "    physics_flag = \"OFF\"\n",
    "print \"Content-type:text/html\\r\\n\\r\\n\"\n",
    "print \"<html>\"\n",
    "print \"<head>\"\n",
    "print \"<title>Checkbox - Third CGI Program</title>\"\n",
    "print \"</head>\"\n",
    "print \"<body>\"\n",
    "print \"<h2> CheckBox Maths is : %s</h2>\" % math_flag\n",
    "print \"<h2> CheckBox Physics is : %s</h2>\" % physics_flag\n",
    "print \"</body>\"\n",
    "print \"</html>\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "moved-contract",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "earlier-interview",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "13--->Write a Python program for Passing Radio Button Data to CGI Program\n",
    "ans->\n",
    "'''\n",
    "\n",
    "#Here is example HTML code for a form with one Radio Button −\n",
    "<form action = \"/cgi-bin/\" method = \"post\" target = \"_blank\">\n",
    "<input type = \"radio\" name = \"subject\" value = \"maths\" /> Maths\n",
    "<input type = \"radio\" name = \"subject\" value = \"physics\" /> Physics\n",
    "<input type = \"submit\" value = \"Select Subject\" />\n",
    "</form>\n",
    "\n",
    "...................................................................................\n",
    "\n",
    "#Below is radiobutton.py script to handle input given by web browser.\n",
    "#!/usr/bin/python\n",
    "# Import modules for CGI handling\n",
    "import cgi, cgitb\n",
    "# Create instance of FieldStorage\n",
    "form = cgi.FieldStorage()\n",
    "# Get data from fields\n",
    "if form.getvalue('subject'):\n",
    "    subject = form.getvalue('subject')\n",
    "else:\n",
    "    subject = \"Not set\"\n",
    "print \"Content-type:text/html\\r\\n\\r\\n\"\n",
    "print \"<html>\"\n",
    "print \"<head>\"\n",
    "print \"<title>Radio - Fourth CGI Program</title>\"\n",
    "print \"</head>\"\n",
    "print \"<body>\"\n",
    "print \"<h2> Selected Subject is %s</h2>\" % subject\n",
    "print \"</body>\"\n",
    "print \"</html>\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "prostate-robertson",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "convenient-feedback",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "14--->Write a Python program for Passing Text Area Data to CGI Program\n",
    "ans->\n",
    "'''\n",
    "#Here is example HTML code for a form with one textarea −\n",
    "<form action = \"/cgi-bin/textarea.py\" method = \"post\" target = \"_blank\">\n",
    "<textarea name = \"textcontent\" cols = \"40\" rows = \"4\">\n",
    "Type your text here...\n",
    "</textarea>\n",
    "<input type = \"submit\" value = \"Submit\" />\n",
    "</form>\n",
    "............................................................................\n",
    "\n",
    "#Below is textarea.py script to handle input given by web browser.\n",
    "#!/usr/bin/python\n",
    "# Import modules for CGI handling\n",
    "import cgi, cgitb\n",
    "# Create instance of FieldStorage\n",
    "form = cgi.FieldStorage()\n",
    "# Get data from fields\n",
    "if form.getvalue('textcontent'):\n",
    "    text_content = form.getvalue('textcontent')\n",
    "else:\n",
    "    text_content = \"Not entered\"\n",
    "print \"Content-type:text/html\\r\\n\\r\\n\"\n",
    "print \"<html>\"\n",
    "print \"<head>\";\n",
    "print \"<title>Text Area - Fifth CGI Program</title>\"\n",
    "print \"</head>\"\n",
    "print \"<body>\"\n",
    "print \"<h2> Entered Text Content is %s</h2>\" % text_content\n",
    "print \"</body>\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "written-smith",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "divided-penetration",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "15--->Write a Python program for Passing Drop down Data to CGI Program\n",
    "ans->\n",
    "'''\n",
    "#Here is example HTML code for a form with one drop down box −\n",
    "<form action = \"/cgi-bin/dropdown.py\" method = \"post\" target = \"_blank\">\n",
    "<select name = \"dropdown\">\n",
    "<option value = \"Maths\" selected>Maths</option>\n",
    "<option value = \"Physics\">Physics</option>\n",
    "</select>\n",
    "<input type = \"submit\" value = \"Submit\"/>\n",
    "</form>\n",
    "\n",
    "..................................................................................\n",
    "#Below is dropdown.py script to handle input given by web browser.\n",
    "\n",
    "#!/usr/bin/python\n",
    "# Import modules for CGI handling\n",
    "import cgi, cgitb\n",
    "# Create instance of FieldStorage\n",
    "form = cgi.FieldStorage()\n",
    "# Get data from fields\n",
    "if form.getvalue('dropdown'):\n",
    "    subject = form.getvalue('dropdown')\n",
    "else:\n",
    "    subject = \"Not entered\"\n",
    "print \"Content-type:text/html\\r\\n\\r\\n\"\n",
    "print \"<html>\"\n",
    "print \"<head>\"\n",
    "print \"<title>Dropdown Box - Sixth CGI Program</title>\"\n",
    "print \"</head>\"\n",
    "print \"<body>\"\n",
    "print \"<h2> Selected Subject is %s</h2>\" % subject\n",
    "print \"</body>\"\n",
    "print \"</html>\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "concerned-aaron",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "identical-romance",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "16--->How To Raise a \"File Download\" Dialog Box?\n",
    "ans->\n",
    "'''\n",
    "#!/usr/bin/python\n",
    "# HTTP Header\n",
    "print \"Content-Type:application/octet-stream; name = \\\"FileName\\\"\\r\\n\";\n",
    "print \"Content-Disposition: attachment; filename = \\\"FileName\\\"\\r\\n\\n\";\n",
    "# Actual File Content will go here.\n",
    "fo = open(\"foo.txt\", \"rb\")\n",
    "str = fo.read();\n",
    "print str\n",
    "# Close opend file\n",
    "fo.close()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
