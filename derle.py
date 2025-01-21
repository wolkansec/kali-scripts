#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import py_compile

print("Derleme Programı")
derle = raw_input("\nProgramın İsmini Girin: ")
py_compile.compile(derle)
