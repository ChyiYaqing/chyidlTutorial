#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# linked_list_LRU_implement.py
# python
#
# 🎂"Here's to the crazy ones. The misfits. The rebels.
# The troublemakers. The round pegs in the square holes.
# The ones who see things differently. They're not found
# of rules. And they have no respect for the status quo.
# You can quote them, disagree with them, glority or vilify
# them. About the only thing you can't do is ignore them.
# Because they change things. They push the human race forward.
# And while some may see them as the creazy ones, we see genius.
# Because the poeple who are crazy enough to think thay can change
# the world, are the ones who do."
#
# Created by Chyi Yaqing on 02/14/19 17:59.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Interview Question

Software Engineer Interview

"" Design an LRU cache. It's a data struct with a capacity. Beyond this
capacity the least recently used item is removed. You should be able to insert
an element, access and element given its key,and  delete an element,in contant
time. Note that when you access an element,event if it's just for a read,it
becames the most recently used"

Doubly linked and HashMap, insert to the top of the list
"""
