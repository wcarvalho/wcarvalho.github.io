---
title: "Dendrites in Artificial Neural Networks define a Column Space?"
comments: true
layout: post
category: deep-learning, machine-learning, linear-algebra
tags: [commentary]
---


I'm currently taking a linear algebra course. The ideas of bases, spans, column spaces, etc. are giving me interesting new ways to think about how neural networks function. I thought I'd share them here. As an example, let's look at a single neural network layer with the relu non-linear activation $f(x)=max(0, x)$.

Let's recall the definition for a column space from linear algebra. A column space is the set of all linear combinations of vectors in a matrix, i.e. their *span*. I chose to forgo discussion on the rank of the matrix or independence of these vectors. Let's just think about the space defined by all linear combinations of these vectors.

<img class="regular materialboxed responsive-img" src="{{ site.baseurl }}/files/posts/misc/simple_nn.png">

$$Definitions$$:
1. $\mathbf{x}$: activations at starting layer
3. $\mathbf{y}$: activations at next layer
2. $A$: matrix defining dendritic connections from $\mathbf{x}$ to $\mathbf{y}$

In a simple, feed-forward neural network, we get activations at a layer $\mathbf{y}$ by multiplying activations at the previous layer $\mathbf{x}$ with a matrix $A$ that defines their dendritic connections. If we think about this in the language of linear algebra, the dendritic connections between layers $A$ define a *column space* and the output activations $\mathbf{y}$ are a vector *within* that column space. The activations at the previous layer $\mathbf{x}$ then **define** how columns within the column space of $A$ are combined to produce $\mathbf{y}$. 

A popular activation function is relu:

$$f(y)=max(0, y)$$

It seems to have some interesting properties in this context.
1. By making elements in this vector $0$, relu seems to project the vector to a lower dimensional subspace. I'm not sure why this is beneficial...
2. Relu also seems to define which vectors from the **next** column space will and won't be used.

Thinking about this was pretty mind blowing for me. 

First, I always thought neurons held all information and that it was routed through layers of a neural network. But this seems to imply that dendrites themselves hold a **massive** amount of information: **they define the column space that activations can belong to!!**

Second, backpropagation is an iterative method of changing dendritic connections. In this perspective, this means backpropagation is an iterative method of changing (perhaps perfecting?) the **column space** defined by dendrites?

If you are knowledgeable about neural networks, linear algebra, or research at their intersection, I'd love if you could contribute to this discussion.