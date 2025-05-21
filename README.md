# AC-FinalProject

# 🔐SecureCrypt: A Cryptographic Web Application

**Course Name:** CSAC 329 – Applied Cryptography  
**Date:** May 2025  

---

## 👥 Group Members

- Garcia, Asi Neo
- Janda, Christian Paul 
- Mediado, Hyachinthe 
- Nanale, Krizia Belle 

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

SecureCrypt was developed as a cryptographic web application to bridge the gap between theoretical cryptography and its practical implementation. With the growing demand for data privacy and secure communication, it is essential for both developers and users to understand how encryption, decryption, and hashing algorithms operate in real-world environments. This project aimed to demonstrate that cryptographic concepts could be implemented, tested, and interacted with through a modern, user-friendly interface.

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



