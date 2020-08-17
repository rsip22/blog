Title: Pushing a commit to a different repo
Date: 2018-03-23 00:49
Modified: 2018-03-23 00:49
Category: blog
Tags: personal, git, github, djangogirls
Slug: pushing-a-commit-to-a-different-repo
Authors: Renata
Summary: How to push a commit to a different repo

![Photo taken from the top of a hill, overlooking light green ocean beaches]({static}/img/trilha_da_galheta_florianopolis.JPG)

*View from the Barra-Galheta beach trail, in Florianopolis, Brazil*

My Outreachy internship with Debian is over. I'm still going to write an article about it, to let everyone know what I worked on towards the ending, but I simply didn't have the time yet to sit down and compile all the information.

As you might or might not have noticed, right after my last Outreachy activity, I sort of took a week off in the beach. \o/

![Renata's picture, a white woman sitting on the grass, overlooking the beach below. She pets a brown stray that sits next to her]({static}/img/renata_with_dog.JPG)

*Mila, a cute stray dog that accompanied us during a whole trail*

For the past weeks, I've also been involved in the organization of three events (one of them was a [Debian Women meeting in Curitiba](https://debianwomenbr.github.io) that took place two Saturdays ago and another one is [Django Girls Porto Alegre](https://djangogirls.org/portoalegre/), which starts tonight). Because of this last one, I was reviewing their [Brazilian Portuguese tutorial](https://tutorial.djangogirls.org/pt) and adding some small fixes to the language. After all, we are talking to women who read the tutorial during the workshop, so why all the mentions to programmers and hackers and such should mention the male counterpart in Portuguese? Women program, too!

When I was going to commit my fixes, though, I got an error:

```
remote: error: GH006: Protected branch update failed for refs/heads/master.
To https://github.com/DjangoGirls/tutorial
! [remote rejected]   master -> master (protected branch hook declined)

```

Oops?

Yup, as it so happens more often than not, I forgot to fork the repository before starting to change the files! I just did 'git clone' straight to Django Girls' tutorial repository. But, since I had already done all the steps towards the commit, what could I do to avoid losing the changes? Could I just push this commit to another repository of my own and try and open a Pull Request to DjangoGirls/tutorial?

Of course I had to go and search for that. Isn't that what all programmers do? Go and find someone else who already had the same problem they have to try and [find a solution](https://stackoverflow.com/questions/15616133/pushing-a-commit-from-one-repository-into-another-repository)?

Quick guide to the solution I've found:

- Fork the original repository to my collection of repos (on Github, just clicking 'Fork' will do).

- Get the branch and the id of the commit that had been created. For instance, on this case:

```
[master 4d314550] Small fixes for pt-br version

```

The branch is: master

The id is: 4d314550

- Use the URL for the new repository (your fork), the branch and the commit id for a new git push command, like this:

```
git push URL_FOR_THE_NEW_REPO commit_id:branch

```

Example with my repo:
```
git push https://github.com/rsip22/tutorial 4d314550:master

```

And this was yet another article for future reference.
