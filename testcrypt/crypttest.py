import hashlib
import hmac

def start_process():
    key = 'some-key'
    value = 'password'
    dlist = ['md5','sha1','sha224','sha256','sha384','sha512']
    for digest in dlist:
    	hashed = hmac_hash(value, key, digest, None)
    	print 'hmac:%s: %s' % (digest, hashed)
	pass

def get_digest(value):
    """
    Returns a hashlib digest algorithm from a string
    """
    if not isinstance(value,str):
        return value
    value = value.lower()
    if value == "md5":
        return hashlib.md5
    elif value == "sha1":
        return hashlib.sha1
    elif value == "sha224":
        return hashlib.sha224
    elif value == "sha256":
        return hashlib.sha256
    elif value == "sha384":
        return hashlib.sha384
    elif value == "sha512":
        return hashlib.sha512
    else:
        raise ValueError("Invalid digest algorithm")


def hmac_hash(value, key, digest_alg='md5', salt=None):
    if ':' in key:
        digest_alg, key = key.split(':')
    digest_alg = get_digest(digest_alg)
    d = hmac.new(key,value,digest_alg)
    if salt:
        d.update(str(salt))
    return d.hexdigest()


if __name__ == "__main__":
	start_process()
