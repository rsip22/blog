Title: Chosing a system for the blog
Date: 2017-11-26 10:00
Modified: 2267-11-01 10:00
Category: blog
Tags: development, outreachy, python, pelican
Slug: chosing-a-system-for-the-blog
Authors: Renata
Summary: How I ended up developing this blog using Pelican


This blog was created because I am supposed to report my journey through the [Outreachy internship](https://outreachy.org).

Let me start by saying that I'm biased towards systems that use flat files for blogs instead of the ones that require a database. It is so much easier to make the posts available through other means (such as having them backed up in a Git repository) that assure their content will live on even if the site is taken down or dies. It is also so much better to download the content this way, instead of pulling down a huge database file, which may cost a significant amount of money to transfer that amount of data. Having flat files with your content with a format that is shared among many systems (such as Markdown) might also assure a smooth transition to a new system, should the change become a necessity at some point.

<!-- more -->
I have experimented some options while working on projects. I played with [Lektor](https://getlektor.com) while contributing to [PyBeeWare](https://pybee.org/). I liked Lektor, but I found it's documentation severely lacking. I worked with [Grav](https://getgrav.org/) while we were working towards getting [tem.blog.br](https://github.com/temblog) back online. Grav is a good CMS and it is definitely an alternative to Wordpress, but, well, it needs a server to host it.

At first, I thought about using [Jekyll](https://jekyllrb.com/). It is a good site generator and it even has a [Code Academy](https://www.codecademy.com/learn/deploy-a-website) course on how to create a website and deploy it to Github Pages that I took a while ago. I could have chosen it to develop this blog, *but* it is written in Ruby. Which is fine, of course. The first steps I took into learning how to program were in Ruby, using [Chris Pine's Learn to Program](https://pine.fm/LearnToProgram/) | [versão pt-br](https://www.jmonteiro.com/aprendaaprogramar/). So, what is my objection with Ruby? It happens that I excpect most of the project I will develop during Outreachy will use Python (and maybe some Javascript) and I thought that adding a third language might make my life a bit harder.

That is how I ended up with [Pelican](https://blog.getpelican.com/). I had played a bit with it while contributing to the [PyLadies Brazil website](https://brasil.pyladies.com/). During Python Sul, the regional Python conference we had last September, we also had a sprint to make the [PyLadies Caxias do Sul website](https://pyladiescaxias.github.io/) using Pelican and hosting it with Github Pages. It went smoothly. Look how awesome it turned out:

![Image of the PyLadies Caxias do Sul website, white background and purple text]({filename}/img/pyladies_caxias_website.png)

So, how to do one of those? Hang on tight, that I will explain it in detail on my next post! ;)
