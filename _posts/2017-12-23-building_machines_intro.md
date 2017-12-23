---
title: Building Machines that Learn and Think Like People (pt 1. Introduction and History)
<!-- img: /files/writing/abyss.jpg -->
<!-- width: 75 -->
<!-- caption: My perfect world. -->
layout: post
comments: true
category: review
tags: [cognitive-science, deep-learning]
---
Note: ideas and opinions that are my own and not of the article will be in an <font color="grey"><em>italicized grey</em></font>.

# Series Table of Contents
[Part 1: Introduction and History]({{ site.baseurl }}/review/2017/12/23/building_machines_intro)<br>
[Part 2: Challenges for Building Human-Like Machines]({{ site.baseurl }}/review/2017/12/22/building_machines_challenges)<br>
[Part 3: Developmental Software]({{ site.baseurl }}/review/2017/12/22/building_machines_developmental)<br>
[Part 4: Learning as Rapid Model-Building]({{ site.baseurl }}/review/2017/12/22/building_machines_learning)<br>
[Part 5: Thinking Fast]({{ site.baseurl }}/review/2017/12/22/building_machines_thinking)<br>


### Article Table of Contents

| [Motivation for series](#personal-motivation-for-post) |
| [Introduction](#introduction) |
| [Historical Brain-Inspiration in AI](#historical-brain-inspiration-in-ai) |

## Motivation for series
### (Feel free to skip)
This is part 1 in a series of blog posts, where I plan to summarize the lengthy, but fascinating, [Building Machines that Learn and Think Like People](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/building-machines-that-learn-and-think-like-people/A9535B1D745A0377E16C590E14B94993) by Lake et al. This is a paper that discusses how current deep learning models, despite their success and common comparison to the brain, do not learn how brains do in many respects. The authors offer a set of "key ingredients" to endow neural networks with that might allow them to learn and think more like brains do.

I've wanted to read this paper for sometime. One of my central goals as an aspiring brain and machine learning researcher is to build human-inspired AI. As I'm very junior in the field, I thought this paper would give me a lot of insight into how to go about doing that. I was finally pushed into reading it when I discovered that along with this paper, the Journal for Behavioral and Brain Sciences has published 27 promising [commentaries](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/building-machines-that-learn-and-think-like-people/A9535B1D745A0377E16C590E14B94993#fndtn-related-commentaries)! Among the ones I'm most excited to read next are:

1. [Building machines that learn and think for themselves](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/building-machines-that-learn-and-think-for-themselves/E28DBFEC380D4189FB7754B50066A96F) by DeepMind 
2. [Building on prior knowledge without building it in](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/building-on-prior-knowledge-without-building-it-in/F342A14C57094D5AF7BC62950AE49CD8) by McClelland et al.
3. [Ingredients of intelligence: From classic debates to an engineering roadmap](https://www.cambridge.org/core/product/3D2A685AC198EC0008835514735033BB), a meta-response by Lake et al.


## Introduction

The purpose of this series is to highlight the challenges with building machines that learn and think like people. As such, I will skip aspects of the paper that generally review deep learning. Please feel free to read the paper for that material. The key idea: thanks to tremendous skill in pattern recognition, deep neural networks have achieved state-of-the-art performance in numerous domains including computer vision {% citbuilding_machines_intro %}, speech modeling, and complex control problems.

While neural networks perform very well on many tasks, they have limitations such as their requirement of large training sets and their inability to generalize knowledge well across tasks. This is, in part, because they (at least, in their current form) rely on stasticial pattern recognition. An alternative, which suggests is a key ingredient of human learning, is a model-building approach. They argue that intelligent cognition relies on building and using causal models to understand, explain, simulate, and predict the world. Despite this contrast, these two methods are certainly not orthogonal and machines can benefit from both, synergistically.

The authors maintain that while they are critical of neural networks, they see them as somewhat fundamental for human-like learning machines, as any computational model for human learning must ultimately be grounded in the brain's biological neural networks. However, the authors believe that future generations of neural networks will look very different from current state-of-the-art.

<font color="grey"><em>
  I support this as the neural networks we use are crude abstractions of our incomplete and incorrent models for biological neural networks.
  For example, physicists have recently found that neurons are not single excitable elements but a collection of excitable elements. Further, each excitable element is sensitive to the <strong>directionality</strong> of the origin of the input signal. This will potentially require a dramatic reformulation of artificial neural networks and will likely spur much research.
</em></font>

<br>
<strong>The main contribution of this paper is its suggestion of "key ingredients" for building machines that learn and think like people. </strong> Defining and motivating these ingredients makes up a majority of the paper, so I will make each broad category its own article in this series. The ingredients can broadly be categorized into 

* ["Developmental Software"]({{ site.baseurl }}/review/2017/12/22/building_machines_developmental): intuitive theories for the world that we learn at an early age such as theories of intuitive physics and intuitive psychology, 
* ["Model Building"]({{ site.baseurl }}/review/2017/12/22/building_machines_learning): the ability to build casual models of the world via methods such as compositionality and learning-to-learn, and 
* ["Thinking quickly"]({{ site.baseurl }}/review/2017/12/22/building_machines_thinking): the ability to quickly do inference and prediction by combining model-free and model-based algorithms.

## History of Brain-Inspiration in AI

Scientists such as Alan Turing have long thought that AI could be informative to or descriptive of cognition. In fact, Turing held a behaviorist view reminiscent to a popular modern view that almost anything can be learning from the statistical patterns of sensory inputs.

Cognitive scientists repudiated this view of cognition and instead assumed that human knowledge representation was symbolic in nature. They argued that many functions of cognition such as language and planning could be understood in terms of symbolic operations. This falls in line more with a "model-based" approach.

Somewhat complementary to both, another school of thought - and what would become the basis for deep learning - believed in sub-symbolic distributed representations of knowledge produced by parallel distributed processing (PDP) systems. Proponents of this view argued that many classic symbolic forms of knowlegde such as graphs and grammers were useful but <em>misleading</em> for characterizing thought. Even if they were manifest, they were more likely emergent epiphenomena than fundamental in their own right. 

Researchers of PDP and neural networks showed that this method of representation learning could, with minimal constraints and inductive biases, learn structured knowledge representations given enough data. They have shown that models could be trained to emulate the rule-like and structured behaviors that characterize cognition. In recent history - perhaps more strikingly - researchers have found that the high-level representations from modern convolutional neural networks can predict the neural response patterns in human and macaque IT cortex. That is, representations learned by generic neural networks seem to align with human representations.

While neural networks have been shown to learn features reminiscent of those learned by humans, how far towards truly human-like learning and thinking can we go by simply feeding large amounts of data to generic neural networks?

