# Get list of users searching by tags in posts

The purpose of this project, is to search a given number of posts that have a given tag(s), after you have gathered all the
posts.-

In case you gave only 1 tag, it will ask for a json for each post, and will get you the user profile that uploaded
a post with that tag.

## Getting Started

First check that you have all the prerequisites, take in mind that the versions specified, where the ones that were used
to develop this project, if you have a newer version it may or may not work.

We will be using the modules requests of python and instagram php scraper from postaddictme (https://github.com/postaddictme/Instagram-php-scraper)

### Prerequisites

For executing the project

You will need python for running this, the version at the moment of writing this project

version 3.7.0

If you want to see what version of python you have execute the following

	python -V

keep in mind, that there are some programs that can create virtual environments,
this makes posible the usage of different versions of a language in the same system
if you are interested in this you might look for

pyenv for python

OR

virtual environment, depending on your needs

If you dont have python installed, you can download and install it looking at the following links		

If using windows

	https://www.python.org/downloads/windows/

if using MacOS

	https://www.python.org/downloads/mac-osx/

or if using linux

	https://www.python.org/downloads/source/

if using linux you might want to check your dist repositories.

Afterwards you will need to install Requests for python

	https://github.com/requests/requests

You can installed it via pip or pip env

	pip install requests

OR

	pipenv install requests

Also you will need php

version=7.1.20

To see what version you have you can do "php -v" on your terminal otherwise here is the
link to download it

	http://php.net/downloads.php

If using a linux distribution you might aswell check your distibution
repositories for installing php

### Installing

So i wanted to keep it simple, if you have all the requirements, you only need to download/clone this project
and modify some parts of the files for its usage

Once you download/clone this project you will have this directory

    InsSearchUsrByPostTags/
        Cache/
        Scrappers/
        vendor/
        Composer.json
        composer.lock
    README.md

go into the Scrappers folder and you will find 2 files

    multiple.py
    scrap-posts.php

open scrap-posts.php

You will se in line 14, that there is "Instagram::withCredentials",
on this line, you will have to change

    <user_name> for your instagram user_name
    <user_password> for your instagram password
    <path/to/cache/folder_in_this_project> for your absolute path (dont know why it has some struggles with relative)

once changed you will be able to run the program

### Usage

This project consist in 2 parts, using php to get n number of posts
and using python to ask for information about those post in a json format.

So on a terminal, change to the Scrappers folder and do:

    php scrap-posts.php dogs photo 100

you will see a number 1 right after pressing enter, this means it started looking for posts that have the "dogs" tag, when you see a number 2, it means it started with the "photo" tag, keep in mind that if you ask for a lot of posts, instagram might block your requests for a few minutes, so far, 2000 posts per tag with a sleep of 120 doesnt have that problem, you can change the sleep time in the line 27 of the scrap-posts.php file.

you will notice that after the code finishes, many files are going to show up, dont worry, they are needed, you will see 3 files

    hashtag_no_1.txt *
    hashtag_no_2.txt *
    list_of_files.txt *
    multiple.py  
    scrap-posts.php

* all the new files

list_of_files.txt is for python to know how many hastags were used on the search while the others contain the posts for each tag.

now you execute

    python multiple.py

If there are posts that have both tags you will start seeing in your terminal something like this:

    ...
    12 Boug9iinqqF cottagecountryfrenchie
    ...

the number is just for you to see how many there are, the second part "Boug9iinqqF" corresponds to the id of the post that was found with both tags, and the last part "cottagecountryfrenchie" is the user who uploaded/created the post, now you will see a new file called list_of_users.txt where you can find the url of the user

And there you have it


## What could be next

I want to add some more options when running the code, so you can get a file or on the terminal the url of the post and the url of the user together. But ill see later what comes to mind.
