---
layout: post
permalink: blog/blog60/
categories: [Finance]
---

![](https://cdn-images-1.medium.com/max/2600/0*2ViIIvP73S67AcIZ)
Photo by [Pascal Bernardon](https://medium.com/r/?url=https%3A%2F%2Funsplash.com%2F%40pbernardon%3Futm_source%3Dmedium%26utm_medium%3Dreferral) on [Unsplash](https://medium.com/r/?url=https%3A%2F%2Funsplash.com%3Futm_source%3Dmedium%26utm_medium%3Dreferral)

<!--end_excerpt-->

# Introduction to Bitcoin and the Blockchain

## Demystifying some of the common misunderstandings about how the Bitcoin and Blockchain community infrastructure works.

### Introduction

The Bitcoin blockchain is a decentralised and democratic model. Miners (users who try to contribute to the blockchain through a Proof of Work) are given the power to expand the blockchain adding new blocks (updating the “ledger”) and the different transactions are then formally accepted if they archive the consensus of the majority of users. This process is performed automatically within the protocol by considering the record of blocks in the blockchain which required the greatest computational power to be constructed as the one represented by the majority of the users. Therefore, this protocol is governed by its own users and the winning miners have the power to write a part of the code in order to add new blocks to the blockchain.

The overall Blockchain workflow is exemplified in Figure 1.

![](https://cdn-images-1.medium.com/max/1200/1*0A5O3Cobb-uHIlfGvkYy7A.png) <br>
Figure 1: Blockchain Workflow ([Image Source](https://medium.com/r/?url=https%3A%2F%2Fcryptolume.co%2Fpros-and-cons-of-blockchain-technology%2F))

The maximum number of Bitcoins is 21 million, although the actual quantity will most likely be a bit lower than this taking into account that Bitcoins are represented with a limited number of decimals (8). This number can be calculated by considering that: every new block added on the blockchain originally introduced 50 new Bitcoins into the system, this amount is then halved every 210000 added blocks and a maximum of 33 halving events can take place (due to the limited decimal representation).

The last Bitcoin will be mined when the block reward will go below one Satoshi (which should happen within the 33rd halving period).

With the Bitcoin rewards assigned to miners halving every four years, the block transaction fees will most likely become the main form of income for the miners in the future. Therefore, in order to incentivize miners to work for the community, the transactions fees might vary in line with the supply/demand relationship of the network. In fact, if miners would be no more stimulated to maintain updated the blockchain, it would be not anymore possible to keep updated the blockchain without a central point of authority. Transaction fees might, therefore, be considered in their function as taxes necessary in order to ensure the correct functioning of the system.

### Upcoming Challenges

#### Animosity

The Bitcoin protocol is not considered to be completely anonymous but pseudo-anonymous. In fact, although being designed to be secure, some techniques have been ideated throughout the years in order to undermine its safety. Two reasons why the Bitcoin protocol can be considered to be secure are \[1\]:

-   On a protocol level, addresses and transactions are not connected to users identities.
-   Bitcoin transaction data propagates through a random subset of the network nodes.

Instead, some examples of approaches which can be used in order to undermine the safety of transactions are:

-   An attacker might be able to retrieve enough information (so that to infer where a transaction was originated) by connecting multiple nodes to the bitcoin network.
-   All Bitcoin transactions are visible on the network, therefore, it can be possible to cluster together Bitcoin addresses connected to same users (deanonymizing the system).

Some possible approaches which can be used in order to prevent privacy breaches when using the Bitcoin protocol are to hide the used IP (Internet Protocol) address or change the IP address used for each transaction.

#### Double Spending Attack

Double spending is a type of attack which aims to erase a transaction from the blockchain by building a competing fork able to achieve wide consensus where the performed transaction is not recorded (therefore allowing the user to spend money on a good, receive the good and keep the initial amount of money spent).

![](https://cdn-images-1.medium.com/max/1200/1*And1qS26SpSxpUKvivBfHw.jpeg)
<br>
Figure 2: Double Spending Attack ([Image Source](https://medium.com/r/?url=https%3A%2F%2Fcoinsutra.com%2Fbitcoin-double-spending%2F))

When forks are created in the blockchain, the network successively achieves consensus by accepting the chain of blocks with most Proof of Work (amount of processing power consumed to create this chain of blocks). Usually, the chain with most Proof of Work is also the chain containing the greatest number of blocks. Consensus mechanisms such as Proof of Work incentives miners to act truthfully (trying to deceive the network would most likely lead to a loss for them). One possible way miners might manage to make the system vulnerable is by controlling at least 51% of the total network processing power (making double-spending feasible). Another problematic of Proof of Work as a consensus mechanism is it’s moderate velocity to reach consensus (although this can lead to an increase in security).

#### Limited block size and Scalability

Increasing block size would allow for more transactions to be contained in a block and would potentially give less importance to transaction fees (more lower transaction fees could be processed faster). Additionally, using a larger block size would make the blocks move at a slower rate through the network (increasing the likelihood and length of forks and therefore of attacks on the blockchain). On the other hand, decreasing the block size would give more importance to transaction fees and would allow for fewer transactions to be processed at the time.

Another possible approach to process more transactions faster in the Bitcoin protocol, could be to reduce the block generation interval. Although, also this approach would then lead to an increase in the number of forks in the network and consequently a decrease in security. Bitcoin scalability is additionally heavily dependent on factors such as: storage requirements, network bandwidth and size.

#### Execution Speed

One of the main problems of the Proof of Work consensus algorithms is its limited execution speed. SegWit2x and Lighting Network (LN) are two examples of techniques proposed in order to speed up transactions executions in the Bitcoin protocol (making this system more easily scalable). SegWit2x was designed in order to increase the allowable block size from 1 MB to 2 MB by creating a hard fork in the system. This approach has currently been rejected by the majority of the users since it might cause the risk of dividing the whole network into two concurrent branches. The use of SegWit (an earlier version of SegWit2x which uses instead a soft fork and is backwards-compatible) allowed successively the creation of Lightning network.

SegWit allows for a faster transaction execution speed by restructuring the block data so that signatures are not stored in conjunction with the transaction data. Both SegWit and Lighting Network are used in order process transactions faster, but Lightning Network is a second-layer protocol and therefore is not embedded in the blockchain itself but is built on the top of the network \[2\].

### Bibliography

\[1\] Is Bitcoin Anonymous? A Complete Beginners Guide Bitcoin Magazine. Accessed at: [https://bitcoinmagazine.com/articles/is-bitcoin-anonymous-a-complete-beginner-sguide-1447875283](https://medium.com/r/?url=https%3A%2F%2Fbitcoinmagazine.com%2Farticles%2Fis-bitcoin-anonymous-a-complete-beginner-sguide-1447875283), February 2020.

\[2\] A Beginners Guide to Segregated Witness (SegWit) Binance Academy. Accessed at: [https://www.binance.vision/blockchain/a-beginners-guide-to-segretated-witness-segwit](https://medium.com/r/?url=https%3A%2F%2Fwww.binance.vision%2Fblockchain%2Fa-beginners-guide-to-segretated-witness-segwit), February 2020.
