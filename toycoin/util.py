from Crypto.Hash import SHA256, RIPEMD160
import base58

def keypub_to_address(key_pub):
    keypubhash = keypub_to_keypubhash(key_pub.hex())
    return base58.b58encode(keypubhash)

def keypub_to_keypubhash(key_pub):
    h = SHA256.new()
    r = RIPEMD160.new()
    b = bytearray()
    b.extend(map(ord, key_pub))
    h.update(b)
    bb = bytearray()
    bb.extend(map(ord, h.hexdigest()))
    r.update(bb)
    return r.hexdigest()
