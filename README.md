# py_packman
A Cub Scout pack management web application, written in Python and Django

## Features
* Membership management - complete with address book for keeping track of things
  such as phone numbers and addresses.
    * Parents
    * Scouts
    * Friends of the Pack
* Den Assignments - so you know what cubs belong to which den.
* Committee assignments - Cubs aren't the only ones who get to have all the fun. A
  well run pack has lots of parent involvement. 
* Dynamic content, manageable through Django's built-in admin frameworks.

## Why this app?
Packman was written specifically for the purpose of managing Cub Scout Pack 144,
a pack based in Seattle, WA.  Being a pack headquartered in a tech-heavy community
in the Pacific Northwest, naturally we wanted to have a website that we could adapt
for our own specific use cases.  At the same time, not all of our pack members are
as tech savvy and we need to ensure that the frameworks we put in place with our
web app are accessible to all.  We chose the Django framework because it is highly
flexible, maintainable, and understandable.  That means that even members who do
not live web development day to day should be able to pick it up and continue to
maintain the site.

## How do I get started?
As with any Python and Django project, it is highly recommended that you install
py_packman in its own virtual environment. 

## Requirements
Review the included requirements.txt for detailed package requirements.  Our 
application is built for:
* Django 2.2
* Python 3
