Title: Not being perfect
Date: 2018-01-17 17:49
Modified: 2018-01-17 17:49
Category: blog
Tags: personal, outreachy, development, moinmoin-wiki
Slug: not-being-perfect
Authors: Renata
Summary: Things might not work out as we expect them to


I know I am *very* late on this update (and also very late on emailing back my mentors). I am sorry. It took me a long time to figure out how to put into words everything that has been going on for the past few weeks.

Let's begin with this: yes, I am so very aware there is an evaluation coming up (in two days) and that it is important "to have at least one piece of work that is visible in the week of evaluation" to show what I have been doing since the beginning of the internship.

But the truth is: as of now, I don't have any code to show. And what that screams to me is that it means that I have failed. I didn't know what to say either to my mentors or in here to explain that I didn't meet everyone's expectations. That I had not been perfect.

So I had to ask what could I learn from this and how could I keep going and working on this project?

Coincidence or not, I was wondering that when I crossed paths (again) with one of the most amazing TED Talks there is:

[Reshma Saujani's "Teach girls bravery, not perfection"](https://www.ted.com/talks/reshma_saujani_teach_girls_bravery_not_perfection)

And yes, that could be me. Even though I had written down almost every step I had taken trying to solve the problem I got stuck on, I wasn't ready to share all that, not even with my mentors (yes, I can see now how that isn't very helpful). I would rather let them go thinking I am lazy and didn't do anything all this time than to send all those notes about my failure and have them realize I didn't know what they expected me to know or... well, that they'd picked the wrong intern.

### What was I trying to do?
As I talked about in my [previous post](/blog/my-project-with-outreachy), the EventCalendar macro seemed like a good place to start doing some work. I wanted to add a piece of code to it that would allow to export the events data to the iCalendar format. Because this is sort of what I did in [my contribution for the github-icalendar](/blog/my-contribution-to-github-icalendar)) and because the mentor Daniel had suggested something like that, I thought that it would be a good way of getting myself familiarized to how macro development is done for MoinMoin wiki.

### How far did I go?
As I had planned to do, I started by studying the EventMacro.py, to understand how it works, and taking notes.

EventMacro fetches events from MoinMoin pages and uses Python's [Pickle module](https://docs.python.org/2/library/pickle.html) to serialize and to de-serialize the data. This *should be* okay if you can trust enough the people editing the wiki (and, therefore, creating the events), but this might not be a good option if we start using external sources (such as third-party websites) for event data - at least, not directly on the data gathered. See the warning below, from the Pickle module docs:

```
Warning: The pickle module is not secure against erroneous or maliciously constructed data. Never unpickle data received from an untrusted or unauthenticated source.
```
From the code and from the inputs from the mentors, I understand that EventMacro is more about *displaying* the events, putting them on a wiki page. Indeed, this could be helpful later on, but not exactly for the purpose we want now, which is to have some standalone application to gather data about the events, model this data in the way that we want it to be organized and maybe making it assessible by an API and/or exporting as JSON? *Then*, either MoinMoin or any other FOSS community project could chose how to display and make use of them.

### What did go wrong?
But the thing is... even if I had studied the code, I couldn't see it running on my MoinMoin instance. I have tried and tried, but, generally speaking, I got stuck on trying to get macros to work. Standard macros, that come with MoinMoin, work perfectly. But macros from MacroMarket, I couldn't find a way to make them work.

For the EventCalendar macro, I tried my best to follow the instructions on the [Instalation Guide](https://moinmo.in/MacroMarket/EventCalendar#Installation_Guide) but I simply couldn't find a way for it to be processed.

Things I did:

* I downloaded the macro file and renamed it to EventCalendar.py
* I put it in the local macro directory (yourwiki/data/plugins/macro) and proceeded with the rest of the instructions.
* When that didn't work, I copied the file to the global macro directory (MoinMoin/macro), it wasn't enough.
* I made sure to [add the .css](https://moinmo.in/MacroMarket/EventCalendar?action=AttachFile&do=view&target=eventcal-096.css) to all styles, both for common.css and screen.css, still didn't work.
* I thought that maybe it was the arguments on the macro, so I tried to add it to the wiki page in the following ways:

```
<<EventCalendar>>

<<EventCalendar(category=CategoryEventCalendar)>>

<<EventCalendar(,category=CategoryEventCalendar)>>

<<EventCalendar(,,category=CategoryEventCalendar)>>
```

Still, the macro wasn't processed and appeared just like that on the page, even though I had already created pages with that category and added event info to them.

To investigate, I tried using other macros:

- [Hits](https://moinmo.in/HelpOnMacros), a System Information macro

- [MonthCalendar](https://moinmo.in/HelpOnMacros/MonthCalendar)

- [ShowSmileys](https://moinmo.in/macro/ShowSmileys.py)

These all came with the MoinMoin core and they all worked.

I tried other ones:

- [SiteIndex](https://moinmo.in/MacroMarket/SiteIndex)

- [EmbedContent](https://moinmo.in/MacroMarket/EmbedContent)

That, just like EventCalendar, didn't work.

Going through these macros also made me realize how awfully documented most of them usually are, in particular about the instalation and making it work with the whole system, even if the code is clear. (And to think that at the beginning of this whole thing I had to search and read up on what are [DocStrings](https://www.python.org/dev/peps/pep-0257/) because the [MoinMoin Coding Style](https://moinmo.in/CodingStyle) says: "That does NOT mean that there should be no docstrings.". Now it seems like some developers didn't know what DocStrings were either.)

I checked permissions, but it couldn't be that, because the downloaded macros has the same permissions as the other macros and they all belong to the same user.

I thought that maybe it was a problem with Python versions or even with the way MoinMoin instalation was done. So I tried some alternatives. First, I tried to install it again on a new CodeAnywhere Ubuntu container, but I still had the same problem.

I tried with a local Debian instalation... same problem. Even though Ubuntu is based on Debian, the fact that macros didn't work on either was telling me that the problem wasn't necessarily the distribution, that it didn't matter which packages or libraries each of them come with. The problem seemed to be somewhere else.

Then, I proceeded to analyze the Apache error log to see if I could figure out.

```
[Thu Jan 11 00:33:28.230387 2018] [wsgi:error] [pid 5845:tid 139862907651840] [remote ::1:43998] 2018-01-11 00:33:28,229 WARNING MoinMoin.log:112 /usr/local/lib/python2.7/dist-packages/MoinMoin/support/werkzeug/filesystem.py:63: BrokenFilesystemWarning: Detected a misconfigured UNIX filesystem: Will use UTF-8 as filesystem encoding instead of 'ANSI_X3.4-1968'

[Thu Jan 11 00:34:11.089031 2018] [wsgi:error] [pid 5840:tid 139862941255424] [remote ::1:44010] 2018-01-11 00:34:11,088 INFO MoinMoin.config.multiconfig:127 using wiki config: /usr/local/share/moin/wikiconfig.pyc
```
Alright, the wikiconfig.py wasn't actually set to utf-8, my bad. I fixed and re-read it again to make sure I hadn't missed anything this time. I restarted the server and... nope, macros still don't work.

So, misconfigured UNIX filesystem? Not quite sure what was that, but I searched for it and it seemed to be easily solved generating an en_US.UTF-8 [Locale](https://wiki.debian.org/Locale) and/or setting it, right?

Well, these errors really did go away... but even after restarting the apache server, those macros still wouldn't work.

So this is how things went up until today. It ends up with me not having a clue where else to look to try and fix the macros and make them work so I could start coding and having some results... or does it?

### This was a post about a failure, but...
Whoever wrote that "often times writing a blog post will help you find the solution you're working on" on the e-mail we received when we where accepted for Outreachy... *damn*, you were right.

I opened the command history to get my MoinMoin instance running again, so I could verify that the names of the macros that worked and which ones didn't were correct for this post, when...

*I cannot believe I couldn't figure out.*

What had been happening all this time? Yes, the .py macro file should go to moin/data/plugin/macro, but not on the directories I was putting them. I didn't realize that all this time, the wiki wasn't actually installed on the directory yourwiki/data/plugins/macro where the extracted source code is. It is installed on /usr/local/share/, so the files should be put on /usr/local/share/moin/data/plugin/macro and *of course* I should've realized this sooner, after all, I was the one to install it, but... it happens.

I copied the files there, set the appropriate owner and... IT-- WORKED!

![Mozilla Firefox screenshot showing MoinMoin wiki with the EventCalendar plugin working and displaying a calendar for January 2018]({static}/img/eventcalendar_working.png)
