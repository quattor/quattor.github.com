---
layout: article
title: A possible package repository architecture for upgrading with Yum
category: review
---

## Introduction

The new SPMA makes it easy to install new packages, and their
dependencies.  However, there may be dependencies that are not part of
the profile and that might get updated at random times.

We want to avoid such uncontrolled upgrades.  One way to avoid them is
to do the old-style package management: specify everything in the
profile, and fix the dependency hell "manually".  This document
proposes a different way to prevent these random upgrades, by taking
snapshots of the Yum repositories.
