---
layout: post
author:
  name: Paper ID 17
  difficulty: medium
share: true
title: Delete, Retrieve, Generate:A Simple Approach to Sentiment and Style Transfer
categories:
- Natural Language Processing
- Style Transfer
- medium

tags: []

---
**Abstract** - We consider the task of text attribute transfer:transforming a sentence to alter a specific at-tribute (e.g., sentiment) while preserving itsattribute-independent content (e.g., changing“screen is just the right size”to“screen is toosmall”). Our training data includes only sen-tences labeled with their attribute (e.g., pos-itive or negative), but not pairs of sentencesthat differ only in their attributes, so we mustlearn to disentangle attributes from attribute-independent content in an unsupervised way.Previous work using adversarial methods hasstruggled to produce high-quality outputs. Inthis paper, we propose simpler methods mo-tivated by the observation that text attributesare often marked by distinctive phrases (e.g.,“too small”). Our strongest method extractscontent words by deleting phrases associatedwith the sentence’s original attribute value, re-trieves new phrases associated with the targetattribute, and uses a neural model to fluentlycombine these into a final output. On humanevaluation, our best method generates gram-matical and appropriate responses on22%more inputs than the best previous system, av-eraged over three attribute transfer datasets:altering sentiment of reviews on Yelp, alteringsentiment of reviews on Amazon, and alteringimage captions to be more romantic or humor-ous

**Paper** - [https://arxiv.org/pdf/1804.06437.pdf](https://arxiv.org/pdf/1804.06437.pdf)

**Dataset -** [https://github.com/rpryzant/delete_retrieve_generate/tree/master/data](https://github.com/rpryzant/delete_retrieve_generate/tree/master/data)
    