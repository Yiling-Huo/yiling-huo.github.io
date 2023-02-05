---
layout: post
title: 23 Jan 2021, Delaney-Busch et al. 2019
date: 2021-01-23 21:41
author: balalahelo
comments: true
categories: [adaptations, model simulation, N400, 未分类]
---
<!-- wp:paragraph -->
<p>A study that fitted a Bayesian learning model to ERP data to study trial-by-trial N400 modulation in two-word priming settings.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The ERP study had two blocks, in block 1 10% of the target word were related with the prime word, while in block 2 50% of the words were related.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The model assumed that the participant estimates the chance of seeing a related word based on both Forward Association Strength and environmental confidence (how likely the participant believes the trial will be related words), plus a small chance of encountering the target word as an unrelated random word. They log transformed the output to indicate surprisal (?)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>They initially got highly significant results doing regressions of the model output and actual ERP data, but they feared that the significance can be largely evoked by the raw semantic priming effect. They entered categorical relatedness as control predictor in their mixed effects regression, variance accounted for dropped a little but was still significant. However they still feared that multicollinearity between categorical relatedness and the model output could be a factor. So they did additional regressions controlling for categorical relatedness, trial-by-trial frequency, and FAS, the results became less strong but was still significant (β-2.3 t-2.11 p0.03).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>They then computed likelihood with different precision parameter (how quickly/largely the agent changes their confidence based on the newest trial: from no change at all to completely flip their belief). And they found that υ=77 is the best fit (min1 max800). Which indicates real participants begin to give more weight to data in block2 than block1 around 77th trial (block 1 had 400 trials).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>They also compared log-transformed probability (surprisal) with raw probability (?), and found that surprisal but not probability accounted for variance in N400 amplitudes (??).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Overall I think they provided a working model of trial-by-trial adaptations on the N400. They also stressed that their model assuming the agent updating their belief on each trial may be just a simple way to look at things, and said the comprehender maybe could keep track of multiple sets of beliefs about the environmental statistics and is able to switch or adjust from model to model.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Reference</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Delaney-Busch, N., Morgan, E., Lau, E., &amp; Kuperberg, G. R. (2019). Neural evidence for Bayesian trial-by-trial adaptation on the N400 during semantic priming. <em>Cognition</em>, <em>187</em>, 10-20.</p>
<!-- /wp:paragraph -->
