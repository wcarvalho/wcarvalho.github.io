---
title: "Weak inductive biases for composable primitive representations"
layout: project_page
---

<center><h1>Weak inductive biases for composable primitive representations</h1></center>
<br>

To generalize across object-centric tasks, a reinforcement learning (RL) agent needs to exploit the structure that objects induce. However, it's not clear how to incorporate objects into an agent's architecture or objective function in a flexible way. Prior work has either hard-coded object-centric features or used inductive biases with strong assumptions. However, these approaches have had limited success in enabling general RL agents.  Part of what gives objects their utility is that they enable an agent to break up and recombine its experience. Motivated by this, we propose “separate and integrate”, a motif for weak inductive biases aimed at enabling an agent to break up and recombine its basic computations: estimating state, predicting value, etc.

We present initial results with ["Feature-Attending Recurrent Modules” (FARM)](https://arxiv.org/abs/2112.08369), an architecture that separates and integrates state across multiple state modules. Additionally, each module attends to spatiotemporal features with an expressive feature attention mechanism. This enables FARM to represent diverse object-induced spatial and temporal regularities across subsets of modules. We hypothesize that this enables an RL agent to flexibly recombine its experiences to generalize across object-centric tasks. We study task suites in both 2D and 3D environments and find that FARM better generalizes compared to competing architectures that leverage attention or multiple modules.

