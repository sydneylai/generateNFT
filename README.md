## Step-by-step tutorial: 
https://dev.to/sydneylai/create-and-host-nfts-with-25-lines-of-code-4l4e
## Video Tutorial: 
https://youtu.be/gfkWJTBqHuE


Author: [@sydneylai](https://twitter.com/sydneylai)

You often hear about the 10,000 NFT collection, but how does someone make thousands of unique images? Today we will build an algorithmically generate image dataset and host them on IPFS as a unique NFT. 

We host the images in [IPFS](https://ipfs.io/) because this a peer to peer and a decentralized form of storage, rather than a centralized solution like AWS or Google Cloud. Therefore if AWS goes down or you forget to pay your Cloud subscription, you still have a hosting solution that assigned a unique identifier or content identifier (CID).

Once you have a unique image, you can either distribute your NFTs on a marketplace, put it on a smart contract or turn it into a game. I'll include resources below for how else you can continue to build.

**Tools you'll need:**

- Python
- [Pillow Library](https://pillow.readthedocs.io/en/stable/)
- [NFT Storage](https://nft.storage/)
