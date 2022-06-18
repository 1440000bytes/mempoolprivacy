# mempoolprivacy

![image](https://user-images.githubusercontent.com/94559964/174421798-46463c84-59f3-4984-acdc-57ae092f3953.png)



### Usage

There are 2 nodes running and GET request will return results for `getrawmempool` for these nodes. Node 2 has `spekreuse=conflict` saved _bitcoin_rw.conf_ file.

Chain: Signet  
Implementation: Bitcoin Knots

Request:

```http
GET /mempool?node=1 HTTP/1.1
Host: spkreuse.fun
Content-Type: application/json
```
Response:

```
{
    "error": null,
    "id": "txid",
    "result": [
        "3ee3410b2f159787604dad78e531947509c6077912d83888a61782d9fb5c3df7",
        "18bd6d09cded20c35087b236b1ff1dbf148e6c595fd916a0fedafd8ab72aefe1",
        "72c0d0f38c2ace02e6a9e75ddfef53f32b8fdc878f7b9170ade7069fdf590cd6",
        "c2bc84eb188b0a6bd84b96c39684eb301c97664c456021d215253596c83016b6",
        "ee1be4c064feeca731b766e0036b3310a2a7353d090b14ae558ae8f21e9914b5",
        "937f52129f69435020cf15f182cb3c6372a8edd38b07647e63ef254eabbc52b2",
        "68615ce6adaa77a149b17bd2a146a53a56dc9495859dd92904a0fd43587e3e84",
        "778c35b0a8fefbcba1dbd61e5fb4579642e2d00fee3af4584ade5d757e61c04d",
        "36bbc468ba0abb25be4a0a5795ad33058d588a13656382651b76127f823b573e",
        "aeb0e6ed1f007c8b901b50fba63f8d45470f34a2d3a5982f256066ae3ea8113a",
        "e6f61f3067c8678650624ee78370a7123fa349fb5de150e1f3e3ed6cfe733b24",
        "71c4a83ad23f99daeba83b3f25316f67110ff392c7ef974203d7e2b33e1ac423",
        "d0c9ff00290cd259e68c5d487c71c584f57279ce1650fb98a91a98325aa56b1e",
        "ed6c63e2391764dacccd95a4fadab25d0494cae37ed90bc14b856abcc6f1a312",
        "7b18c28b924ae6dfb35481c734da0822dc38316444c2cdfccd5e753ed7b61800"
    ]
}
```

To run the API locally change credentials in [api.py](https://github.com/1440000bytes/mempoolprivacy/blob/main/api.py) and run it using flask (python)

Mempool transactions for two nodes will be differemt when node 2 does not allow transactions with address reuse. JSON output can be used to create tables, highlight difference etc. Example python script to get the difference between mempool of 2 nodes [diff.py](https://github.com/1440000bytes/mempoolprivacy/blob/main/diff.py) will return [diff](https://github.com/xlwings/jsondiff) for 2 JSON:

```
{insert: [(5, 'fee0cc08b1fbd051ad0170bccc1028f3a964c9734a55e4a2ea626bb71222de6a')]}

{delete: [86, 68, 50, 16]}

{}
```



