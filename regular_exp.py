{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "treated-batch",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "1--->Does Python support strongly for regular expressions?\n",
    "     What are the other languages that support strongly for regular expressions?\n",
    "ans->Yes, python strongly support regular expression. Other languages supporting regular expressions \n",
    "     are: Delphi, Java, Java script, . NET, Perl, Php, Posix, python, Ruby, Tcl, Visual Basic, XML schema, \n",
    "          VB script, Visual Basic 6.\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "western-gateway",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "synthetic-deployment",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Found a match!\n",
      "Found a match!\n",
      "Found a match!\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "2--->Write a Python program that matches a string that has an a followed by zero or more b's\n",
    "ans->\n",
    "'''\n",
    "import re\n",
    "def text_match(text):\n",
    "        patterns = 'ab*?'\n",
    "        if re.search(patterns,  text):\n",
    "                return 'Found a match!'\n",
    "        else:\n",
    "                return('Not matched!')\n",
    "\n",
    "print(text_match(\"ab\"))\n",
    "print(text_match(\"abc\"))\n",
    "print(text_match(\"abbc\"))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "advisory-finland",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "different-stewart",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "3--->Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)\n",
    "ans->\n",
    "'''\n",
    "import re\n",
    "def is_allowed_specific_char(string):\n",
    "    charRe = re.compile(r'[^a-zA-Z0-9.]')\n",
    "    string = charRe.search(string)\n",
    "    return not bool(string)\n",
    "\n",
    "print(is_allowed_specific_char(\"ABCDEFabcdef123450\")) \n",
    "print(is_allowed_specific_char(\"*&%@#!}{\"))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "afraid-aluminum",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "fallen-approval",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "4--->Write a Python program where a string will start with a specific number\n",
    "ans->\n",
    "'''\n",
    "import re\n",
    "def match_num(string):\n",
    "    text = re.compile(r\"^5\")\n",
    "    if text.match(string):\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "print(match_num('5-2345861'))\n",
    "print(match_num('6-2345861'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "alive-grade",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "preceding-pollution",
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
    "5--->Write a Python program to check for a number at the end of a string\n",
    "ans->\n",
    "'''\n",
    "import re\n",
    "def end_num(string):\n",
    "    text = re.compile(r\".*[0-9]$\")\n",
    "    if text.match(string):\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "\n",
    "print(end_num('abcdef'))\n",
    "print(end_num('abcdef0'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aggressive-roller",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "structural-handle",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Found a match!\n",
      "Not matched!\n",
      "Not matched!\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "6--->Write a Python program to find sequences of lowercase letters joined with a underscore.\n",
    "ans->\n",
    "'''\n",
    "import re\n",
    "def text_match(text):\n",
    "        patterns = '^[a-z]+_[a-z]+$'\n",
    "        if re.search(patterns,  text):\n",
    "                return 'Found a match!'\n",
    "        else:\n",
    "                return('Not matched!')\n",
    "\n",
    "print(text_match(\"aab_cbbbc\"))\n",
    "print(text_match(\"aab_Abbbc\"))\n",
    "print(text_match(\"Aaab_abbbc\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "accepting-accessory",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "three-trade",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Found a match!\n",
      "Not matched!\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "7--->Write a Python program that matches a word containing 'z', not start or end of the word.\n",
    "ans->\n",
    "'''\n",
    "import re\n",
    "def text_match(text):\n",
    "        patterns = '\\Bz\\B'\n",
    "        if re.search(patterns,  text):\n",
    "                return 'Found a match!'\n",
    "        else:\n",
    "                return('Not matched!')\n",
    "\n",
    "print(text_match(\"The quick brown fox jumps over the lazy dog.\"))\n",
    "print(text_match(\"Python Exercises.\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "statutory-passage",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "facial-symposium",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "50\n",
      "Index position: 62\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "8--->Write a Python program to separate and print the numbers and their position of a given string\n",
    "ans->\n",
    "'''\n",
    "import re\n",
    "# Input.\n",
    "text = \"The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly.\"\n",
    "\n",
    "for m in re.finditer(\"\\d+\", text):\n",
    "    print(m.group(0))\n",
    "    print(\"Index position:\", m.start())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "adaptive-seminar",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "impossible-merchandise",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python:Exercises::PHP:exercises:\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "9--->Write a Python program to replace all occurrences of space, comma, or dot with a colon\n",
    "ans->\n",
    "'''\n",
    "import re\n",
    "text = 'Python Exercises, PHP exercises.'\n",
    "print(re.sub(\"[ ,.]\", \":\", text))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "virgin-december",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "congressional-excerpt",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original string:  Python    Exercises \n",
      "Without extra spaces: PythonExercises\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "10--->Write a Python program to remove all whitespaces from a string\n",
    "ans->\n",
    "'''\n",
    "import re\n",
    "text1 = ' Python    Exercises '\n",
    "print(\"Original string:\",text1)\n",
    "print(\"Without extra spaces:\",re.sub(r'\\s+', '',text1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "activated-proxy",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "communist-ribbon",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PythonExercises12\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "11--->Write a Python program to remove everything except alphanumeric characters from a string\n",
    "ans->\n",
    "'''\n",
    "import re\n",
    "text1 = '**//Python Exercises// - 12. '\n",
    "pattern = re.compile('[\\W_]+')\n",
    "print(pattern.sub('', text1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "going-source",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "rough-capacity",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original string: Python      Exercises\n",
      "Without extra spaces: Python Exercises\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "12--->Write a Python program to remove multiple spaces in a string.\n",
    "ans->\n",
    "'''\n",
    "import re\n",
    "text1 = 'Python      Exercises'\n",
    "print(\"Original string:\",text1)\n",
    "print(\"Without extra spaces:\",re.sub(' +',' ',text1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "white-works",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "healthy-confirmation",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python\n",
      "Python Exercises\n",
      "Python Exercises Practice Solution\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "13--->Write a Python program to insert spaces between words starting with capital letters\n",
    "ans->\n",
    "'''\n",
    "import re\n",
    "def capital_words_spaces(str1):\n",
    "    return re.sub(r\"(\\w)([A-Z])\", r\"\\1 \\2\", str1)\n",
    "\n",
    "print(capital_words_spaces(\"Python\"))\n",
    "print(capital_words_spaces(\"PythonExercises\"))\n",
    "print(capital_words_spaces(\"PythonExercisesPracticeSolution\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "brown-county",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "infectious-apartment",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " quick brown jumps over lazy.\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "14--->Write a Python program to remove words from a string of length between 1 and a given number\n",
    "ans->\n",
    "'''\n",
    "import re\n",
    "text = \"The quick brown fox jumps over the lazy dog.\"\n",
    "# remove words between 1 and 3\n",
    "shortword = re.compile(r'\\W*\\b\\w{1,3}\\b')\n",
    "print(shortword.sub('', text))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "increasing-cooper",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "welcome-mongolia",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['quick', 'brown', 'jumps', 'over', 'lazy']\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "15--->Write a Python program to find all words which are at least 4 characters long in a string\n",
    "ans->\n",
    "'''\n",
    "import re\n",
    "text = 'The quick brown fox jumps over the lazy dog.'\n",
    "print(re.findall(r\"\\b\\w{4,}\\b\", text))"
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
