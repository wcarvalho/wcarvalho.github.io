---
title: "Highlights: A markdown pdf annotator"
comments: true
layout: post
category: misc
tags: [tutorial software]
---


It's getting close to the end of the day and I don't feel like doing work-work, so I've decided to do some pseudo-work and write this little blog post recommending a phenomenal pdf annotator I recently discovered: [Highlights](http://highlightsapp.net/). 

<img class="regular materialboxed responsive-img" src="http://highlightsapp.net/img/highlightsapp_yosemite2.jpg">


## TL; DR

[Highlights](http://highlightsapp.net/) saves annotatations as editable markdown and let's you  effortlessly export the markdown to evernote, which then makes your notes searchable on google (only to you).

## Full Story

I wanted a system where I could easily access the annotations I made on pdfs. I wanted them to be accessible across pdf readers so the annotations needed to be saved to the file and I wanted them to be easily found when I searched for related topics. [Highlights](http://highlightsapp.net/) combined with [Evernote](https://evernote.com/) managed to accomplish both rather easily and elegantly

I'll try to keep it to the "facts". To *highlight* the utility of [Highlights](http://highlightsapp.net/) (hehe), I will use my annotations on this pdf, [Tutorial on Variational Autoencoders](https://arxiv.org/pdf/1606.05908v2.pdf), as an example.



### Pros

1. The annotations are saved in markdown. The impact is two-fold. (1) They are easy to edit, (2) It is easy to export to many clients **including Evernote**.
2. Evernote has a cool feature that when you search things on google, you can concurrently perform a search on evernote. Below you can see an example where I searched for hidden variables and 2 notes with related text came up (one of which was my markdown notes from this example)

   <img class="regular materialboxed responsive-img" src="{{ site.baseurl }}/files/highlights/evernote_google.png">

3. The annotation tools are powerful
* Aside from text, you can also "highlight" diagrams, adding them to your markdown
* You can set a specific underline color for references and your markdown will correclty link references

   <table>
      <tr>
      <th>Regular View</th>
      <th>Markdown View</th>
      </tr>
      <tr>
      <td>
         <img class="regular materialboxed responsive-img" src="{{ site.baseurl }}/files/highlights/view.png">
      </td>
      <td>
         <img class="regular materialboxed responsive-img" src="{{ site.baseurl }}/files/highlights/markdown.png">
      </td>
      </tr>
   </table>

4. Everything is saved in-file so you can view your pdf (and all annotations) in other readers. This was important to me. I use [Papers](http://papersapp.com/mac/) to manage my papers, and being able to browse my annotations on that platform (or any other) is really useful.

   <img class="regular materialboxed responsive-img" src="{{ site.baseurl }}/files/highlights/papers.png">

5. It's extremely easy to change the color/type of any annotation or add text to any placed not

   <img class="regular materialboxed responsive-img" src="{{ site.baseurl }}/files/highlights/ease.png">


### Half-Pros/Half-cons:
1. It is supposed to support DOI lookup so that references are clickable and openable, but I have found this feature to not work.
2. If you use bookends or paper3 (I used papers), it supports opening the reference in your manager (but, again, this require DOI lookup to work)

### Cons:
1. It costs $30 but its made by a PhD student so I'm happy to support (for those that don't want to, it isn't too hard to find a copy online...)

---

Here are some examples of markup and pdf it generated from my annotations

* [markup]({{ site.baseurl }}/files/highlights/markup.md)
* [pdf]({{ site.baseurl }}/files/highlights/pdf.pdf)
