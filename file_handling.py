{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "1--->What is File function in python?what is keywords to create and write file?\n",
    "ans->The Python open file function returns a file object that contains methods and attributes to perform various operations \n",
    "     for opening files in Python. ... filename: gives name of the file that the file object has opened. mode: \n",
    "     attribute of a file object tells you which mode a file was opened in.\n",
    "\n",
    "     \"x\" - Create - will create a file, returns an error if the file exist\n",
    "\n",
    "     \"a\" - Append - will create a file if the specified file does not exist\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hi im prabhat\\n'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''\n",
    "2--->Write a Python program to read an entire text file\n",
    "ans->\n",
    "'''\n",
    "r = open('tony.txt')\n",
    "r.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "done\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "3--->Write a Python program to append text to a file and display the text.\n",
    "ans->\n",
    "'''\n",
    "a = open('tony.txt','a')\n",
    "a.write('nxksjneked')\n",
    "a.close()\n",
    "print('done')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hi i m prabhat\n",
      "\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "4--->Write a Python program to read first n lines of a file\n",
    "ans->\n",
    "'''\n",
    "'''f = open('tony.txt','a')\n",
    "f.write('how are u?')\n",
    "f.close()\n",
    "print('done')'''\n",
    "\n",
    "a_file = open(\"tony.txt\",'r')\n",
    "\n",
    "number_of_lines = 1\n",
    "\n",
    "for i in range(number_of_lines):\n",
    "    line = a_file.readline()\n",
    "    print(line)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['teyeq']\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "5--->Write a Python program to read last n lines of a file\n",
    "ans->\n",
    "'''\n",
    "a_file = open(\"tony.txt\",'r')\n",
    "lines = a_file.readlines()\n",
    "last_lines = lines[-1:]\n",
    "\n",
    "print(last_lines)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['i l jcnehuiwewef\\n', '45tgtgwet\\n', 'ertwert\\n', 'ertwertert\\n', 'rtwert\\n', 'twert\\n', 'erte\\n', 'rtew\\n', 'teyeq']\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "6--->Write a Python program to read a file line by line and store it into a list\n",
    "ans->\n",
    "'''\n",
    "a_file = open(\"tony.txt\",'r')\n",
    "reads = a_file.readlines()\n",
    "print(reads)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['i l jcnehuiwewef\\n', '45tgtgwet\\n', 'ertwert\\n', 'ertwertert\\n', 'rtwert\\n', 'twert\\n', 'erte\\n', 'rtew\\n', 'teyeq']\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "7--->Write a Python program to read a file line by line store it into a variable.\n",
    "ans->\n",
    "'''\n",
    "a_file = open(\"tony.txt\",'r')\n",
    "var = a_file.readlines()\n",
    "print(var)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['jcnehuiwewef']\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "8--->Write a python program to find the longest words\n",
    "ans->\n",
    "'''\n",
    "\n",
    "with open('tony.txt', 'r') as infile:\n",
    "    words = infile.read().split()\n",
    "    max_len = len(max(words, key=len))\n",
    "    for word in words: \n",
    "        if len(word) == max_len:\n",
    "            print(longest_word('tony.txt'))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This is the number of lines in the file\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "9--->Write a Python program to count the number of lines in a text file.\n",
    "ans->\n",
    "'''\n",
    "file = open('tony.txt','r')\n",
    "Counter = 0\n",
    "  \n",
    "# Reading from file \n",
    "Content = file.read() \n",
    "CoList = Content.split(\"\\n\") \n",
    "  \n",
    "for i in CoList: \n",
    "    if i: \n",
    "        Counter += 1\n",
    "          \n",
    "print(\"This is the number of lines in the file\") \n",
    "print(Counter) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Counter({'prabhat': 2, 'prabhas': 2, 'ganveer': 2, 'ganvir': 2, 'raju': 1, 'shray': 1})\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "10--->Write a Python program to count the frequency of words in a file\n",
    "ans->\n",
    "'''\n",
    "from collections import Counter\n",
    "with open('tony.txt','r') as f:\n",
    "    print(Counter(f.read().split()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "11--->Write a Python program to write a list to a file.\n",
    "ans->\n",
    "'''\n",
    "instruments    =  ['guitar,piano,banjo,band']\n",
    "artist         =  ['arijit,armaan,vishal']\n",
    "composer       =  ['pritam,himesh,ajay-atul']\n",
    "\n",
    "with open ('album.txt','w') as f:\n",
    "    for c in instruments,artist,composer:\n",
    "        f.write(\"%s\\n\" % c)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "12--->Write a Python program to copy the contents of a file to another file\n",
    "ans->\n",
    "'''\n",
    "with open('album.txt','r') as firstfile, open('album2.txt','w') as secondfile: \n",
    "      \n",
    "    # read content from first file \n",
    "    for line in firstfile: \n",
    "\n",
    "         # append content to second file \n",
    "        secondfile.write(line)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'3'"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''\n",
    "13--->Write a Python program to read a random line from a file.\n",
    "ans->\n",
    "'''\n",
    "import random\n",
    "lines = open('album2.txt','r').read().splitlines()\n",
    "random.choice(lines)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "14--->Write a Python program to assess if a file is closed or not\n",
    "ans->\n",
    "'''\n",
    "f = open('album.txt','r')\n",
    "print(f.closed)\n",
    "f.close()\n",
    "print(f.closed)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[\"['guitar,piano,banjo,band']\\n\", \"['arijit,armaan,vishal']\\n\", \"['pritam,himesh,ajay-atul']\\n\", '1\\n', '2\\n', '3\\n', '4\\n', '5\\n', 'g\\n', 'g\\n', 'g']\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "15--->Write a Python program to remove newline characters from a file.\n",
    "ans->\n",
    "'''\n",
    "\n",
    "flist = open('album2.txt').readlines()\n",
    "for s in flist:\n",
    "    s.rstrip('\\n') \n",
    "print(flist)\n"
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
 "nbformat_minor": 4
}
