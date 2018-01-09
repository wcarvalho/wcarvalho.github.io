---
title: Building Machines that Learn and Think Like People (pt 5. Thinking Fast)
layout: building_machines
comments: true
category: review
tags: [cognitive-science, machine-learning, brain, deep-learning]
---

<br>

| Article Table of Contents |
| --- |
| [Approximate inference in structured models](#approximate-inference-in-structured-models) |
| [Model-based and model-free reinforcement learning](#model-based-and-model-free-reinforcement-learning) |
| [Series Conclusion](#series-conclusion) |
| [References](#references) |

So far in this series we've covered:

* the history of building machines that learn and think like people,
* current challenges for having neural networks learn like people, including learning efficiently and learning robust, generalizable representations,
* skills manifest in infancy which seem to be key to learning complex concepts as adults, and
* what might allow for neural networks to learn rapidly instead of slowly as they currently do

In this post, the focus is shifted from learning like humans to thinking like humans. Particularly, the focus is on how neural networks can be endowed with the ability to do quick, complex inference, and with the ability to combine model-free and model-based methods for flexible representations in reinforcement learning. 


## Approximate inference in structured models

Many tasks that humans do are computationally expensive. For example, the complex inference we're capable of doing, (for example, inferring all the reasons behind social dynamics we experience) is, from a statistical perspective, very computationally expensive. If we were to indeed look at all possibilities when doing inference, it would be an impossible task. However, to have inference with high accuracy, rich and structured inference models are typically necessary which required complex and slow inference algorithms. This makes the speed with which humans perceive, think, and perform inference remarkable. The brain's neural networks, and current neural networks, may provide the efficient approximations necessary to alleviate this cost.

Cognitive scientists have proposed that the brain does approximate inference using monte-carlo methods {% cite monte_carlo_inference --file building_machines_thinking %}. This works by picking a possible hypothesis and evaluating it against data and prior knowledge. This, however, doesn't seem to fall in line with how humans do inference because our exploration is guided and not random. For example, in the game of frost-bite, we learn that jumping on an ice-float constructs part of the igloo, that birds make you lose points, that you can change the direction of an ice-float at the cost of an igloo piece, and so on as we learn a causal model for the game.

Recently, deep learning research has begun to work on the problem of learning to do inference. This is potentially useful because solutions to related problems become correlated, a phenomenon shown in humans {% cite amortized_inference_humans --file building_machines_thinking %}. Still, the inference supported by neural networks is far less flexible than more computationally expensive, but seemingly unrealistic methods like monte-carlo methods. A key line of research for human-like thinking is studying how neural networks can perform rich, flexible, and fast inference.


## Model-based and model-free reinforcement learning

When looking at reinforcement learning in deep learning, we focused on the DQN. It is a model which uses a model-free algorithm for learning to play video games. This was useful because model-free algorithms are known for their speed. However, significant evidence indicates that the brain also has a model-based learning system, responsible for building a "cognitive map" of the environment and using it to plan action sequences for complex tasks {% cite model_free_based --file building_machines_thinking %}.

To reuse knowledge of what has been learned for new tasks, model-based methods seem like an appropriate choice. However, model building is slow. Evidence in humans shows that actions begin model-based and slow and become model-free and fast over the course of learning {% cite speed_accuracy --file building_machines_thinking %}. As shown in the sections on [Challenges for Building Human-Like Machines]({{ site.baseurl }}/review/2017/12/31/building_machines_challenges), employing a model-based system seems to be key to more sophisticated tasks. Learning how the brain does this might allow for more robust AI. 


## Series Conclusion

While deep learning is gaining a lot of [media](https://www.wired.com/tag/deep-learning/) and [industry](https://www.bloomberg.com/news/articles/2017-12-06/demand-for-ai-talent-turns-once-staid-conference-into-draft-day) attention for its efficacy as an AI system, it is clear that deep learning still has a way to go before achieving human-level general intelligence. While "Building Machines that Learn and Think Like People" was written more than a year ago, most (if not all) of the challenges it discusses are still present. Humans quickly learn rich representations for the world and this is something currently lacking from AI and neural networks. However, neural networks are making tremendous progress, for example, [reaching super-human abilities in the game of go](), a feat that was considered decades away just a few years ago. 

I, personally, am excited by the speed of deep learning research. I am happy that neuroscientists, cognitive scientists, and those with little interest in the brain are working to advance the field. While neural networks are still very crude approximations for the brain's networks and obviously wrong, I think they are one of the best areas of research for understanding how the brain learns and processes information. At the least, while the learning method may not resemble the brain's, the learned representations seem to resemble the brains. As we continue to do research, I have hope that we will one day be able to create neural networks that do in fact learn and think like people, though I believe we are decades (or centuries) away from this, and I'm okay with that. 

## References
{% bibliography --file building_machines_thinking %}