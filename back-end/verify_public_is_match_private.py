# 检查公私钥是否匹配
from collections import namedtuple

try:
    from hashlib import sha3_256
except ImportError:
    from sha3 import sha3_256

from cryptoconditions import crypto

CryptoKeypair = namedtuple('CryptoKeypair', ('private_key', 'public_key'))

PrivateKey = crypto.Ed25519SigningKey
PublicKey = crypto.Ed25519VerifyingKey


def key_pair_from_ed25519_key(hex_private_key):
    """Generate base58 encode public-private key pair from a hex encoded private key"""
    priv_key = crypto.Ed25519SigningKey(bytes.fromhex(hex_private_key)[:32], encoding='bytes')
    public_key = priv_key.get_verifying_key()
    return CryptoKeypair(private_key=priv_key.encode(encoding='base58').decode('utf-8'),
                         public_key=public_key.encode(encoding='base58').decode('utf-8'))


def public_key_from_ed25519_key(hex_public_key):
    """Generate base58 public key from hex encoded public key"""
    public_key = crypto.Ed25519VerifyingKey(bytes.fromhex(hex_public_key), encoding='bytes')
    return public_key.encode(encoding='base58').decode('utf-8')


def hash_data(data):
    """Hash the provided data using SHA3-256"""
    return sha3_256(data.encode()).hexdigest()


import base64
import base58
import nacl.signing
import nacl.encoding
import nacl.exceptions

from cryptoconditions import exceptions


class Base58Encoder(object):

    @staticmethod
    def encode(data):
        return base58.b58encode(data)

    @staticmethod
    def decode(data):
        return base58.b58decode(data)


def _get_nacl_encoder(encoding):
    if encoding == 'base58':
        return Base58Encoder
    elif encoding == 'base64':
        return nacl.encoding.Base64Encoder
    elif encoding == 'base32':
        return nacl.encoding.Base32Encoder
    elif encoding == 'base16':
        return nacl.encoding.Base16Encoder
    elif encoding == 'hex':
        return nacl.encoding.HexEncoder
    elif encoding is 'bytes':
        return nacl.encoding.RawEncoder
    else:
        raise exceptions.UnknownEncodingError("Unknown or unsupported encoding")


def verify_public_is_match_private(public_key, private_key):
    try:
        temp = Base58Encoder.decode(private_key)

        private_hex = _get_nacl_encoder('hex').encode(temp)

        private_hex_s = str(private_hex, encoding="utf-8")

        test = key_pair_from_ed25519_key(private_hex_s)
    except:
        print("fail！")
        return 0
    else:
        if test[1] == public_key:
            print("sucess")
            return 1
        else:
            print("fail")
            return 0
