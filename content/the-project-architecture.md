Title: Ideas for the project architecture and short term goals
Date: 2018-01-24 14:49
Modified: 2018-01-24 14:49
Category: blog
Tags: outreachy, outreachy, development, moinmoin-wiki
Slug: the-project-architecture
Authors: Renata
Summary: What we have considered so far and what lies ahead

There has been many discussions about planning for the FOSS calendar. On this post, I report about some of the ideas.

### How I first thought the Foss Events calendar

Back in december, when I was just making sense of my surroundings and trying to find a way to start the internship, I drawed this diagram to picture in my head how everything would work:

![A diagram showing the schema that will be described bellow. Each item is connected to the next using arrows, except for the relationship between user interface and API, where data flows both ways.]({static}/img/foss_events.jpg)

1. There would be a "crawler.py" module, which would access each site on a determined list (It could be Facebook, Meetup or any other site such as another calendar) that have events information. This module would pull the event data from those sites.

2. A validator.py would check if the data was good and *if there was* data. Once this module verified this, it would dump all info into a dirty_events database.

3. The dirty_events database would be accessed by the module parser.py, which would clean and organize the data to be properly stored in the events database.

4. An API.py module would query the events database and return the proper data, formatted into JSON, ical and/or some other formats.

5. There would be an user interface to get data from API.py and to display this data. It should also be possible to add (properly formatted) events to the database using this interface. [If we were talking about a plugin to merely *display* the events in MoinMoin or Wordpress or some other system, this plugin would enter in this category.]

### The ideas that Daniel put on paper

Then, when I shared with my mentors, Daniel came up with this:

![Another diagram. On the left, the plugins boxes, they connect to an aggregator, with input towards the storage. The storage then outputs to reports and data dump, represented on the right.]({static}/img/foss_events_daniel.jpg)

Daniel proposed that module or plugins could be developed or improved (there are some of them already, but they might not support iCalendar URLs) for MoinMoin, Drupal, Wordpress that would allow the data each of these systems have about events to be aggregated. Information from the Meetup and the Facebook APIs could be converted to ical to be agreggated. This aggregation process could happen through a cron job - and I believe *daily* is enough, because people don't usually publish an event to happen in the very next day (they need time for people to acknowledge it). If the time frame ends up not being the ideal, this can be reviewed and changed later.

Once all this data is gathered, it would then be stored, inserting it or updating it in what could be a PostgreSQL or NoSQL solution.

Using the database with events information, it should be possible to do a data dump with all the information or to give "reports" of the event data, whether the user wants to access the data in iCalendar format (for Thunderbird or GNOME Evolution) or just HTML for viewing in the browser.


### Short term goals

Creating a FOSS events calendar it is a big project that will most certainly continue beyond my Outreachy internship.

Therefore, along with my mentors, we have established that my short term goal will be to contribute a bit to it by working on the MoinMoin EventCalendar so the events can be exported to the iCalendar format.

I have been studying and playing around with the EventCalendar code and, so far, I've concluded that the best way to do this might be by writing a function to it. Just like there are other functions on this plugin to change the display of the calendar, there might be a function to just sort the data to the iCalendar format and to allow downloading the file.
