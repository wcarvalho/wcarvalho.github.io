---
title: Building Machines that Learn and Think Like People (pt 4. Learning as Rapid Model-Building)
layout: building_machines
comments: true
category: review
tags: [cognitive-science, machine-learning, brain, deep-learning]
---

### Article Table of Contents

| [Compositionality](#compositionality) |
| [Causality](#causality) |
| [Learning-to-learn](#learning-to-learn) |
| [References](#references) |

Previously, we discussed some skills manifest early in childhood that might play a key role in human-level learning & thinking. Whereas there, the focus was on what type of information the brain may use to bootstrap learning, here we focus on how the brain learns so efficiently. We will try to discuss methods of learning that are potentially useful for the brain, with a particular focus on endowing neural networks with the ability to "rapidly build models". By this, we mean the ability to quickly learn and construct models for "concepts" of things in the world.

Throughout the history of neural networks, learning has traditionally been characterized by gradual adjustment of network weights (abstractions for their synapses) {% cite contrastive_divergence backprop --file building_machines_learning %}. Through gradual weight changing, neural networks have learned to gradually (read slowly) match the statistics of a dataset they're trained on. However, we know from studies with children that humans have the ability to learn and generalize rapidly from small amounts of data {% cite new_word --file building_machines_learning %}. If you imagine that there is some abstract, infinite space which contains representations of all possible objects, humans seem to be able to demarcate the subset of that space which corresponds to a particular category after only a few examples. For example, in the image below, from just seeing a few examples of "dogs", humans learn that "dogs" belong to a particular region in that space. <font color="grey"><em>This reminds me of the stratification found between concept representations with <a href="http://suriyadeepan.github.io/img/seq2seq/we1.png">word embeddings</a>. This makes me wonder if humans are learning the demarcation in a naturally occuring space that they'e learning or in a space they fabricate and populate as they learn. Put differently, it makes me wonder if the space below is real and learned by humans or created by humans as they learn to represent and differentiate objects.</em></font>

![space_demarcation]({{ site.baseurl }}/files/posts/building_machines_like_people/space_demarcation.png)

It is clear that neural networks don't use data as efficiently as humans do. The authors argue that what differentiates humans from neural networks currently is that neural networks simply learn to recognize patterns whereas humans learn *concepts*. Learning concepts is more flexible because you can, for example, parse a concept into important components or create more sophisticated meta-concepts. To learn concepts, the authors suggest we work to endow neural networks with compositionality, causality, and learning-to-learn.

To showcase the utility of these components, the authors compare learning with a neural network to learning with a probabilistic programming framework they developed known as "Bayesian Program Learning" (BPL) {% cite bpl --file building_machines_learning %}. Here, concepts are learned as simple, learnable, stochastic programs which are controlled by a meta-program. I will describe how the framework works in the context of representing the characters in omniglot as concepts:

1. One program is responsible for representing concepts/object templates.
    1. There are primitives, which for omniglot represent "fundamental" strokes that can be made for characters.
    2. Primitives are related and combined to create parts. Parts are then re-related and combined to create templates for a "concept".
2. A meta-program is then responsible for generating a "concept" using the template. This whole process is stochastic because how each component of a concept manifests (or is drawn) is stochastic. In the figure below, you can see possible variations the program might generate for each object template.

![bpl]({{ site.baseurl }}/files/posts/building_machines_like_people/bpl.png)

Concept learning is then learning these stochastic programs for generating object templates. A key facet of concepts is that their "components" are represented **hierarchically**. For example, primitives are combined into sub-parts which are combined and related into parts in a hierarchical process. By representing concept learning in this form, BPL is able to learn character concepts using only a few examples similarly to humans.


## Compositionality

Compositionality is the classic idea that new representations can be constructed through combinations of primitive elements. Real world examples include sentences which are combinations of words, the "primitives" of language {% cite lang_of_thought --file building_machines_learning %}, or programs which are compositions of functions, which are themselves compositions of more primitive data types.

Compositionality has been influential in both artificial intelligence and cognitive science. This paper focuses on it in the context of object representation. Here, structural description models have historically assumed that visual concepts could be represented as *compositions* of parts and relations {% cite vis_composition --file building_machines_learning %}. For example, a segway can be *composed* of wheels, connected to a stand and handle.

As a reminder, learning-to-learn is the idea of using learned concepts as "primitives" for other concepts when learning. In the diagram above, once one learns the "primitives", using them to learn new concepts is "learning-to-learn". <font color="grey"><em>("Learning-to-learn" actually sounds like a misnomer in this context. You're not learning to learn. You're bootstrapping knowledge. But I digress.)</em></font> Compositionality and learning-to-learn, as seen by the example above, can naturally go together for learning concepts, especially with a hierarchical structure. This in turn can facilitate generalization to new tasks as previous knowledge is easily built upon and reused.

Neural networks have been shown to have compositionality like functionality as progressively deep layers are compositions of more primitive features at lower layers. However, neural networks seem to lack the "relation" feature, disallowing them from utilizing compositionality for complex tasks. <font color="grey"><em> This seems to no longer be true as <a href="https://www.youtube.com/watch?v=pPN8d0E3900">capsule</a> <a href="https://medium.com/ai%C2%B3-theory-practice-business/understanding-hintons-capsule-networks-part-i-intuition-b4b559d1159b">networks</a> seem to be able to capture relations between objects. Previously, neural networks would recognize the object in the image below as a face because they learned that faces were compositions of more primitive parts (nose, eyes, lips, etc.). However, capsule networks also learn relations between parts, requiring the components of a face to have roughly correct spatial relations in order for the composition to be classified as a face. </em></font>

![capsule]({{ site.baseurl }}/files/posts/building_machines_like_people/capsule.png)

Compositionality in neural networks has a number of utilities. Besides allowing for more sophisticated object recognition, non-visual objects can also be seen from a compositional perspective. For example, completing the level of a video game can be thought of (and possibly learned) as completing a composition of sub-goals (e.g. get to ledge, jump down, jump over enemy, etc.).

## Causality

Causal models attempt to abstractly describe the real world process that produces an observation. They are a sub-class of generative models that attempt to describe a process for generating data. They differ in that the process for generating data described by a generative models does not need to resemble the real world process that generated the data, whereas in causal models, it does. For example, a model that learns to predict the pixels associated with different character concepts is simply a generative model (e.g. {% cite vae --file building_machines_learning %}); whereas a model that attempts to generate hand-written characters by imitating strokes is a causal model (e.g. {% cite bpl --file building_machines_learning %}). 

Causal models have been influential in research on perception, particularly in the idea of "analysis by synthesis" {% cite analysis_by_synthesis --file building_machines_learning %}. It states that sensory data can be more richly represented by modeling the process that generated it. Studies in cognitive science have shown that causal models are important and likely modeled by humans. For example, experiments have shown that changing the causal process for how data is generated can change how humans both learn and generalize what they learn {% cite causality_effects_humans --file building_machines_learning %}.

Much research indicates that we model the causal process that generated the data we see. For example, when we see images, we often interpret or caption them in the form of an answer to "why is this happening?" {% cite causality_effects_humans --file building_machines_learning %}. This is something that neural networks currently lack, as evident by the examples of captions generated by neural networks below. While the components in the images are present, their causal relation is missing and leads to wildly inaccurate captions.

![nn_captions]({{ site.baseurl }}/files/posts/building_machines_like_people/nn_captions.png)

While neural networks have had difficulty learning the causal structure in images, one has done a good job with learning causal models for hand-written characters: the DRAW architecture {% cite draw --file building_machines_learning %}. This model was able to learn a causal model for characters and learned to draw characters from only a few examples similarly to the BPL. However, the authors claim that they way in which DRAW generalizes is inhuman. This is, however, a point of contention {% cite think_for_themselves --file building_machines_learning %}, as prominent cognitive scientists and neuroscientists have argued otherwise.

Regardless, neural networks can likely benefit from causality and compositionality. They may facilitate learning-to-learn as it may allow for more primitive concepts to effectively be utilized for explaining new data. They may also facilitate neural networks learning realistic models for how data is produced, and more strongly, learning model for the world and how it changes.

## Learning-to-learn

As mentioned before, learning-to-learn is the utilization of prior knowledge in learning a new task. In BPL, this was reusing primitives and learned parts when learning new concepts. In machine learning, this is closely related to "transfer learning" where you apply knowledge learned from one task to another, "multi-task learning" where you learn multiple tasks concurrently with the hope that task-constituents are shared and help each other, and "representation learning" where you seek to learn generalizable representations of data.

In learning-to-learn, hierarchical structure seems to be particularly useful. For example, with BPL, once the parts were learned, hierarchical structure facilitated their reuse for learning new concepts. Further, hierarchical structure allowed for compositionality, causality, and learning-to-learn to naturally work together, acting somewhat like a catalyst for producing a model that could quickly learn new concepts. 

While there is much research being done on learning-to-learn, the authors believe this could particularly benefit from compositional, hierarchical, and causal representations. <font color="grey"><em>I actually think neural networks already have compositional and hierarchical representations. However, they're missing causality, which I do believe will play a key role. I think this is evident by the captions generated above. </em></font> Learning-to-learn is particularly important for efficient learning because it allows for the re-use of learned representations for new tasks and **the interaction between representations and previous experience may be the key to building machines that learn as fast as people do**.

## References

{% bibliography --file building_machines_learning %}