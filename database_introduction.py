{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "neutral-median",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "1--->What database does Python use? What database API includes?\n",
    "ans->Python supports various databases like MySQL, Oracle, Sybase, PostgreSQL, etc. Python also supports Data Definition \n",
    "     Language (DDL), Data Manipulation Language (DML) and Data Query Statements. For database programming, the Python DB API \n",
    "     is a widely used module that provides a database application programming interface.\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fancy-survivor",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "olympic-reunion",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "2--->Explain benefit of python database programming\n",
    "ans->Programming in Python is arguably more efficient and faster compared to other languages.\n",
    "---->Python is famous for its portability.\n",
    "---->It is platform independent.\n",
    "---->Python supports SQL cursors.\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "tight-volunteer",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "worth-metabolism",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "3--->What is PyMySQL in Python?\n",
    "ans->PyMySQL is an interface for connecting to a MySQL database server from Python. It implements the Python Database API v2. 0 \n",
    "     and contains a pure-Python MySQL client library. The goal of PyMySQL is to be a drop-in replacement for MySQLdb.\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bound-control",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "welsh-sharing",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "4--->How does Python integrate with SQL?\n",
    "ans->connector Python SQL module contains a method . connect() that you use in line 7 to connect to a MySQL database server. \n",
    "     Once the connection is established, the connection object is returned to the calling function. Finally, in line 18 you call\n",
    "     create_connection() with the host name, username, and password.\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "helpful-onion",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "spectacular-question",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "5--->What is MySQLdb Python?What is Generic database interface?\n",
    "ans->MySQLdb is an application programming interface which enables you to connect a Python program with a database server, \n",
    "     and it is built on top MySQL C API.\n",
    "\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cellular-argentina",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "failing-surfing",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "6--->what is relational database system interface?\n",
    "ans->An interface between the user and the Relational Database Management System (RDBMS) takes natural language queries, \n",
    "     translates them to Structured Query Language (SQL) queries, and submits to RDBMS for execution. Various efforts have been\n",
    "     made in the development of natural language interfaces to databases\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "missing-april",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "knowing-martial",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "7--->Write crud program using sql connection\n",
    "ans->Create a Python project in Visual Studio\n",
    "   ->Create a database and a table in SQL\n",
    "   ->Create a config file for the database\n",
    "   ->Install Python Package as \"Pypyodbc\"\n",
    "   ->Create a connection file\n",
    "   ->Create new record\n",
    "   ->Read Data\n",
    "   ->Update existing record\n",
    "   ->Delete data\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "korean-sharp",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "forced-allen",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "8--->make login application using python connectivity\n",
    "ans->\n",
    "'''\n",
    "import pymysql\n",
    "\n",
    "db_connect = pymysql.connect(user='root', password='', databse='Login')\n",
    "\n",
    "<title>Login</title>\n",
    "{% block body %}\n",
    "<form action=\"/lgoin\" method=\"POST\">\n",
    "<div class=\"login\">\n",
    "  <div class=\"login-screen\">\n",
    "    <div class=\"app-title\">\n",
    "      <h1>Login</h1>\n",
    "    </div>\n",
    "  <div class=\"login-form\">\n",
    "    <div class=\"control-group\">\n",
    "        <input type=\"text\" class=\"login-field\" value=\"\" placeholder=\"username\" name=\"username\">\n",
    "        <label class=\"login-field-icon fui-user\" for=\"login-name\"></label>\n",
    "    </div>\n",
    "    <div class=\"control-group\">\n",
    "        <input type=\"password\" class=\"login-field\" value=\"\" placeholder=\"password\" name=\"password\">\n",
    "        <label class=\"login-field-icon fui-lock\" for=\"login-pass\"></label>\n",
    "    </div>\n",
    "     <input type=\"submit\" value=\"Log in\" class=\"btn btn-primary btn-large btn-block\">\n",
    "   </div>\n",
    "  </div>\n",
    " </div>\n",
    "</form>\n",
    "{% endblock %}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "opponent-supervisor",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "turkish-honey",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "9--->What are .Cursor objects?\n",
    "ans->Cursor class is an instance using which you can invoke methods that execute SQLite statements, fetch data from the result \n",
    "     sets of the queries. ... You can create Cursor object using the cursor() method of the Connection object/class.\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fresh-chapel",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "spanish-regular",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "10--->What is Error and exception handling in DB-API\n",
    "ans->According to the Python DB-API errors are indicated by raising exceptions. There is one top-level exception for the DB \n",
    "     package that is used to catch all database exceptions raised by that module. In general this package is 'module. Error'. ... \n",
    "     Every DB-API statement that you execute has the potential to raise an exception.\n",
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
