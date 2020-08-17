Title: My notes on Moin Moin
Date: 2017-12-31 00:49
Modified: 2017-01-18 18:49
Category: blog
Tags: personal, outreachy, development, moinmoin-wiki
Slug: my-notes-on-moin-moin
Authors: Renata
Summary: Appointments from my work

Below are just some appointments that I had made while working/studying MoinMoin wiki in December.

### Just download and install it?
Downloading [MoinMoin Wiki](https://moinmo.in/MoinMoinDownload) comes with a very nice message saying: 'You also need to apply this bugfix patch, sorry.' Which meant nothing to me, because I had never applied a patch before. And, really, that is not very welcoming to new people, it makes me wonder why couldn't they just provide a final corrected version of the code for instalation? But, anyway, I had to learn how to do that.

### Applying a patch on GNU/Linux
At first, I had a bit of trouble trying to figure out what 'applying a patch' meant in practical terms (what I had to do to apply them). I had *created a patch* before, when contributing to some translations, but I had never *applied a patch*.

I searched online for a bit and... it ended up not being as difficult as it sounds (but it would be so much easier *not having to do it to begin with*). First of all, I had to find the 'raw commit' on the link provided and download the file to the moinmoin directory. Not only that, but this file should be saved with a .diff extension, for instance: **patch_file.diff**.

Then, inside the directory the command patch should be used:


```
patch -p1 < patch_file.diff

```

And done! Patch applied to all the four files.

### Categories
From my understanding, to use EventCalendar, at least a page inside a category had to be created.

> To insert an event, insert the event information in any pages of specified category (CategoryEventCalendar by default). [https://moinmo.in/MacroMarket/EventCalendar](EventCalendar)

That meant I had to play a bit with MoinMoin and get familiarized on how to use it. Sure, I had used a wiki before (Wikipedia and, as I mentioned in another post, ikiwiki). I spend a whole day just doing that, learning how to create new categories on this wiki and creating new pages, inserting the new pages in a category, listing them and such. Was CategoryCategory a thing? Should I just write EventCalendar or CategoryEventCalendar? This last one won, because that seems to be the pattern for the MoinMoin website itself.

### Still on Macros
A macro is entered as wiki markup and it processes a few parameters to generate an output, which is displayed in the content area.

MoinMoin allows two types of macros:

* [Standard macros](https://moinmo.in/HelpOnMacros)
Standard macros are macros which code comes with MoinMoin code. They are ready to use.

> Macros reside in MoinMoin/macro and data/plugin/macro.

> The macro object can access the following objects:

> macro.request (see MoinMoin/request)

> http://hg.moinmo.in/moin/1.8?f=-1;file=MoinMoin/request

> macro.formatter (see MoinMoin/formatter for API)

> http://hg.moinmo.in/moin/1.8?f=-1;file=MoinMoin/formatter

> macro.formatter.page (see MoinMoin/Page.py)

> http://hg.moinmo.in/moin/1.8?f=-1;file=MoinMoin/Page.py

> Macros should use macro.formatter to create the output and return it.

That makes sense, now. [EmbedContent](https://moinmo.in/MacroMarket/EmbedContent?action=AttachFile&do=view&target=EmbedContent.py) uses this macro.formatter and EventCalendar uses it as well. This is called when the macro is executed (on EventCalendar, it calls a setglobalvalues function and uses global variables to it).

* [Macros from the macro market](https://moinmo.in/MacroMarket/)
This is the place to find new macros - and to publish macros developed by the community. There are some guidance for developers, talking about security and documentation, not to mention on how to publish there (create a wiki page).

Macros from the macro market have to be downloaded and put on the correct directory where MoinMoin wiki is installed to work. I noticed that, for some reason, wget can't be used to download the .py file with the macro code, which sucks when you're using just a terminal on a server.
