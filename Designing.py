{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "brown-installation",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "1--->Create a simple web site using frame set. Each page of web site should contain\n",
    "     header, menu,content area and footer. When I click on any link in menu, the related page \n",
    "     should open in the content area.\n",
    "ans->\n",
    "'''\n",
    "<!DOCTYPE html>\n",
    "<html lang=\"en\">\n",
    "    <head>\n",
    "        <meta charset=\"UTF-8\">\n",
    "        <title>My Title</title>\n",
    "    </head>\n",
    "    <body>\n",
    "        <header>\n",
    "            <nav>..navigation menu links here…</nav>\n",
    "        </header>\n",
    "        <article>\n",
    "            <section>…</section>\n",
    "            <section>…</section>\n",
    "            <section>…</section>\n",
    "        </article>\n",
    "        <aside>…</aside>\n",
    "        <footer>…</footer>\n",
    "    </body>\n",
    "</html>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "actual-documentation",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "coordinate-harassment",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "2--->Create three pages and apply formatting to each of them using inline, internal and external Css respectively.\n",
    "ans->\n",
    "'''\n",
    "<!DOCTYPE html>\n",
    "<html>\n",
    "<head>\n",
    "<link rel=\"stylesheet\" href=\"styles.css\">      #External CSS\n",
    "<style>\n",
    "body {background-color: powderblue;}      \n",
    "h1   {color: blue;}                            #Internal CSS\n",
    "p    {color: red;}\n",
    "</style>\n",
    "</head>\n",
    "<body>\n",
    "\n",
    "<h1 style=\"color:blue;\">A Blue Heading</h1>    #Inline CSS\n",
    "\n",
    "<p style=\"color:red;\">A red paragraph.</p>\n",
    "\n",
    "</body>\n",
    "</html>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "corresponding-database",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "usual-kazakhstan",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "3--->Create a tabular layout using divisions and css floating\n",
    "ans->\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "growing-vehicle",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "rough-steal",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "4--->Create a page with a division. Apply border, font color, background color and more using css. \n",
    "     Where division should resize when the browser window resizes.\n",
    "\n",
    "ans->\n",
    "'''\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "downtown-uniform",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "existing-milan",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "5--->place an image in top right corner of the page. The image should remain at that position even the page scrolls.\n",
    "ans->\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "varying-thirty",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "round-flood",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "6--->Create link-pseudo classes using external css, to format links on the pages\n",
    "ans->\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "liquid-honor",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fifty-lender",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "7--->Create a Internal JavaScript for display an alert on Page Load\n",
    "ans->\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "frequent-tracy",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "collective-walter",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "8--->Create a External JavaScript which takes an input from user and display in Alert.\n",
    "ans->\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "adjusted-caribbean",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "destroyed-termination",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "9--->Print a Confirm message on Button click If user click ok then another alert should be there \n",
    "     and if user clicks on cancel then cancellation message should be display.\n",
    "ans->\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "swedish-peninsula",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "favorite-switzerland",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "10--->Write a JavaScript to change the image source on button click\n",
    "ans->\n",
    "'''\n",
    "<h1>Changing the Image</h1>\n",
    "    <img src=\"waterbottel.gif\" id=\"myImage\" width=\"100\" height=\"150\">\n",
    "    <input type=\"button\" onclick=\"changeImage()\" value=\"Change\" />\n",
    "    <p>Click on the \"Change\" button to convert waterbottle<br />\n",
    "        into Softdrink bottle</p>\n",
    "\n",
    "    <script>\n",
    "        function changeImage() {\n",
    "            var image = document.getElementById('myImage');\n",
    "            if (image.src.match(\"colorbottel\")) {            \n",
    "                image.src = \"waterbottel.gif\";\n",
    "            }\n",
    "            else {\n",
    "                image.src = \"colorbottel.gif\";\n",
    "            }\n",
    "        }\n",
    "    </script>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "iraqi-flashing",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "changing-greek",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "11--->Create a simple table with two rows and two columns using JavaScript document.write() function\n",
    "ans->\n",
    "'''\n",
    "function tableCreate() {\n",
    "  var body = document.getElementsByTagName('body')[0];\n",
    "  var tbl = document.createElement('table');\n",
    "  tbl.style.width = '100%';\n",
    "  tbl.setAttribute('border', '1');\n",
    "  var tbdy = document.createElement('tbody');\n",
    "  for (var i = 0; i < 3; i++) {\n",
    "    var tr = document.createElement('tr');\n",
    "    for (var j = 0; j < 2; j++) {\n",
    "      if (i == 2 && j == 1) {\n",
    "        break\n",
    "      } else {\n",
    "        var td = document.createElement('td');\n",
    "        td.appendChild(document.createTextNode('\\u0020'))\n",
    "        i == 1 && j == 1 ? td.setAttribute('rowSpan', '2') : null;\n",
    "        tr.appendChild(td)\n",
    "      }\n",
    "    }\n",
    "    tbdy.appendChild(tr);\n",
    "  }\n",
    "  tbl.appendChild(tbdy);\n",
    "  body.appendChild(tbl)\n",
    "}\n",
    "tableCreate();"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "western-destiny",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "gothic-momentum",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "12--->Implement the Following event. OnClick, OnMouseHover, OnMouseOut.\n",
    "ans->\n",
    "'''\n",
    "<html>\n",
    "  <body>\n",
    "    <p id=\"demo\"></p>\n",
    "      <p>The function bigImg() is triggered when the user moves the mouse pointer over the image.</p>\n",
    "         <p>The function normalImg() is triggered when the mouse pointer is moved out of the image.</p>\n",
    "\n",
    "        <script>\n",
    "            function myFunction() \n",
    "            {\n",
    "              document.getElementById(\"demo\").innerHTML = \"Hello World\";\n",
    "            }\n",
    "\n",
    "            function bigImg(x)\n",
    "            {\n",
    "              x.style.height = \"64px\";\n",
    "              x.style.width = \"64px\";\n",
    "            }\n",
    "\n",
    "            function normalImg(x) \n",
    "            {\n",
    "              x.style.height = \"32px\";\n",
    "              x.style.width = \"32px\";\n",
    "            }\n",
    "            function bigImg(x) \n",
    "            {\n",
    "              x.style.height = \"64px\";\n",
    "              x.style.width = \"64px\";\n",
    "            }\n",
    "\n",
    "            function normalImg(x) \n",
    "            {\n",
    "              x.style.height = \"32px\";\n",
    "              x.style.width = \"32px\";\n",
    "            }\n",
    "        </script>\n",
    "        \n",
    "<button onclick=\"myFunction()\">Click me</button>\n",
    "<img onmouseover=\"bigImg(this)\" onmouseout=\"normalImg(this)\" border=\"0\" src=\"smiley.gif\" alt=\"Smiley\" width=\"32\" height=\"32\">\n",
    "<img onmouseover=\"bigImg(this)\" onmouseout=\"normalImg(this)\" border=\"0\" src=\"smiley.gif\" alt=\"Smiley\" width=\"32\" height=\"32\">\n",
    " </body>\n",
    "</html>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "renewable-glance",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "jewish-flush",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "13--->Create a division which should not resize on browser resize\n",
    "ans->\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ambient-ordinary",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "responsible-fishing",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "14--->Create an elastic page layout.\n",
    "ans->\n",
    "'''"
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
