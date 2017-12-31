---
title: Building Machines that Learn and Think Like People (pt 1. Introduction and History)
layout: building_machines
comments: true
category: review
tags: [cognitive-science, machine-learning, brain, deep-learning]
---

### Article Table of Contents

| [Motivation for series](#motivation-for-series) |
| [Introduction](#introduction) |
| [History of Brain-Inspiration in AI](#history-of-brain-inspiration-in-ai) |
| [References](#references) |
| [Glossary](#glossary) |

## Motivation for series
### (Feel free to skip)
This is part 1 in a series of blog posts, where I plan to summarize the fascinating (but lengthy) [Building Machines that Learn and Think Like People](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/building-machines-that-learn-and-think-like-people/A9535B1D745A0377E16C590E14B94993) by Lake et al. This paper discusses how current [deep learning models](https://medium.freecodecamp.org/want-to-know-how-deep-learning-works-heres-a-quick-guide-for-everyone-1aedeca88076)[^1], despite their [success](https://www.technologyreview.com/s/513696/deep-learning/) and common comparison to [the](http://www.dailymail.co.uk/sciencetech/article-5207101/Googles-AI-software-learning-makes-good-photo.html) [brain](https://www.datanami.com/2017/07/06/google-mimics-human-brain-unified-deep-learning-model/), do not learn how brains do in many respects. The authors offer a set of "key ingredients" to endow neural networks[^2] with what might allow them to learn and think more like brains do.

I've wanted to read this paper for some time. One of my central goals as an aspiring brain and machine learning researcher is to build human-inspired AI. As I'm very junior in the field, I thought this paper would give me a lot of insight into how to go about doing that. I was finally pushed into reading it when I discovered that along with this paper, the Journal for Behavioral and Brain Sciences has published [27 promising commentaries](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/building-machines-that-learn-and-think-like-people/A9535B1D745A0377E16C590E14B94993#fndtn-related-commentaries)! Among the ones I'm most excited to read next are:

1. [Building machines that learn and think for themselves](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/building-machines-that-learn-and-think-for-themselves/E28DBFEC380D4189FB7754B50066A96F) by DeepMind 
2. [Building on prior knowledge without building it in](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/building-on-prior-knowledge-without-building-it-in/F342A14C57094D5AF7BC62950AE49CD8) by McClelland et al.
3. [Ingredients of intelligence: From classic debates to an engineering roadmap](https://www.cambridge.org/core/product/3D2A685AC198EC0008835514735033BB), a meta-response by Lake et al.


## Introduction

The purpose of this series is to highlight the challenges with building machines that learn and think like people. As such, I will skip aspects of the paper that generally review deep learning. Please feel free to read the paper for that material. The key idea: thanks to tremendous skill in pattern recognition, deep neural networks have achieved state-of-the-art performance in numerous domains including 

* [computer vision](https://tryolabs.com/blog/2017/08/30/object-detection-an-overview-in-the-age-of-deep-learning/) (e.g. learning to detect objects in images with complex scenes {% cite imagenet --file building_machines_intro %})
* [speech modeling](https://deepmind.com/blog/wavenet-generative-model-raw-audio/) (e.g. learning to produce human-like speech {% cite wavenet --file building_machines_intro %}), and 
* [complex control problems](https://deepmind.com/research/publications/human-level-control-through-deep-reinforcement-learning/) (e.g. learning to play a Atari video-games without embedded knowledge of the video-game structure {% cite dqn --file building_machines_intro %}). 

While neural networks perform very well on many tasks, they have limitations. For example, they often must be trained on tremendous quantities of data. Additionally, they are not know to generalize knowledge well to different tasks. This is in part because they (at least, in their current form) rely on statistical pattern recognition--they essentially learn to notice patterns through thousands to millions of examples. An alternative, which {% cite lake --file building_machines_intro %} suggest is a key ingredient of human learning, is a model-building approach. They argue that intelligent cognition relies on building and using [causal models](https://en.wikipedia.org/wiki/Causal_model) to understand, explain, simulate, and predict the world. Despite this contrast, these two methods are certainly not orthogonal and machines can synergistic ally benefit from both.


The authors maintain that while they are critical of neural networks, they see them as somewhat fundamental to human-like learning machines. This is partly because any computational model for human learning must ultimately be grounded in the brain's biological neural networks. However, the authors believe that future generations of neural networks will look very different from current state-of-the-art.

<font color="grey"><em>
  I support this -- the neural networks we use are crude abstractions of our currently incomplete and incorrect models for biological neural networks.
  For example, neuroscientists (and especially AI researchers) have long modeled neurons as single excitable units. Whether a neuron fires was a function of the electric signal that it received from its dendrites. For more on this perspective, see <a href="http://cs231n.github.io/neural-networks-1/#biological-motivation-and-connections">this introduction</a>. However, physicists have recently found that neurons are not single excitable units but a collection of excitable units {% cite multineuron --file building_machines_intro %}. Further, each excitable unit is sensitive to the <strong>directionality</strong> of the origin of the input signal (i.e. the direction of the attached dendrite). This will potentially require a dramatic reformulation of artificial neural networks and will likely spur much research.
</em></font>

<br>
<strong>The main contribution of this paper is its suggestion of "key ingredients" for building machines that learn and think like people. </strong> Defining and motivating these ingredients makes up a majority of the paper, so I will make each broad category its own article in this series:

* ["Developmental Software"]({{ site.baseurl }}/review/2017/12/22/building_machines_developmental): intuitive theories for the world that we learn at an early age such as theories of intuitive physics and intuitive psychology, 
* ["Model Building"]({{ site.baseurl }}/review/2017/12/22/building_machines_learning): the ability to build casual models of the world via methods such as [compositionality](https://plato.stanford.edu/entries/compositionality/) and [learning-to-learn](http://bair.berkeley.edu/blog/2017/07/18/learning-to-learn/), and 
* ["Thinking quickly"]({{ site.baseurl }}/review/2017/12/22/building_machines_thinking): the ability to quickly do inference[^3] and prediction by combining model-free and model-based algorithms[^4].

## History of Brain-Inspiration in AI

Scientists such as Alan Turing have long thought that AI could be informative to or descriptive of cognition {% cite computing_turing --file building_machines_intro %}. In fact, Turing held a [behaviorist view](http://www.funderstanding.com/theory/behaviorism/) of learning reminiscent to a popular modern view that almost everything can be learning from the statistical patterns of sensory inputs.

Cognitive scientists repudiated this view of cognition and instead assumed that human knowledge representation was symbolic[^5] in nature. They argued that many functions of cognition such as language and planning could be understood in terms of symbolic operations. This falls in line more with a "model-based" approach as you use an explicitly structured representation.

Somewhat complementary to both, another school of thought - and what would become the basis for deep learning - believed in sub-symbolic[^6] distributed representations[^7] of knowledge produced by parallel distributed processing (PDP) systems {% cite pdp --file building_machines_intro %}. Proponents of this view argued that many classic symbolic forms of knowledge such as graphs and [grammars](https://en.wikipedia.org/wiki/Grammar) were useful but <em>misleading</em> for characterizing thought. Even if they were manifest, they were more likely emergent epiphenomena than fundamental in their own right {% cite structure_emerge --file building_machines_intro %}. 

Researchers of PDP and neural networks showed that this method of distributed representation learning could, with minimal constraints and inductive biases[^8], learn structured knowledge representations given enough data. They have shown that models could be trained to emulate the rule-like and structured behaviors that characterize cognition {% cite dqn --file building_machines_intro %}. In recent history - perhaps more strikingly - researchers have found that the representations learned by artificial neural networks can predict the neural response patterns in the human and macaque cortex {% cite deep_it --file building_machines_intro %}. That is, representations learned by generic neural networks seem to align with human representations.

Modern neural networks fed large amounts of data for pattern recognition tasks have been shown to learn representations reminiscent of those learned or used by humans. <strong>But how far towards truly human-like learning and thinking can we go by simply feeding large amounts of data to generic neural networks?</strong>

<br>
# References
{% bibliography --file building_machines_intro %}

---
# Glossary
[^1]: **Deep Learning**: a model vaguely resembling a biological neural network that learns how to map inputs to outputs. For example, suppose you give it images of cats and dogs as inputs and the labels "cat" and "dog", respectively. It will learn to predict the label "cat" when given cat images and "dog" when given dog images.
[^2]: I use "Neural Networks", "Artificial Neural Networks", and "Deep Learning" interchangeably. They all refer to artificial neural networks. When referring to the brain's networks, I say "biological neural networks".
[^3]: When A typically causes B, you can predict that B will come from A, and you can do *inference* that A was the **cause** of B.
[^4]: model-free algorithms use experience to directly learn quantities while model-based algorithms learn models for the world (such as probabilities for transitioning between world states). For example, learning an internal geographical map to get to work is "model-based", whereas simply learning the turn at each corner and nothing more is "model-free". Model-based is somewhat preferred because you can use your learned map to plan a new way to get to work that is a *composition* of your previous routes.
[^5]: Symbols can be thought of as having variables which represent different quantities. For example, every letter of the alphabet can be seen as a symbol. Likewise for words in our vocabulary.
[^6]: A representation is sub-symbolic if its constituents are not symbolic. For example, if you represent an image as real-valued pixels, then the image has a sub-symbolic representations. A symbolic representation would represent the image itself as a symbol of some sort.
[^7]: A distributed representation is one where different computational units hold different parts of a representation. In the example of neurons in a neural network, every neuron in a layer by itself one aspect of a representation you care about. When you combine these neurons, you get the full representation.
[^8]: Inductive Biases are the assumptions your model makes about the relationship between its inputs and outputs for **new, unseen** inputs