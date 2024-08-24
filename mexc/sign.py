import json
import random
import string
import hashlib
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from base64 import b64encode
from time import time


def get_data(fp_data, info, auth):

    ts = str(int(time() * 1000))

    chash = "".join(random.choice(string.hexdigits.lower()) for _ in range(32))
    key = get_random_bytes(32)
    p0 = get_p0(json.dumps(fp_data), key)
    k0 = get_k0(key)

    data = {
        **info,
        "p0": p0,
        "k0": k0,
        "chash": chash,
        "mtoken": fp_data["mtoken"],
        "ts": ts,
        "mhash": fp_data["mhash"],
    }

    hash = get_sign(auth, json.dumps(data), ts)

    return data, hash, ts


def encrypt_aes_gcm_256(plaintext, key_hex):
    key = bytes.fromhex(key_hex)
    iv = get_random_bytes(12)
    cipher = AES.new(key, AES.MODE_GCM, iv)
    ciphertext, auth_tag = cipher.encrypt_and_digest(plaintext.encode("utf-8"))
    encrypted_message = iv + ciphertext + auth_tag
    encrypted_message_base64 = b64encode(encrypted_message).decode("utf-8")
    return encrypted_message_base64


def get_p0(plaintext_object_str, key):
    return encrypt_aes_gcm_256(plaintext_object_str, key.hex())


def get_k0(aes_key):
    public_key_str = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqqpMCeNv7qfsKe09xwE5o05ZCq/qJvTok6WbqYZOXA16UQqR+sHH0XXfnWxLSEvCviP9qjZjruHWdpMmC4i/yQJe7MJ66YoNloeNtmMgtqEIjOvSxRktmAxywul/eJolrhDnRPXYll4fA5+24t1g6L5fgo/p66yLtZRg4fC1s3rAF1WPe6dSJQx7jQ/xhy8Z0WojmzIeaoBa0m8qswx0DMIdzXfswH+gwMYCQGR3F/NAlxyvlWPMBlpFEuHZWkp9TXlTtbLf+YL8vYjV5HNqIdNjVzrIvg/Bis49ktfsWuQxT/RIyCsTEuHmZyZR6NJAMPZUE5DBnVWdLShb6KuyqwIDAQAB
-----END PUBLIC KEY-----"""
    public_key = RSA.import_key(public_key_str)
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted = cipher_rsa.encrypt(aes_key)
    return b64encode(encrypted).decode("utf-8")


def get_md5(string):
    return hashlib.md5(string.encode("utf-8")).hexdigest()


def get_g(auth, ts):
    md5_hash = get_md5(auth + ts)
    return md5_hash[7:], ts


def get_sign(auth, formdata, ts):
    g, current_ts = get_g(auth, ts)
    return get_md5(current_ts + formdata + g)
