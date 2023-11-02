```
# AirBnB Clone - The Console

## Overview

The AirBnB Clone project aims to deploy a simplified version of the AirBnB website on a server. The initial phase of this project focuses on developing a command-line tool, referred to as the "Console," to manage AirBnB-related objects. This command-line tool serves as a fundamental component for the subsequent stages of the project, including HTML/CSS templating, database storage, API integration, and front-end development.

## Command Interpreter

The Command Interpreter is designed to enable users to perform essential operations on AirBnB objects, including:

- **Create:** Create new objects such as Users or Places.
- **Retrieve:** Retrieve objects from files, databases, etc.
- **Operations:** Perform various operations on objects, such as counting and computing statistics.
- **Update:** Modify attributes of existing objects.
- **Destroy:** Delete objects.

## Usage

The Command Interpreter can be utilized in both interactive and non-interactive modes:

**Interactive Mode:**
```shell
$ ./console.py
(hbnb) help
```

**Non-Interactive Mode:**
```shell
$ echo "help" | ./console.py
```

## Supported Commands

The following commands are supported by the Command Interpreter:

- **create:** Create a new object of a specified class.
- **show:** Display an object based on its class name and ID.
- **destroy:** Delete an object based on its class name and ID.
- **all:** Display all objects, either of a specific class or of all available classes.
- **update:** Update an instance based on the class name and ID.
- **quit/EOF:** Terminate the console.
- **help:** Display descriptions and usage instructions for each command.

## Getting Started

To begin using the Command Interpreter, navigate to the project directory and run the following command:

```shell
AirBnB_clone$ ./console.py
(hbnb)
```

## Examples

- **Create:**
  To create an object, use the "create" command followed by the class name.
  ```
  (hbnb) create BaseModel
  ```

- **Show:**
  To show an instance, provide the class name and ID.
  ```
  (hbnb) show BaseModel 1234-1234-1234
  ```

- **Destroy:**
  To delete an instance, use the "destroy" command with the class name and ID.
  ```
  (hbnb) destroy BaseModel 1234-1234-1234
  ```

- **All:**
  To display all instances, use the "all" command. To filter by class, specify the class name.
  ```
  (hbnb) all
  (hbnb) all State
  ```

- **Update:**
  To update an instance, use the "update" command with the class name, ID, attribute, and value.
  ```
  (hbnb) update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
  ```

## Supported Classes

The Command Interpreter supports the following classes:

- BaseModel
- User
- State
- City
- Amenity
- Place
- Review

## Authors

- Ilvian Dimco - Email: d.ilvian1993@gmail.com
```
