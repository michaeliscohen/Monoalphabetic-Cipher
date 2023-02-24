<h1 align="center" id="title">Python Monoalphabetic Cipher</h1>

<p id="description">This program executes a monoalphabetic cipher in Python. Encryption and Decryption operations are supported. Usage of a monoalphabetic cipher for security is not recommended.</p>

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Encryption
*   Decryption
*   File IO

<h2>🛠️ Installation Steps:</h2>

<p>1. Clone this GitHub repo</p>

```
git clone https://github.com/michaeliscohen/Monoalphabetic-Cipher.git
```

<p>2. Create an input file</p>

```
touch in.txt
```

<p>3. Insert a text string into the input file WITHOUT whitespace</p>

```
example: thisisastringthatwillbeputthroughourcipher
```

<p>4. Make sure no whitespace is added at the end of the file</p>

```
perl -pi -e 'chomp if eof' in.txt
```

<p>5. Run the python program</p>

```
python3 mono.py in.txt out.txt seed(integer 50-10000) 1(encryption if decryption then use 0)
```
