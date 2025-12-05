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


## Pseudocode
START PROGRAM

CREATE list LOST_ITEMS
CREATE list FOUND_ITEMS

DISPLAY "Find My Stuff"
DISPLAY options:
1. Report Lost Item
2. Report Found Item
3. Search Items
4. Exit

GET user_choice

IF user_choice = 1 THEN
    DISPLAY "Enter lost item details"
    GET item_name
    GET item_description
    GET item_location
    GET item_date

    CREATE lost_item record with the details
    ADD lost_item to LOST_ITEMS

    DISPLAY "Lost item recorded."

ELSE IF user_choice = 2 THEN
    DISPLAY "Enter found item details"
    GET item_name
    GET item_description
    GET item_location
    GET item_date

    CREATE found_item record with the details
    ADD found_item to FOUND_ITEMS

    DISPLAY "Found item recorded."

ELSE IF user_choice = 3 THEN
    DISPLAY "Search for:"
    DISPLAY "1. Lost Items"
    DISPLAY "2. Found Items"
    DISPLAY "3. Automatic Match"

    GET search_choice

    IF search_choice = 1 THEN
        GET keyword
        SEARCH LOST_ITEMS for keyword
        DISPLAY matching results

    ELSE IF search_choice = 2 THEN
        GET keyword
        SEARCH FOUND_ITEMS for keyword
        DISPLAY matching results

    ELSE IF search_choice = 3 THEN
        FOR each lost_item in LOST_ITEMS
            FOR each found_item in FOUND_ITEMS
                IF lost_item.name similar to found_item.name THEN
                    DISPLAY "Possible match:"
                    DISPLAY lost_item information
                    DISPLAY found_item information
                ENDIF
            END FOR
        END FOR
    ENDIF

ELSE IF user_choice = 4 THEN
    DISPLAY "Goodbye."
    END PROGRAM

ENDIF

LOOP back to main menu

END PROGRAM

## Contributors
Student 1: Bradgette Angel C. Macheca (data input and validation)

Student 2: Rafael Barabar (search and matching logic)

Student 3: Sharlin Minji Kang (user interface design)
