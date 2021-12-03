import hashlib
import bech32
import ecdsa
import hdwallets
import mnemonic
from hdwallets import BIP32DerivationError as BIP32DerivationError
from typing import TypedDict

DEFAULT_DERIVATION_PATH = "m/44'/118'/0'/0/0"
DEFAULT_BECH32_HRP = "dex"


class PrivateKey:

    def __init__(self, key: bytes) -> None:
        self._privkey = key

    def to_public_key(self) -> bytes:
        privkey_obj = ecdsa.SigningKey.from_string(self._privkey, curve=ecdsa.SECP256k1)
        pubkey_obj = privkey_obj.get_verifying_key()
        return pubkey_obj.to_string("compressed")

    def to_address(self, hrp: str = DEFAULT_BECH32_HRP) -> str:
        return pubkey_to_address(self.to_public_key(), hrp=hrp)

    def sign(self, message_bytes: bytes) -> bytes:
        privkey = ecdsa.SigningKey.from_string(self._privkey, curve=ecdsa.SECP256k1)
        signature_compact = privkey.sign_deterministic(
            message_bytes, hashfunc=hashlib.sha256, sigencode=ecdsa.util.sigencode_string_canonize
        )
        return signature_compact


class Wallet(TypedDict):
    seed: str
    derivation_path: str
    private_key: PrivateKey
    public_key: bytes
    address: str


def generate_wallet(
        *, path: str = DEFAULT_DERIVATION_PATH, hrp: str = DEFAULT_BECH32_HRP
) -> Wallet:
    while True:
        phrase = mnemonic.Mnemonic(language="english").generate(strength=256)
        try:
            privkey = seed_to_privkey(phrase, path=path)
            break
        except BIP32DerivationError:
            pass
    pubkey = privkey.to_public_key()
    address = pubkey_to_address(pubkey, hrp=hrp)
    return {
        "seed": phrase,
        "derivation_path": path,
        "private_key": privkey,
        "public_key": pubkey,
        "address": address,
    }


def seed_to_privkey(seed: str, path: str = DEFAULT_DERIVATION_PATH) -> PrivateKey:
    """Get a private key from a mnemonic seed and a derivation path.

    Assumes a BIP39 mnemonic seed with no passphrase. Raises
    `cosmospy.BIP32DerivationError` if the resulting private key is
    invalid.
    """
    seed_bytes = mnemonic.Mnemonic.to_seed(seed, passphrase="")
    hd_wallet = hdwallets.BIP32.from_seed(seed_bytes)
    # This can raise a `hdwallets.BIP32DerivationError` (which we alias so
    # that the same exception type is also in the `cosmospy` namespace).
    derived_privkey = hd_wallet.get_privkey_from_path(path)

    return PrivateKey(derived_privkey)


def pubkey_to_address(pubkey: bytes, *, hrp: str = DEFAULT_BECH32_HRP) -> str:
    s = hashlib.new("sha256", pubkey).digest()
    r = hashlib.new("ripemd160", s).digest()
    five_bit_r = bech32.convertbits(r, 8, 5)
    assert five_bit_r is not None, "Unsuccessful bech32.convertbits call"
    return bech32.bech32_encode(hrp, five_bit_r)

