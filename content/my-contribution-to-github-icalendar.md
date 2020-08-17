Title: My contribution to Github-icalendar
Date: 2017-12-20 00:01
Modified: 2017-12-20 00:01
Category: blog
Tags: outreachy, development, github-icalendar
Slug: my-contribution-to-github-icalendar
Authors: Renata
Summary: What I did to apply to Outreachy

Hello!

Now that [you already know a bit about me](/blog/hello-world), let me start talking about my internship with Outreachy.

One of the steps to apply to the internship is to pick the project you would like to work on. I chose the one with Debian to build [a calendar database of social events and conferences](https://wiki.debian.org/Outreachy/Round15/Projects#Outreachy.2FRound15.2FProjects.2FSocialEventAndConferenceCalendars.A_calendar_database_of_social_events_and_conferences).

It is also part of the application process to make some contribution for the project. At first, it wasn't clear to me what contribution would that be (I hadn't found that URL yet), so I went to the [#debian-outreach](irc://irc.debian.org/debian-outreach) IRC channel and... well, asked, of course. That is when I found the page with a description of the task. I was supposed to learn about the iCalendar format (I didn't even know what it was, back then!) and work on an [issue on the github-icalendar project](https://github.com/dpocock/github-icalendar/issues/6): to use repository labels in one of the suggested ways.

## My contribution for github-icalendar

[Github-icalendar](https://github.com/dpocock/github-icalendar/) works by accessing the open issues in all repositories that the user has access to and transforming them into an iCalendar feed of VTODO items.

I chose to solve the labels issue using them to filter the list of issues that should appear in a feed. I imagined two use cases for it:

1. An user wants to get issues from all their repositories that contain a given label (getting all 'bug' issues, for instance)

2. An user wants to get issues from only an specific repository that contain a given label.

Therefore, the label system should support both of these uses.

Working on this contribution taught me not only about the icalendar format, but it also gave me hands-on experience on interacting with the [Github Issues API](https://developer.github.com/v3/issues/).

Back in October, I was able to attend [Python Brasil](http://2017.pythonbrasil.org.br), the national conference about Python, during which I stayed in an accomodation with other PyLadies and allies. I used this opportunity to share what I had developed so far and to get some feedback. That's how I learned about pudb and how to use it to debug my code (and find out where I was getting the Github Issues API wrong). Because I found it so useful, on my Pull-Request, I proposed it to be added to the project, to help with future development. I also started adding some tests and wrote some specifications as suggestions to anyone who keeps working on it.

I would like take this opportunity to thank you to the friends who pointed me in the right direction during the application process and made this internship a reality to me, in particular Elias Dorneles.
