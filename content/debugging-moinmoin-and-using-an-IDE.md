Title: Debugging MoinMoin and using an IDE
Date: 2018-02-14 17:19
Modified: 2018-02-14 18:00
Category: blog
Tags: personal, outreachy, development, eclipse, python, moinmoin-wiki
Slug: debugging-moinmoin-and-using-an-IDE
Authors: Renata
Summary: How using an IDE helped me to debug

### Debugging
When I was creating the cal_action, I didn't quite know how to debug MoinMoin. Could I use pudb with the wiki? I wasn't sure how. To figure out if the code I was writing worked, I ended up consulting the error logs from Apache. It sort of worked, but of course that was *very far* from the ideal. What if I wanted to check something that wasn't an error?

Well, MoinMoin supposedly has a logging module, that lives on ```moin-1.V.V/wiki/config/logging/```, but I simply couldn't get it to work as I wanted.

I searched some more and found a guide on [setting up Winpdb Source Level Debugger](https://moinmo.in/DebugWithWinpdb), but I don't use Windows (really, where is the GNU/Linux guide to debug?), so that didn't help. &#128557;

*But*... MoinMoin does offer a [guide on setting up a development enviroment with Eclipse](https://moinmo.in/EclipseDevelopmentEnvironment) that I ended up following.

### Using an IDE
Up until this point, most of the code I created in Python where simple scripts that could be ran and debugged in the terminal. I had used [IDLE](https://docs.python.org/2/library/idle.html) while I was taking the [Python para Zumbis](https://www.pycursos.com/python-para-zumbis/) (Python for Zombies) course, but other than that, I just used a code editor (Sublime, then Vim and, finally, Atom) when programming in Python.

When I was taking a tech vocational course, I used Eclipse, an [Integrated development environment, or IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) to code in Java, but that was it. After I passed the course and didn't need to code in Java again, I simply let go of the IDE.

As it turns out, going back to Eclipse, along with the [PyDev plugin](http://www.pydev.org/) - both free software - was what actually helped me in debugging and figuring my way around the MoinMoin macro.

The steps I had to take:

1. Install eclipse-pydev and it's dependencies using Synaptic (Debian package manager)
2. Define Python 2.7 as the interpreter in preferences
3. Create a new workspace
4. Create a new project
5. Import the installed MoinMoin into the new project
6. Configure the new wiki
7. Run wikiserver.py

To develop the plugins (macro and actions):

1. Create a new workdir for the Plugins, that goes alongsite Moin
2. Copy the contents from the plugin directory of the wiki to the new directory

On step 2, though, instead of copying I just created a symbolic link to the files I had been working on that where in another directory. It would make no sense to have two copies of the same file in different places in the computer - besides, it would just complicate tracking what changes had been made ans where. To create a symbolic link:

```
$ ln -s PATH-TO-THE-ORIGINAL-FILE PATH-TO-THE-DESTINATION/FILE_ON_DESTINATION
```

More on [symbolic links](https://wiki.debian.org/SymLink) can be found using the command ```man ln``` on Debian's terminal.

With the Eclipse console, I could use ```print help(request)``` to figure out what methods would be available to me with the request provided by the macro. With this, I finally began to figure out how to create the response we want (without returning the whole wiki page with it, just the event information in the icalendar format).

![Eclipse IDE running the wikiserver.py from MoinMoin and showing the debug output in a terminal]({static}/img/moin_with_eclipse.png)

If you don't know what I mean with request/response: in simple terms, when you click something on a webpage (for instance, my ical link in the bottom of the calendar) in your internet browser, you are *requesting* a resource (the icalendar file). It's up to the server to *respond* with the appropriate resource (the file) or with an status code explaining why it can't fulfill your request (for instance, you get an 404 error when the page - resource - you're trying to access - *requesting* - can't be found).

![A simplified diagram of a static web server showing the request-response cycle.](https://mdn.mozillademos.org/files/13841/Basic%20Static%20App%20Server.png)

Here you can find more information on [client-Server overview, by Mozilla web docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Client-Server_overview).

So now I'm working on constructing that response. Thanks to the Eclipse console, now I know that just trying to use the response.write() method with the return value of my method I get a ```TypeError: Expected bytes```. I will probably have to transform the result of the method to generate the icalendar into bytes instead of InstanceClass. Well, at least I can say that the choices that have been made when writing the ExportPDF macro come to me more clearly now.
