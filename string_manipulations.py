{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "34\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "1--->Write a Python program to calculate the length of a string.\n",
    "ans->given below.\n",
    "\"\"\"\n",
    "s=\"prabhat ganveer jdb hbcjh chdbjh\"\n",
    "print(len(s))"
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
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "2\n",
      "2\n",
      "2\n",
      "2\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "2--->Write a Python program to count the number of characters (character frequency) in a string\n",
    "ans->given below.\n",
    "\"\"\"\n",
    "s=\"abcabc\"\n",
    "for i in s:\n",
    "    print(s.count(i))"
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
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "3--->What are negative indexes and why are they used?\n",
    "ans->The negative index is used to remove any new-line spaces from the string and allow the string to\n",
    "     except the last character that is given as S[:-1]. The negative index is also used to show the index\n",
    "     to represent the string in correct order.\n",
    "\"\"\""
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
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "4--->Explain split(), sub(), subn() methods of “re” module in Python.\n",
    "ans->The re module in python refers to the module Regular Expressions (RE). It specifies a set of strings or patterns\n",
    "     that matches it. Metacharacters are used to understand the analogy of RE.\n",
    "     \n",
    "---->(1).Function split()\n",
    "\n",
    "This function splits the string according to the occurrences of a character or a pattern. When it finds that pattern, \n",
    "it returns the remaining characters from the string as part of the resulting list.  The split method should be imported \n",
    "before using it in the program.\n",
    "\n",
    "Syntax:  re.split (pattern, string, maxsplit=0, flags=0)\n",
    "\n",
    "---->(2).Function sub()\n",
    "\n",
    "Syntax:\n",
    "\n",
    "re.sub (pattern, repl, string, count=0, flags=0)\n",
    "\n",
    "This function stands for the substring in which a certain regular expression pattern is searched in the given string \n",
    "(3rd parameter). When it finds the substring, the pattern is replaced by repl (2nd parameter). The count checks and maintains\n",
    "the number of times this has occurred.\n",
    "\n",
    "---->(4).Function subn()\n",
    "\n",
    "Syntax:\n",
    "\n",
    "re.subn (pattern, repl, string, count=0, flags=0)\n",
    "\n",
    "This function is similar to sub() in all ways except the way in which it provides the output. It returns a tuple with count of\n",
    "total of all the replacements as well as the new string.\n",
    "\n",
    "\"\"\""
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
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"\\n5--->How do you perform pattern matching in Python?Explain\\nans->Steps of Regular Expression Matching\\n\\n----->(1).Import the regex module with import re.\\n----->(2).Create a Regex object with the re. compile() function. ...\\n----->(3).Pass the string you want to search into the Regex object's search() method. ...\\n----->(4).Call the Match object's group() method to return a string of the actual matched text.\\n\\n\""
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\"\"\n",
    "5--->How do you perform pattern matching in Python?Explain\n",
    "ans->Steps of Regular Expression Matching\n",
    "\n",
    "----->(1).Import the regex module with import re.\n",
    "----->(2).Create a Regex object with the re. compile() function. ...\n",
    "----->(3).Pass the string you want to search into the Regex object's search() method. ...\n",
    "----->(4).Call the Match object's group() method to return a string of the actual matched text.\n",
    "\n",
    "\"\"\""
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
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the string :- abc abc abc\n",
      "substring count :- abc\n",
      "occurrences:-  3\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "6--->Write a Python program to count occurrences of a substring in a string\n",
    "ans->given below\n",
    "\n",
    "\"\"\"\n",
    "a=input(\"enter the string :- \")\n",
    "b=input(\"substring count :- \")\n",
    "print(\"occurrences:- \",a.count(b))"
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
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "7--->Write a Python program to count the occurrences of each word in a given sentence\n",
    "ans->given below\n",
    "\n",
    "\"\"\"\n",
    "a=\"prabhas prabhas ganveer\"\n",
    "b=a.split(\" \")\n",
    "print(b.count(\"prabhas\"))"
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
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "xyc abz\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "8--->Write a Python program to get a single string from two given strings, separated by a space and swap the first \n",
    "     two characters of each string.\n",
    "ans->given below\n",
    "\n",
    "\"\"\"\n",
    "a=('abc')\n",
    "b=('xyz')\n",
    "new_a = b[:2] + a[2:]\n",
    "new_b = a[:2] + b[2:]\n",
    "c= new_a + ' ' + new_b\n",
    "print(c)"
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
   "execution_count": 161,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the string :- ffging\n",
      "ffgingly\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "9--->Write a Python program to add 'ing' at the end of a given string (length should be at least 3).\n",
    "     If the given string already ends with 'ing' then add 'ly' instead If the string length \n",
    "     of the given string is less than 3, leave itunchanged\n",
    "ans->given below\n",
    "\n",
    "\"\"\"\n",
    "str1=input(\"enter the string :- \")\n",
    "length = len(str1)\n",
    "if length > 2:\n",
    "    if str1[-3:] == 'ing':\n",
    "        str1 += 'ly'\n",
    "    else:\n",
    "        str1 += 'ing'\n",
    "print(str1)"
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
   "execution_count": 176,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The lyrics is good!\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "10--->Write a Python program to find the first appearance of the substring'not' and 'poor' from a given string,\n",
    "     if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.Return the resulting string.\n",
    "ans->given below\n",
    "\n",
    "\"\"\"\n",
    "str1=('The lyrics is not that poor!')\n",
    "snot = str1.find('not')\n",
    "spoor = str1.find('poor')\n",
    "\n",
    "if spoor > snot and snot>0 and spoor>0:\n",
    "    str1 = str1.replace(str1[snot:(spoor+4)], 'good') \n",
    "    print(str1)\n",
    "else:\n",
    "    print(\"not find\")"
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
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The largest word is at  0  and has length  3\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "11--->Write a Python function that takes a list of words and returns the length of the longestone.\n",
    "ans-->given below\n",
    "\n",
    "\"\"\"\n",
    "a = ['dva','bc','d'] \n",
    "len_a = [len(i) for i in a] \n",
    "max_length = max(len_a) \n",
    "print(\"The largest word is at \", len_a.index(max_length),\" and has length \",max_length)"
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
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a name:pouy\n",
      "yuop\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "12--->Write a Python function to reverses a string if it's length is a multiple of 4.\n",
    "ans-->given below\n",
    "\n",
    "\"\"\"\n",
    "name=input(\"enter a name:\")\n",
    "\n",
    "if(len(name)%4==0):\n",
    "    print(name[::-1])\n",
    "else:\n",
    "    print(\"cant\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the string :- w3resource\n",
      "w3ce\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "13--->Write a Python program to get a string made of the first 2 and the last 2chars\n",
    "      from a given a string. If the string length is less than 2, return instead of the empty string. \n",
    "      Go to the editor\n",
    "      Sample String : 'w3resource' \n",
    "      Expected Result : 'w3ce' \n",
    "      Sample String : 'w3' \n",
    "      Expected Result : 'w3w3' \n",
    "      Sample String : ' w'\n",
    "      Expected Result : Empty String\n",
    "ans-->given below\n",
    "\n",
    "\"\"\"\n",
    "\n",
    "str1=input(\"enter the string :- \")\n",
    "if len(str1) < 2:\n",
    "    print(\" \")\n",
    "else:\n",
    "    res=str1[0:2] + str1[-2:]\n",
    "    print(res)"
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
   "execution_count": 219,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "resta$t\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "14--->Write a Python program to get a string from a given string where all occurrences of its first char have been \n",
    "      changed to '$', except the first char itself\n",
    "ans-->given below\n",
    "\n",
    "\"\"\"\n",
    "str1='restart'\n",
    "char = str1[0] \n",
    "str2 = str1.replace(char, '$')\n",
    "str2 = char + str2[1:]\n",
    "print(str2)"
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
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[python]]\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "15--->Write a Python function to insert a string in the middle of astring.\n",
    "ans-->given below\n",
    "\n",
    "\"\"\"\n",
    "str1='[[]]'\n",
    "word='python'\n",
    "c=str1[:2] + word + str1[2:]\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
