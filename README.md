# About the author
![cv](cv.png)

# Falcon Post-Quantum Signature Implementation

## Overview
The Falcon algorithm is a signature scheme that is designed to be secure against quantum attacks. This implementation demonstrates the generation of a key pair, signing a message, and verifying the signature using the `liboqs` library. Falcon is one of the finalists in the NIST Post-Quantum Cryptography standardization process, known for its compact signatures and efficient verification.

## Key Features
- Post-quantum secure digital signatures
- Based on the NIST-standardized Falcon algorithm
- Uses the well-maintained `liboqs` library
- Simple Python implementation
- Suitable for educational and research purposes

## Usage
1. #### Clone this repository
   ```bash
   git clone --depth=1 https://github.com/deba10106/falcon-python
   ```
2. #### Create a virtual environment
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
4. #### Install the required packages
   ```bash
   pip install -r requirements.txt
   ```
5. #### Run the example script
   ```bash
   python falcon_liboqs_example.py
   ```

## Expected Output
```bash
Original Message: b'Hello, World!'
Is the signature valid? True
Decrypted Message (Original): b'Hello, World!'
```

## Applications
1. **Digital Signatures**: Secure document signing that remains secure even against quantum computers.
2. **Authentication Systems**: Verifying the identity of users or systems in a post-quantum secure manner.
3. **Blockchain**: Implementing quantum-resistant transaction signatures in blockchain networks.
4. **Secure Communication**: Ensuring message authenticity in communication protocols.
5. **Software Distribution**: Signing software packages and updates with quantum-resistant signatures.

## Technical Details
### Falcon Algorithm
Falcon (Fast-Fourier Lattice-based Compact Signatures over NTRU) is a lattice-based signature scheme with the following characteristics:
- Based on the NTRU (N-th degree TRUncated polynomial ring) problem
- Provides a good balance between signature size and key size
- Offers fast signature generation and verification
- Designed to be resistant against both classical and quantum attacks

### Security Level
The implementation uses Falcon-1024, which provides:
- 256-bit classical security
- 128-bit post-quantum security
- NIST Security Level 5

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## How to Cite
If you use this implementation in your research, please cite it as follows:

### BibTeX
```bibtex
@misc{falcon_python_implementation,
  author = {Debasis Mondal},
  title = {Falcon Post-Quantum Signature Implementation},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/deba10106/falcon-python}
}
```

### APA
```
Mondal, D. (2025). Falcon Post-Quantum Signature Implementation [Computer software]. 
GitHub. https://github.com/deba10106/falcon-python
```

## Further Reading
1. [NIST Post-Quantum Cryptography Standardization](https://csrc.nist.gov/projects/post-quantum-cryptography)
2. [Falcon Official Documentation](https://falcon-sign.info/)
3. [Open Quantum Safe Project](https://openquantumsafe.org/)

## License
This project is licensed under the MIT License.

## Contact
- **Author**: Debasis Mondal
- **GitHub**: [@deba10106](https://github.com/deba10106)
