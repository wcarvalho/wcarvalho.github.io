---
title: Sublime-like edits in Jupyter Notebook
layout: post
comments: true
category: tutorial
tags: [software]
---

I've found some conflicting information online regarding getting sublime-like edits (e.g. ctrl+D selecting the next instance of what's selected) so I thought I'd post what's worked for me as recently today (September 18th, 2017)

1. Navigate to `~/.jupyter/custom/` (create it if it doesn't exist)
2. Open `custom.js` (also create if it doesn't exist)
3. Paste the following:

{% highlight ruby %}
require(["codemirror/keymap/sublime", "notebook/js/cell", "base/js/namespace"],
    function(sublime_keymap, cell, IPython) {
        // setTimeout(function(){ // uncomment line to fake race-condition
        cell.Cell.options_default.cm_config.keyMap = 'sublime';
        var cells = IPython.notebook.get_cells();
        for(var cl=0; cl< cells.length ; cl++){
            cells[cl].code_mirror.setOption('keyMap', 'sublime');
        }
    } 
);
{% endhighlight %}


Feel free to comment more optimal or up to date methods. 

Cheers :)