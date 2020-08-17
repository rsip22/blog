Title: Working with git branches was the best decision I made
Date: 2018-02-27 00:00
Modified: 2018-02-27 00:00
Category: blog
Tags: personal, outreachy, git, development, for beginners, git basics
Slug: git-branch-the-best-decision-I-made
Authors: Renata
Summary: A short story about how chosing to use git branches saved me from some trouble

This is a short story about how chosing to use git branches saved me from some trouble.

### How did I decide to use a new branch?
Up until certain point, I was just commiting all the code (and notes) I wrote into the master branch, which is the default for Git. No big deal, if I broke something, I could just go back and revert one or more commits and it would be okay.

It got to the point, though, that I would have send the code to people other than the mentors who had been seeing me breaking things: I would have to submit it for other developers to test it. While a broken code was the ideal for my mentors to see and help me in figuring out how to fix it, that wouldn't be useful for people seeing it in production and giving me feedback and suggestions for improvement. I had to send to them a good code that worked, and I had to do that while I worked on the last functionality needed, which is the recurrence rule for events.

After working on the recurrence rule for a few hours I realized that, since it wasn't really functional yet, I couldn't simply commit it on top of the rest of the code that had already been commited/published. Sure, I could have commented the function and commited the code that way, but it would be just too much trouble to have to comment/uncomment it every time I would work on that part.

That is how I chose to create a new git branch instead and starting commiting there the changes I had made.

I created a new branch called "devel" and asked git to change to it:

```
git checkout -b devel
```

Then, I did a "git status" to check everything was as expected and the branch had been changed to devel:
```
git status
renata@debian:~/foss_events$ git status
On branch devel
```

Next: staging the files and [creating the commit](https://git-scm.com/docs/git-commit):
```
git add --all .
git commit -m "COMMENTS FOR THE COMMIT"
```

Because the branch was created on my local machine, if I straight out try to just push the code upstream, it will give an error, because there is no "devel" branch on Github yet. So let's give some arguments to the git push command, asking it to set an upstream branch in the origin, which will receive the code:

```
git push --set-upstream origin devel
```

### How did this save me from some trouble?

Simply because, before I sent the code to the moin-devel list, I decided to clean out the repository of the old and repeated code... by deleting those files. I wanted to do that so anyone who came to try it out would be able to spot the macro easily and not to worry whether the other files had to be installed anywhere for the code to work.

Once I had deleted those files using rm -r on the command line and right before I commited, I did a "git status" to check if the delete action had been recorded... that was when I noticed that I was still on the devel branch, and not on the master branch, where I wanted this change to take place! My development branch *should* stay the mess it was because it was stuff I used to try out.

I had used "rm -r", though, so how did I get those files back to the devel branch? I mean, the easy way, not the downloading-the-repo-again way.

Simple! I would have to **discard** the changes (deletes) I had made on the devel branch and change to the master branch to do it again:

**BE CAREFUL, THIS COMMAND WILL DISCARD ANY CHANGES YOU HAVE MADE WHILE WORKING ON THE CURRENT BRANCH**

```
git checkout -f
```

This will throw away the changes. Then, it's possible to move back to the master branch:

```
git checkout master
```

And, yup, I'm totally writing this article for future reference to myself.

### Read more
 - [Understanding the GitHub Flow · GitHub Guides](https://guides.github.com/introduction/flow/)
