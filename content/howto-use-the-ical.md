Title: How to use the EventCalendar ical
Date: 2018-02-21 19:49
Modified: 2018-02-21 19:49
Category: blog
Tags: personal, outreachy, development, moinmoin-wiki, icalendar, eventcalendar
Slug: howto-use-the-ical
Authors: Renata
Summary: A summary of the improvent to EventCalendar and how to use it

Hello!

If you follow this blog, you should probably know by now that I have been working with my mentors to contribute to MoinMoin EventCalendar macro, adding the possility to export the events' data to an icalendar file.

![A screenshot of the code, with the function definition for creating the ical file from events from the macro]({static}/img/create_ical.png)

The code ([which can be found on this Github repository](https://github.com/rsip22/foss_events/blob/master/macro/EventCalendar-099b.py)) isn't quite ready yet, because I'm still working to convert the recurrence rule to the icalendar format, but other than that, it should be working. Hopefully.


This guide assumes that you have the
[EventCalendar](https://moinmo.in/MacroMarket/EventCalendar) macro installed on the wiki and that the macro is called on a determined wikipage.

The icalendar file is now generated as an attachment the moment the macro is loaded. I created an "ical" link at the bottom of the calendar. When activated, this link prompts the download of the ical attachment of the page. Being an attachment, there is still the possibility to just view ical the file using the "attachment" menu if the user wishes to do so.

![Wiki page showing the calendar, with the 'ical' link at the bottom]({static}/img/eventcalendar_with_ical_menu.png)

There are two ways of importing this calendar on Thunderbird. The first one is to download the file by clicking on the link and then proceeding to import it manually to Thunderbird.

![Thunderbird screenshot, with the menus "Events and Tasks" and "Import" selected]({static}/img/events_and_tasks_import.png)

The second option is to "Create a new calendar / On the network" and to use the URL address from the ical link as the "location", as it is shown below:

![Thunderbird screenshot, showing the new calendar dialog and the ical URL pasted into the "location" textboxd]({static}/img/thunderbird_new_calendar_location.png)

As usual, it's possible to customize the name for the calendar, the color for the events and such...

![Thunderbird screenshot, showing the new calendar with it's events]({static}/img/ical_imported_to_thunderbird.png)

I noticed a few Wikis that use the EventCalendar, such as [Debian wiki](https://wiki.debian.org) itself and the [FSFE wiki](http://wiki.fsfe.org). [Python wiki](https://wiki.python.org/moin/PythonEventsCalendar#Python_Events_Calendar) also seems to be using MoinMoin and EventCalendar, but it seems that they use a Google service to export the event data do iCal.

If you read this and are willing to try the code in your wiki and give me feedback, I would really appreciate. You can find the ways to contact me in my [Debian Wiki profile](https://wiki.debian.org/RenataDAvila).
