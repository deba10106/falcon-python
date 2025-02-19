# Falcon Signature Example

This project demonstrates the implementation of post-quantum encryption using the Falcon algorithm through the `liboqs` library.

## Overview
The Falcon algorithm is a signature scheme that is designed to be secure against quantum attacks. This example focuses on generating a key pair, signing a message, and verifying the signature using the `liboqs` library.

## Usage
1. #### Clone this repository.
   ```bash
   git clone --depth=1 https://github.com/deba10106/falcon-python
   ```
2. #### Create a virtual environment.
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. #### Install liboqs-python
   ```bash
   git clone --depth=1 https://github.com/open-quantum-safe/liboqs-python
   cd liboqs-python
   pip install .
   cd ..
   ```
4. #### Install the required packages listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
5. #### Run the example script:
   ```bash
   python falcon_liboqs_example.py
   ```

## Expected Output
```bash
Original Message: b'Hello, World!'
Is the signature valid? True
Decrypted Message (Original): b'Hello, World!'
```




## License
This project is licensed under the MIT License.
