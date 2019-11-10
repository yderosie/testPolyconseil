import hashlib
import time
import json

# block d'exemple pour la mesure du hash rate
block = {
    "hash":"0000000000000000000000000000000000000000000000000000000000000000",
    "ver":1,
    "prev_block":"0000000000000000000000000000000000000000000000000000000000000000",
    "mrkl_root":"0000000000000000000000000000000000000000000000000000000000000000",
    "time":1322131230,
    "bits":437129626,
    "nonce":0,
    "n_tx":22,
    "size":100000,
    "block_index":818044,
    "main_chain":True,
    "height":154595,
    "received_time":1322131301,
    "relayed_by":"255.255.255.255",
    "tx":[]
}
nonce = 0

def getHashRate():
    # mesure du hash rate par seconde
    start_time = time.time()
    while (time.time() - start_time <= 1):
        block["nonce"] += 1
        hash_result = hashlib.sha256(json.dumps(block).encode()).hexdigest()
    return block["nonce"]


def scalingDifficulty(target_time):
    global block, nonce
    power = 1

    if (nonce == 0):
        nonce = getHashRate()

    while (16**power / nonce < target_time):
        power += 1

    if (abs((16**power / nonce) - target_time) > abs((16**(power - 1) / nonce) - target_time)):
        return power - 1

    return power


print(scalingDifficulty(200))
print(scalingDifficulty(600))
print(scalingDifficulty(30))
print(scalingDifficulty(120))
print(scalingDifficulty(10))
print(scalingDifficulty(1))
