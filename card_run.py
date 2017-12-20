# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import card_loader
import network
#old net = network.Network([208, 30, 52])
#old net.SGD(train, 30, 10, 3.0, test_data=test)

#49%
#second net = network.Network([208, 60, 52])
#second net.SGD(train, 60, 10, 3.0, test_data=test)

# 84.27%
#third net = network.Network([208, 30, 52])
#third net.SGD(train, 60, 10, 3.0, test_data=test)

#86.62%
#fourth net = network.Network([208, 20, 52])
#fourth net.SGD(train, 60, 10, 3.0, test_data=test)

#63.65%
#fifth net = network.Network([208, 10, 52])
#fifthnet.SGD(train, 60, 10, 3.0, test_data=test)

#78.94
#six net = network.Network([208, 15, 52])
#six net.SGD(train, 60, 10, 3.0, test_data=test)

#89.46% with nums60k.json
#84.28% with randmap60k.json 
net = network.Network([208, 22, 52])
net.SGD(train, 60, 10, 3.0, test_data=test)
