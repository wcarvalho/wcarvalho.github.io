---
title: Building Machines that Learn and Think Like People (pt 3. Developmental Software)
layout: building_machines
comments: true
category: review
tags: [cognitive-science, machine-learning, brain, deep-learning]
---

### Article Table of Contents

| [Intuitive Physics](#intuitive-physics) |
| [Intuitive Psychology](#intuitive-psychology) |
| [Summary](#summary) |
| [References](#references) |

Neural Networks have the ability to learn rich, structured representations given abundant amounts of data, but their learning seems to be constrained (at least without infinite data) to what can be learned through pattern recognition. Increasingly, inductive biases endowed either by [architectural choices](https://tryolabs.com/blog/2017/08/30/object-detection-an-overview-in-the-age-of-deep-learning/) or by [algorithmic choices](https://deepmind.com/research/publications/human-level-control-through-deep-reinforcement-learning/) seem to be the key to effective learning with neural networks. However, to get human-level learning and thinking, there are still many core ingredients missing from neural networks. In order to gain insight into which inductive biases might be necessary for the brain, we can look at some core abilities manifest in humans by early childhood. 

Cognitive scientists have found that early in development, humans have a strong understanding of several domains including numbers, physics, and psychology {% cite core_knowledge --file building_machines_developmental %}. The authors refer to this as "developmental start-up software," and claim that this *likely* plays an active and important role in producing human-like learning and thought in ways contemporary machine learning has yet to capture. 

The process of developing cognitive representations for the domains mentioned can be seen as the development of relevant "intuitive theories" {% cite intuitive_theories --file building_machines_developmental %}. 
Experimental work with children shows the "child as a scientist" that learns about a topic (at least partially) akin to the scientific process: they seek out data that distinguishes hypotheses, isolate variables, and tests causal hypotheses {% cite where_science_starts --file building_machines_developmental %}. Childhood learning seems to resemble an active process of defining and testing intuitive theories about various aspects of the world. 

Studies indicate that these domains (or at least methods of analysis and learning about the world) are shared cross-culturally and partly with non-human animals. Here, we focus on intuitive theories of physics and psychology.

## Intuitive Physics

Researchers have found that at young ages, infants learn to incorporate physical characteristics into their representations of objects. For example, by 2 months, they expect inanimate objects to follow principles of persistence, continuity, cohesion, and solidity {% cite object_perception --file building_machines_developmental %}; by 6 months, they have developed expectations for the movement and properties of rigid, soft, and liquid bodies {% cite objects_v_substances --file building_machines_developmental %}. Unfortunately, there is no agreement on the underlying computational principles that guide this phenomena {% cite infant_reasoning_tree infant_learning_rules --file building_machines_developmental %}.

<img src="{{ site.baseurl }}/files/posts/building_machines_like_people/intuitive_physics.png">

Recently, people have started to to frame intuitive physics as inference over a physics "software engine"{% cite human_sim_prediction --file building_machines_developmental %}. <font color="grey"><em>For example, in experiments, researchers will literally simulate all or a subset of physical outcomes for a scenario using a physics engine and do inference on which is <a href="https://youtu.be/YORzoOYvonY?t=23m34s">most likely</a></em></font>. Physics engines have the desiderata that they're oversimplified and incomplete, requiring probabilistic approximations of states--something humans likely do. Further, they seem to capture how humans make predictions and simulate hypothetical world events {% cite sim_scene_understanding infant_reasoning --file building_machines_developmental %}.

It remains unclear whether physical properties can be embedded (implicitly or explicitly) into deep learning models. One successful attempt has been the PhysNet {% cite physnet --file building_machines_developmental %}, which learned to predict the stability of 2, 3, or 4 towers of blocks. Its performance matched human performance on real images, and exceeded it on synthetic images. However; it requires extensive training (hundreds of thousands of examples) and has limited generalization abilities.

A clear challenge is whether deep learning models can be made to generalize well without explicitly simulating causal interactions (i.e. containing causal models of the world). One possible method is to have the model emulate a physics simulator, where successive layers of abstraction hopefully learn successive high-level physics dynamics (e.g. distance, velocity, and acceleration). This would be akin to the way current models learn successive abstractions over images (where lower layers learn edges, successive layers learn textures, and even deeper layers learn objects). In deep reinforcement learning, this might enable models that are more robust to slight alterations in the testing data -- something that now requires re-training.

## Intuitive Psychology

Researchers have found that intuitions about other agents also emerge in infancy. For example, pre-verbal infants learn to distinguish inanimate objects from animate objects using low-level cues such as the presence of eyes or whether an object initiates movement from rest {% cite infant_gaze --file building_machines_developmental %}.

Infants also expect agents to act contingently, to have goals, and to take efficient goals subject to constraints {% cite goal_attribution_infants --file building_machines_developmental %}. At just 3 months, infants are able to discriminate anti-social agents that hurt or hinder others from neutral agents. Soon thereafter, they learn to distinguish anti-social, neutral, and pro-social agents {% cite infant_moral_judgement --file building_machines_developmental %}.

<font color="grey"><em>
These "intuitive psychology" abilities are likely useful for AI agents learning to play games, and learning to model the behavior of other agents within the game. For example, an AI agent with these abilities can learn to distinguish animate objects from inanimate objects, categorize animate objects, treat them as other acting agents, and learn relevant corresponding attributes for animate-object categories (e.g. harmful/helpful, anti-social/pro-social).</em></font><br>

Cognitive scientists have tried to model social behavior in a rule-based manner {% cite cue_system --file building_machines_developmental %} but this is not robust to the many possibilities for how an agent can interpret highly variable scene settings. An alternate approach that is becoming increasingly popular is to model agents as having generative models ([glossary]({{ site.baseurl }}/review/2017/12/23/building_machines_glossary/#generative-models)) for the actions of others {% cite bayesian_tom --file building_machines_developmental %}. <font color="grey"><em>Such a representation fits well with the example above where an agent learns to model animate objects in the world as other acting agents with attributes. Stereotyping the behavior of other agents based on their perceived category membership (i.e. assuming all agents that belong to a category perform the same actions) may then allow for quick reasoning about their actions.</em></font>

Just as it is unclear whether deep learning systems can implicitly learn physical properties, it is unclear if they can learn high-level psychological representations for concepts such as "agents" and "goals" in their modern capacity. The endowment of such principles from intuitive psychology could, for example, allow for learning about a game by watching another agent playing it. If another agent consistently avoids a particular object, an AI can then infer that object is dangerous or "anti-social" without experiencing the consequences of that interaction.


## Summary

Research indicates that there are a number of key skills manifest in infancy. It makes sense that these skills aid us in learning and utilizing new information quickly as we progress through life. Intuitive physics gives us a basis for reasoning about the physical world and intuitive psychology about the social world. However, it is unclear how to incorporate these skills into modern neural networks and endow them with the ability to learn and build on knowledge similarly to humans.

At a more fundamental level, from an early age, humans show the ability to seek out knowledge as they build internal models for the world. How these questions are devised, their answers found, and the subsequent knowledge stored and incorporated is unclear. Just as there is a concept of the "child as a scientist" actively learning about the world, can we have a "neural network as a scientist"?

## References

{% bibliography --file building_machines_developmental %}