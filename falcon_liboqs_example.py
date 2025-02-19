from oqs.oqs import Signature

def create_falcon_signature():
    # Generate a Falcon key pair
    signer = Signature('Falcon-1024')
    
    # Generate key pair and get public key
    public_key = signer.generate_keypair()
    
    # Optionally get the secret key for storage
    secret_key = signer.export_secret_key()
    
    return signer, public_key, secret_key

# Create a key pair
signer, public_key, secret_key = create_falcon_signature()

# Message to sign
message = b'Hello, World!'
print('Original Message:', message)

# Sign the message
signature = signer.sign(message)


# Create a new instance for verification
verifier = Signature('Falcon-1024')

# Verify the signature using the public key
is_valid = verifier.verify(message, signature, public_key)
print('Is the signature valid?', is_valid)

# Print the original message again to confirm it
print('Decrypted Message (Original):', message)


# Print results
# print('Public Key Length:', len(public_key))
# print('Secret Key Length:', len(secret_key))
# print('Signature Length:', len(signature))

# Clean up
signer.free()
verifier.free()