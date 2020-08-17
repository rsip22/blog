Title: Exporting EventCalendar data to ical
Date: 2018-02-07 14:49
Modified: 2018-02-07 14:00
Category: blog
Tags: outreachy, development, icalendar, eventcalendar, moinmoin-wiki
Slug: exporting-eventcalendar-data-to-ical
Authors: Renata
Summary: An update on my work on the EventCalendar macro

I have been working on the EventCalendar code, to allow to export the events' data to icalendar.

### A new cal_action
I started by creating a new cal_action (ical) that would call the function I created, download_events_ical(). I added it to the bottom menu of the calendar, along with with other views (Weekly, Daily, Simple) that also use cal_action to return the calendar.

![Wiki page showing the calendar, with the 'ical' link at the bottom]({static}/img/eventcalendar_with_ical_menu.png)

Afterwards, discussing it with my mentors, we figured out that this could be improved by always offering the .ics file as an attachment to the page.

Either way, no matter if we decide to leave just the link at the bottom or put it up as an attachment, or both, the file must be properly constructed with the data gathered by EventCalendar from the wiki pages with event data. This is what I'm working on this past week.

### Setting the headers
The 'download' or opening the icalendar file directly in the calendar application should happen automatically once the proper headers are set, so I had to specify the Content-Type that will be returned for the 'download ical' request.

A bug error page with code that actually showed me how to do that in moinmoin: [EditorContentTypeHttpHeader](https://moinmo.in/MoinMoinBugs/EditorContentTypeHttpHeader)

Now the browser knows that this file should be opened by a software that handles calendars (this immediately prompts the open/save dialog in browsers).

### Debugging
To parse the data, I investigated the EventCalendar variables that had the event data stored.

I knew there was a function loadEvents() already written in the code, that could unpack to dictionary variables (events, cal_events, labels) the info about the events. I needed to see how this data was constructed to figure out how to use it for the icalendar elements. With a print command, I ended up with this:

```
Events: {
    u'e_Workshops_2': {
        'date_len': 1,
        'startdate': u'20180124',
        'time_len': 0,
        'enddate': u'20180124',
        'description': u'workshop test',
        'recur_freq': 0,
        'title': u'workshop',
        'clone': 0,
        'recur_type': '',
        'label': '',
        'recur_until': '',
        'bgcolor': u'#000000',
        'hid': 'head-f5e173288ca20abb0a37e74aa035e6bbedc3e6ff-2',
        'starttime': '',
        'endtime': '',
        'id': u'e_Workshops_2',
        'refer': u'Workshops'
    },
}
```

Which shows that each 'events' item is an unicode object (e_Workshops_1, e_Conferences_1...) that contains another dictionary.

In Python, dictionaries may be interacted with using the values method. So that is what I did, and, for each value, I called a make_todo function that would create a [VTODO](https://en.wikipedia.org/wiki/ICalendar#To-do_(VTODO)). But scratch that. Even though I indeed created a 'to-do', that isn't what I *should have* created - I realize that as I write this post. We are talking about events, so I should've created a  [VEVENT](https://en.wikipedia.org/wiki/ICalendar#Events_(VEVENT)) component, as needed for icalendar format. I'm going to begin rectifying this as soon as I finish this post.


### Next steps
As it is now, the cal_event does allow to download a file... but the file returned is an html page from the wiki, with the icalendar element inserted in it. This isn't what we need. We need just the icalendar file to be returned, no HTML, and certainly not the wiki page, so it can be understood properly by the calendar software/application.

This is caused both by how MoinMoin works and by the macro code itself. When the EventCalendar macro executes, it appends it's result to the page html. I thought for a bit that if this append didn't happen, the return result would be an empty page and that this might allow our .ics file 'take over', so I kept thinking of turning the download_ical function into a whole new macro which uses EventCalendar data, but MoinMoin doesn't actually work like that.

I have found a macro called [Format Converter](https://moinmo.in/MacroMarket/FormatConverter) that 'allows instant single-file conversions from various input formats into various output formats'. Maybe icalendar could be added to it and that would solve the problem? If that so, anyone who wanted to use EventCalendar with the capacity to export to .ics, would need to install this macro as well. Doesn't seem like the most appopriate way to solve this. Maybe just copying part of FormatConverter to EventCalendar could work.

I'm still investigating the issue of returning the file with my mentors. We will see how that works out.

## Some thoughts
I remember how I thought it would be "simple", developing this functionality to the EventCalendar macro. Now I see that it is anything but simple, specially because of how much of MoinMoin wiki internals I have to learn in order to do so (and that is just a fraction of the whole system). If I didn't have mentors who patientily help me during the whole process (special thanks to Bruno!) and if I wasn't being paid for the time I spend learning all this - if I was just doing this on my own for the sake of doing it, it's very probable that I would have given up trying to contribute to this complex project a while ago. I'm very glad that [Outreachy](https://outreachy.org) came along and it's enabling this work - and my technical and personal growth.

By the way, for anyone that might be interested, I have been commiting the changes to the macro to the EventCalendar-099.py file on my [foss_events Github repository](https://github.com/rsip22/foss_events/blob/master/EventCalendar-099b.py). I warn you that it is kind of messy because I leave there things I use to debug and things that I think might be useful.

### Bonus: how to download attachments from MoinMoin using curl
I was bummed that I couldn't download the macro .py files using the terminal, it always gave me 403 (Forbidden) and returned HTML. I talked about this with my mentor Bruno and... there is actually a way! It turns out that the '&' character in the URL probably confuses wget and curl, so we use quotes for the address and... it works!

```
curl 'https://moinmo.in/MacroMarket/FormatConverter?action=AttachFile&do=get&target=FormatConverter-1.0.py …' --output http://FormatConverter.py
```
I'm still curious to see if this won't be a problem when specifying the URL to download the .ics file using Thunderbird.
