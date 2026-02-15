## Project Title: Find My Stuff

## Project Description
Find My Stuff is a simple lost-and-found tracking system designed to help users report, search, and claim lost items. The project aims to make it easier for people to locate missing belongings or return found items to their rightful owners. It provides a structured way to record item details and retrieve matches efficiently.

## Problem Statement
Students and community members often lose their belongings, and traditional methods like handwritten notices or verbal announcements are disorganized and unreliable.
Find My Stuff solves this problem by offering a centralized system for recording, finding, and recovering lost items.

## Target Users
*Students and teachers who lose or find items

*School staff managing lost-and-found

*Anyone who wants a simple way to track lost belongings

## Project Objectives
1. Provide an organized way to report lost and found items

2. Allow users to search for items quickly

3. Automatically match found items with lost item reports

4. Store data for future reference

5. Allow users to update or delete their entries

## Features

-Add lost item details (name, description, location, date)

-Add found item details

-Search for lost or found items

-Match found items with lost reports

-Update or delete entries

-Store and retrieve data for future reference

## Inputs and Outputs
## Inputs

*Item name

*Description

*Location

*Date

*Category(optional)

*User contact info (optional)

## Outputs

*List of matching lost and found items

*Confirmation of added entries

*Updated or deleted item logs

*Search results based or keywords

## How to Use the Project
1. Launch the program or open the file.
2. Choose whether to report a lost item, report a found item, or search the database.
3. Fill in the required details.
4. View matches or search results.
5. Follow the instructions to contact the owner or claimant.

## Example Usage
Lost Item Report


Name: Black Wallet

Description: Contains school ID and cash

Location: School library

Date: August 10, 2025


Search Result

A matching wallet was found in the school cafeteria on August 11, 2025.


## Detailed Methodology
## 1. System Architecture
The project consists of three main modules.
## a. Input Module
Handles input for lost or found items.
Includes data validation for required fields.
## b. Storage Module
Stores data in JSON or CSV files for easy reading and writing.

```
{

  "item_name": "",
  
  "description": "",
  
  "location": "",
  
  "date": "",
  
  "category": "",
  
  "contact": "",
  
  "status": "lost" or "found"
  
}
```

## c. Search and Matching Module

Searches based on:

• Keywords

• Items with similar location, date, or name

• Matches entries from lost and found lists automatically.


## Technologies Used
| Technology    | Purpose                         | Reason                                      |
|---------------|---------------------------------|---------------------------------------------|
| Python        | Logic, processing, and search  | Easy to learn, readable, and widely used  |
| JSON/CSV      | Data storage                    | Lightweight and simple to read/write       |
| GitHub        | Version control and collaboration | Tracks changes, allows teamwork, stores files |
| HTML/CSS (optional) | Frontend interface          | Makes the user interface accessible and easy to use |


## Backend–Frontend Communication (If applicable)

• User fills a form in the interface

• Data is sent to the backend for processing

• Backend stores the data and returns matching results

• Results are displayed on the screen

## Key Design Decisions

• Use of simple file-based storage for accessibility

• Modular structure to keep the code organized

• Keyword search for simplicity and speed

• Minimalistic interface for accessibility and ease of use


## Programming and Computing Ethics

The project follows ethical guidelines that ensure responsible programming.

## 1. Privacy

* Contact information is optional

* Only necessary data is collected
  
* Data stored in simple, readable, and modifiable formats

## 2. Intellectual Property

* All external code is credited appropriately
 
* No plagiarism
 
* Proper citations used following APA format

## 3. Accessibility and Inclusion

* Simple UI
  
* Readable text and beginner-friendly layout

* Avoids unnecessary complexity

## 4. Professional Responsibility

Based on the ACM Code of Ethics:

*Avoid harm

*Respect privacy

*Be honest and trustworthy

*Credit others’ work

*Ensure computing benefits society


## GitHub Repository Information

## 1. File Structure

```FindMyStuff/
│── src/
│    ├── main.py
│    ├── search.py
│    ├── storage.py
│── data/
│    ├── lost_items.json
│    ├── found_items.json
│── docs/
│    ├── README.md
│    ├── CHANGELOG.md
│── tests/
│── LICENSE
```

## 2. Commit Messages

Should be descriptive and meaningful:

* “Added search module with keyword filter”

* “Updated README with methodology section”

* “Improved data validation for lost item inputs”

## 3. Branch Usage (optional)

* main for final code

* dev for new features

## 4. README Must Contain

* Description of the project

* How to install and run

* Technologies used

## Contributors
Student 1: Bradgette Angel C. Macheca (data input and validation)

Student 2: Rafael Barabar 

Student 3: Sharlin Minji Kang (user interface design)

## References (APA Style)

Association for Computing Machinery. (2018). ACM Code of Ethics and Professional Conduct. https://www.acm.org/code-of-ethics
