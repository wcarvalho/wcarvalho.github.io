---
title: Knowledge of the Brain Informing Machine Learning and Vice-Versa
excerpt: I share interesting material (papers, articles, etc.) I came across related to how brain research is complimenting machine learning research and vice-versa.
comments: true
layout: post
tags: [machine-learning, brain, research]
---

I have just joined [Yan Liu's research group](http://www-bcf.usc.edu/~liu32/) and gave a small presentation this monday surveying current work using knoweldge about the brain to inform machine learning and vice-versa.

The focus of the presentation was a recent paper published by Google DeepMind in Nature, [Human-level control through deep reinforcement learning](http://www.nature.com/nature/journal/v518/n7540/full/nature14236.html).

The presentation was meant to introduce the group to my research interests. I chose to focus on research that has explored the relations between the architecture and functionality of the brain and artificial neural network models. 

As I prepared for the presentation, I came across many interesting papers, articles, and videos. I thought I'd gather and share them here for others with similar interests. 

*Note: some things weren't particularly relevant to my research interests but I found them really cool so I added them to this list anyway.*

#### Papers

##### [Human-level control through deep reinforcement learning](http://www.nature.com/nature/journal/v518/n7540/full/nature14236.html)
1. [Playing Atari with Deep Reinforcement Learning ](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf). This was the original model they created.
1. [Review by Jürgen Schmidhuber](http://people.idsia.ch/~juergen/naturedeepmind.html). Two members of the original DeepMind team worked in his lab. He claims some of the results of the paper had already been found by his lab.
1. [**Code** for Human-Level Control](https://sites.google.com/a/deepmind.com/dqn/)
1. [Play it again: reactivation of waking experience and memory](http://ac.els-cdn.com/S0166223610000172/1-s2.0-S0166223610000172-main.pdf?_tid=77068256-8c45-11e5-b963-00000aab0f26&acdnat=1447666748_9c10668ad2aa41dc9b08bea73b771683). The memory consolidation described here was the inspiration for their "action replay" model.

##### Deep architecture possibly used by brain for vision
1. [A quantitative theory of immediate visual recognition](http://serre-lab.clps.brown.edu/wp-content/uploads/2012/08/Serre_etal_PBR07_wfig.pdf). This is a quantitative model for how the brain performs rapid object recognition. It indicated that the brain had a deep architecture.
1. [Sparse belief net model for V2](http://papers.nips.cc/paper/3313-sparse-deep-belief-net-model-for-visual-area-v2.pdf). This was an ANN model which successfully replicated results from visual cortices V1 & V2.
1. [Learning Deep Architectures for AI](http://www.iro.umontreal.ca/~pift6266/A08/documents/ftml.pdf), [Shallow vs. Deep Sum-Product Networks](http://papers.nips.cc/paper/4350-shallow-vs-deep-sum-product-networks.pdf). Two articles by Yoshua Bengio in which he explores deep architectures. He claims deep architectures may be necessary to learn the complicated functions necessary to represent high-level abstractions, e.g. vision, language, etc.

##### "Neural-Turing Machines"
1. [The Human Turing Machine: a Neural Framework for Mental Programs](http://www.ncbi.nlm.nih.gov/pubmed/21696998)
1. [Neural Turing Machines](http://arxiv.org/abs/1410.5401)

##### Misc. Papers
1. **Modha, Dharmendra S et al. “Cognitive Computing.” Communications of the ACM 54.8 (2011): 62–71.** Couldn't get a link. This describes IBM's brain-inspired chip and some of the ways software is being implemented for it.
1. [Is the Brain a Good Model for Machine Intelligence?](http://www.gatsby.ucl.ac.uk/~demis/TuringSpecialIssue(Nature2012).pdf). Fun series of articles discussing advancements and limitations in modeling the brain's computations.
1. [Machines That Think for Themselves](http://www.nature.com/scientificamerican/journal/v307/n1/full/scientificamerican0712-78.html)
1. [Learning to Execute](http://arxiv.org/abs/1410.4615). A neural network to learn simple computer programs.
1. [RM-SORN: a reward-modulated self-organizing recurrent neural network](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4371712/). A dynamic neural network model that uses Hebbian learning to learn to perform a variety of tasks. 
1. [Show and Tell: A Neural Image Caption Generator](http://arxiv.org/pdf/1411.4555v1.pdf). An article about transfer learning (learning being transferred from one network to another)
1. [Unsupervised and Transfer Learning Challenge: a Deep Learning Approach](http://jmlr.csail.mit.edu/proceedings/papers/v27/mesnil12a/mesnil12a.pdf)
1. [Unsupervised feature learning for audio classification using convolutional deep belief networks](http://papers.nips.cc/paper/3674-unsupervised-feature-learning-for-audio-classification-using-convolutional-deep-belief-networks.pdf). Deep learning applied to audio.
1. [A Large-Scale Model of the
Functioning Brain](http://www.sciencemag.org/content/338/6111/1202.full.pdf). A mini-brain model that can redraw images it is presented with - seems pretty cool.
1. [Survery of papers on transfer learning](https://scholar.google.nl/scholar?cluster=17771403852323259019&hl=en&as_sdt=0,5)
1. [Deep Learning Reading List](http://deeplearning.net/reading-list/)

#### Other

##### Articles
1. [Deep Minds: An Interview with Google's Alex Graves & Koray Kavukcuoglu](https://www.linkedin.com/pulse/deep-minds-interview-googles-alex-graves-koray-sophie-curtis)
3. [Fei-Fei Li: If We Want Machines to Think, We Need to Teach Them to See](http://www.wired.com/brandlab/2015/04/fei-fei-li-want-machines-think-need-teach-see/)
4. [Andrew Ng: Why ‘Deep Learning’ Is a Mandate for Humans, Not Just Machines](http://www.wired.com/brandlab/2015/05/andrew-ng-deep-learning-mandate-humans-not-just-machines/)
4. [The Man Behind the Google Brain: Andrew Ng and the Quest for the New AI](http://www.wired.com/2013/05/neuro-artificial-intelligence/)
6. [Artificial Neural Networks Get a Boost: Computer Chip Replicates Neuron Activity](http://www.decodedscience.org/artificial-neural-networks-get-a-boost-computer-chip-replicates-neuron-activity/5894)
7. [Machine-Learning Maestro Michael Jordan on the Delusions of Big Data and Other Huge Engineering Efforts](http://spectrum.ieee.org/robotics/artificial-intelligence/machinelearning-maestro-michael-jordan-on-the-delusions-of-big-data-and-other-huge-engineering-efforts)
11. [Thinking in Silicon](http://www.technologyreview.com/featuredstory/522476/thinking-in-silicon/).
13. [Using large-scale brain simulations for machine learning and A.I.](https://googleblog.blogspot.com/2012/06/using-large-scale-brain-simulations-for.html)
1. [Building artificial nervous system (seem like biophysical modeling)](http://www.theatlantic.com/video/archive/2012/07/mapping-the-brains-neural-networks-to-build-an-artificial-nervous-system/260397/)
2. [Neuroscientists Are Making an Artificial Brain for Everyone](http://www.wired.com/2015/05/nara-logics-ai/)

##### Videos
2. [DeepMind Founder (Shane Legg) talk on machine intelligence](https://www.youtube.com/watch?v=evNCyRL3DOU)
9. [Video about Deep learning by Geoffery Hinton](https://www.youtube.com/watch?v=1Wp3IIpssEc)

##### Misc.
8. Tutorial: [Neural Networks, the Human Brain and Learning](http://www.doc.ic.ac.uk/~nd/surprise_96/journal/vol2/cs11/article2.html)
