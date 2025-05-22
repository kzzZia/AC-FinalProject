# AC-FinalProject

# 🔐SecureCrypt: A Cryptographic Web Application

**Course Name:** CSAC 329 – Applied Cryptography  
**Date:** May 2025  

---

## 👥 Group Members

- Garcia, Asi Neo
- Janda, Christian Paul 
- Mediado, Hyacinthe 
- Nanale, Krizia Belle 

---

## Access through this server:
https://ac-finalproject-2.onrender.com

---

## 📖 Introduction

**SecureCrypt** is a web-based cryptographic application built using Flask that allows users to securely encrypt, decrypt, and hash messages and files using various cryptographic algorithms. The application provides an intuitive UI for selecting and interacting with multiple symmetric, asymmetric, and hashing techniques. Cryptography is vital in protecting data confidentiality, integrity, and authenticity. In a digital age of increasing cyber threats, understanding and implementing cryptographic principles is fundamental to secure software systems.

---

## 🎯 Project Objectives

1. Implement and demonstrate at least 3 symmetric, 2 asymmetric, and 4 hashing cryptographic algorithms using Python.
2. Develop a user-friendly web interface for secure message and file processing using Flask.
3. Provide educational context and documentation about each cryptographic technique to enhance learning and usability.

---

## 💡 Discussions

The SecureCrypt application was developed to provide users with a hands-on platform for understanding and utilizing modern cryptographic techniques in a secure and interactive environment. By integrating multiple encryption, decryption, and hashing algorithms within a user-friendly web interface, the project aims to bridge the gap between theoretical cryptography and real-world application. Built using the Flask web framework, the application adopts a modular architecture that separates the frontend UI, backend logic, and cryptographic functions. This design ensures scalability, ease of maintenance, and clarity in both user experience and code structure. The user interface features a dark, cybersecurity-inspired theme with intuitive navigation, making it accessible to users with varying levels of technical knowledge.

From an educational and practical standpoint, SecureCrypt serves as both a learning tool and a secure application. It implements a wide range of algorithms including symmetric methods like XOR, Caesar, and AES; asymmetric approaches like RSA and Diffie-Hellman; and hashing algorithms such as SHA-256, SHA-1, MD5, and BLAKE2. Each algorithm is integrated using Python libraries like hashlib and pycryptodome, and is accessible via dedicated Flask routes that handle user input and display real-time cryptographic results. Through this approach, the application allows users to understand the strengths and limitations of each technique, experiment with encryption keys and plaintext, and observe the transformation of data in a secure environment. Ultimately, SecureCrypt emphasizes the importance of cryptographic literacy and demonstrates how foundational security principles can be applied in modern software systems.

In addition to its core cryptographic functionality, SecureCrypt also emphasizes the importance of user awareness and digital responsibility. By offering clear, accessible explanations of each algorithm’s purpose, background, and use case, the application encourages users to not only perform cryptographic operations but also understand why they matter in today’s digital landscape. This educational aspect is especially valuable for students and early-stage developers who are new to cybersecurity. Moreover, by supporting both classical and modern algorithms, the project provides historical context alongside contemporary relevance, showing how cryptography has evolved to meet increasingly complex security demands. Through its interactive design and well-documented features, SecureCrypt succeeds in transforming abstract security concepts into practical, hands-on experiences.

### ⚙️ Application Architecture and UI Choice

The SecureCrypt application is a web-based platform for cryptographic functionalities that has been built with the Flask framework. The architecture is developed modularly and in layers, so that the frontend (user interface), backend (Flask routes and logic), and the methods that perform cryptographic tasking are separated components within the system. Due to this modular design, the system allows for scaling, easy maintenance, and convenient debugging or future development tasks. The frontend has been rendered using HTML and CSS, while incorporating some custom styling to preserve a technically-modern dark themed user interface to reflect the secure and technical use of the application. Bright and neon accents (with an emphasis on cyan and orange) have been used for readability and for visual appeal; and to draw the user's eye towards interactive components like buttons or icons.

The homepage functions as a dashboard where a user is welcomed and provided user-friendly buttons for each supported cryptographic algorithm. Each button takes the user to a specific tool (e.g., XOR Cipher, RSA Cipher, Hashing Algorithms) through clearly defined Flask routes where a user can enter plaintext or ciphertext, select keys, and perform a cryptographic operation. The homepage's user-friendly design and lack of clutter allows for ease of use, even for a beginner, and the back-end layout allows a developer to add or edit cryptographic areas of the project without a significant impact on other areas of the system. Overall, design and architecture work together to provide a seamless educational and secure user experience.

### 🔐 Implemented Cryptographic Algorithms

The SecureCrypt application implements the following types of cryptographic algorithms for encryption, decryption, key exchanges, and hashing. The XOR Cipher is a symmetric algorithm that utilizes the bitwise XOR function with a repeating key implemented with basic Python operations. The Caesar Cipher is also a symmetric method with a known shift value that changes letters by a pre-determined value and can be implemented with Python string manipulation. The Diffie-Hellman algorithm is also secure key exchange; it can be implemented over discrete logarithms, and I built a simulation of Diffie-Hellman that generated random integers and used the pow() function defined in Python. The RSA Cipher is asymmetric where there are two keys; the public and private key, and I also only utilized the pycryptodome libraries for implementation. The Block Cipher module is predefined for a fixed number of bytes (block size), which is likely the AES (Advanced Encryption Standard) algorithm as there is a process known as padding, and the block cipher uses only symmetric keys, and I also built this with the pycryptodome libraries. Hashing Algorithms like SHA-256 and MD5 will hash incoming data and is one-way; I implemented these with Python's hashlib. Each of the algorithms were integrated into SecureCrypt using Flask routes to demonstrate the aforementioned cryptographic activities using backend handlers and provide the user with a unique experience during the cryptographic process.

## 📸 Sample Runs / Outputs
Dashboard
![image](https://github.com/user-attachments/assets/d487d1fd-a7f7-4265-90ac-45433204c430)
Layout Dashboard
![image](https://github.com/user-attachments/assets/876095eb-df41-4121-81cf-b71a84276e1e)



