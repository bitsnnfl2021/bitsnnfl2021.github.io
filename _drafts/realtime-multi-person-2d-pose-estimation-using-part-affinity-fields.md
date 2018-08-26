---
layout: post
share: true
title: Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields
date: 2018-08-26 07:54:45 +0530
author:
  name: Aakriti Agrawal
  email: f2015276@pilani.bits-pilani.ac.in
categories: []
tags: []

---
We present an approach to efficiently detect the 2D pose of multiple people in an image. The approach uses a nonparametric representation, which we refer to as Part Affinity Fields (PAFs), to learn to associate body parts with individuals in the image. The architecture encodes global context, allowing a greedy bottom-up parsing step that maintains high accuracy while achieving realtime performance, irrespective of the number of people in the image. The architecture is designed to jointly learn part locations and their association via two branches of the same sequential prediction process. Our method placed first in the inaugural COCO 2016 keypoints challenge, and significantly exceeds the previous state-of-the-art result on the MPII MultiPerson benchmark, both in performance and efficiency.   