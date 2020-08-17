Title: My project with Outreachy
Date: 2017-12-20 02:20
Modified: 2017-12-20 02:20
Category: blog
Tags: outreachy, development, moinmoin-wiki
Slug: my-project-with-outreachy
Authors: Renata
Summary: The start of my Outreachy internship

Let's get to the project I actually applied to:

## To build a calendar for FOSS events

We have a page on Debian wiki where we centralize the information needed to make that a reality, you can find it here: [SocialEventAndConferenceCalendars](https://wiki.debian.org/SocialEventAndConferenceCalendars)

So, in fact, the first thing I did on my internship was:

* Search for more sources for FOSS events that hadn't been mentioned in that page yet

* Update said page with these sources

* Add some attributes for events that I believe could be useful for people wanting to attend them, such as:
    - Is the registration (and not just the CFP) still open?
    - Does the event has a code of conduct?
    - What about accessibility?

I understand that some of these informations might not be readily available for most of the events, but maybe the mere act of mentioning them in our aggregation system may be enough to an organizer to think about them, if they aim to have their event mentioned "by us"?

Both my mentor, Daniel, and I have been looking around to find projects that have worked on a goal similar to this one, to study them and see what can be learned from what has been done already and what can be reused from it. They are mentioned on the wiki page as well. If you know any others, feel free to add there or to let us know!

Among the proposed deliverables for this project:

* making a plugin for other community web sites to maintain calendars within their existing web site (plugin for Discourse forums, MoinMoin, Drupal, MediaWiki, WordPress, etc) and export it as iCalendar data
* developing tools for parsing iCalendar feeds and storing the data into a large central database
* developing tools for searching the database to help somebody find relevant events or see a list of deadlines for bursary applications

My dear mentor Daniel Pocock suggested that I considered working on a plugin for [MoinMoinWiki](https://moinmo.in/MoinMoinWiki), because Debian and FSFE use MoinMoin for their wikis. I have to admit that I thought that was an awesome idea as soon as I read it, but I was a bit afraid that it would be a very steep learning curve to learn how MoinMoin worked and how I could contribute to it. I'm glad Daniel calmed my fears and reminded me that the mentors are on my side and glad to help!

So, what else have I been doing?

So far? I would say studying! Studying documentation for MoinMoin, studying code that has already been written by others, studying how to plan and to implement this project.

And what have I learned so far?

## What is MoinMoin Wiki?

![MoinMoin logo, sort of a white "M" inside a circle with light blue background. The corners of the M are rounded and seem connected like nodes]({static}/img/Moinmoin.png)

MoinMoin is a wiki written in... Python (YAY! \o/). Let's say that I have... interacted with development on a wiki-like system back when I created my first (and now defunct) blog post-Facebook.

![Ikiwiki logo, the first 'iki' is black and mirrors the second one, with a red 'W' in the middle]({static}/img/ikiwiki.png)

[Ikiwiki](https://ikiwiki.info/) was written in Perl, a language I know close to nothing about it, which limited a lot how I could interact with. I am glad that I will be able to work with a language that I am way more familiarized with. (And, on Prof. Masanori's words:  "Python is a cool language.")

I also learned that MoinMoin's storage mechanism is based on flat files and folders, rather than a database (I swear that, despite [my defense for flat file systems](/chosing-a-system-for-the-blog), this is a coincidence. I mean, if you believe in coincidences). I also found out that the development uses [Mercurial](https://www.mercurial-scm.org/) for version control. I look forward to learning exploring it, because so far I have only used git.

The past few days I set up a local MoinMoin instance. Even though there is [a HowTo guide](https://moinmo.in/HowTo/Debian8) to get MoinMoinWiki working on Debian, I had a little trouble setting it up using it. Mostly because the guide is sort of confusing with permissions, I think? I mean, it says to create a new user with no login, but then it gives commands that can only be executed by root or sudo. That doesn't seen very wise. So I went on and found [a docker image for MoinMoin wiki](https://hub.docker.com/r/olavgg/moinmoin-wiki/) and was able to work on MoinMoin with it. This image is based on Debian Jessie, so maybe that is something that I might work to improve in the future.

Only after I got everything working with docker that I found this [page with instructions for Linux](https://master19.moinmo.in/InstallDocs/QuickInstall#qdlinux) which was what I should've tried in the first place, because I didn't really needed fully configurated server with nginx and uwsgi, only a local instance to play with. It happens.

I studied the development guide for MoinMoin and I have also worked to understand the development process (and what Macros, Plugins and such are in this context), so I could figure out where and how to develop!

### *Macros*
> A macro is entered as wiki markup and it processes a few parameters to generate an output, which is displayed in the content area.

Searching for Macros, I found out there is a [Calendar Macro](https://moinmo.in/WikiCourse/21%20Macros). And I have discovered that, besides the Calendar Macro, there is also an [EventCalendar macro](https://moinmo.in/MacroMarket/EventCalendar) that was developed years ago. I expect to use the next few days to [study the EventCalendar code](https://moinmo.in/MacroMarket/EventCalendar?action=AttachFile&do=view&target=EventCalendar-099b.py) more throughly, but the first impression I had is that this code that can be reused and improved for the FOSS calendar.

### *Parsers*
> A parser is entered as wiki markup and it processes a few parameters and a multiline block of text data to generate an output, which is displayed in the content area.

### *Actions*
> An action is mostly called using the menu (or a macro) and generates a complete HTML page on its own.

So maybe I will have to work a bit on this afterwards, to interact with the macro and customize the information to be displayed? I am not sure, I will have to look more into this.

I guess that is all I have to report for now. See you in two weeks (or less)!
