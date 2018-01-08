---
title: Building Machines that Learn and Think Like People (Glossary)
layout: building_machines
comments: true
category: review
tags: [cognitive-science, machine-learning, brain, deep-learning]
hide: true

---


### Deep Learning
A model vaguely resembling a biological neural network that learns how to map inputs to outputs. For example, suppose you give it images of cats and dogs as inputs and the labels "cat" and "dog", respectively. It will learn to predict the label "cat" when given cat images and "dog" when given dog images.

### Neural Networks
I use "Neural Networks", "Artificial Neural Networks", and "Deep Learning" interchangeably. They all refer to artificial neural networks. When referring to the brain's networks, I say "biological neural networks".

### Inference
When A typically causes B, you can predict that B will come from A, and you can do *inference* that A was the **cause** of B.

### Model-free, Model-based
model-free algorithms use experience to directly learn quantities while model-based algorithms learn models for the world (such as probabilities for transitioning between world states). For example, learning an internal geographical map to get to work is "model-based", whereas simply learning the turn at each corner and nothing more is "model-free". Model-based is somewhat preferred because you can use your learned map to plan a new way to get to work that is a *composition* of your previous routes.

### Symbolic representations
Symbols can be thought of as having variables which represent different quantities. For example, every letter of the alphabet can be seen as a symbol. Likewise for words in our vocabulary.

### Sub-symbolic representations
A representation is sub-symbolic if its constituents are not symbolic. For example, if you represent an image as real-valued pixels, then the image has a sub-symbolic representations. A symbolic representation would represent the image itself as a symbol of some sort.

### Distributed Representations
A distributed representation is one where different computational units hold different parts of a representation. In the example of neurons in a neural network, every neuron in a layer by itself one aspect of a representation you care about. When you combine these neurons, you get the full representation.

### Inductive Biases
Inductive Biases are the assumptions your model makes about the relationship between its inputs and outputs for **new, unseen** inputs