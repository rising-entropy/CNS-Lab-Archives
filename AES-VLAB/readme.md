We would have to perform in all the 4 modes

Cipher Block Chaining
Image 5 -> Generate the values

Plaintext:
 da7127a2 a3692fc2 afad8461 6293af56
 0b2bef88 e9e84baf e5755065 f6f1fbcc
 77cd0fb1 189e9661 4bc45e58 168b02a5
 84dc26fe fcb0dc76 1e438824 745d8413
 b986edec 12be7882 36b550aa 6042c495

Key:
 ed9fe343 4d2b726d ee3442da 3f2ce730

IV:  2fa2a879 71a90e72 6feb2e39 346e10d3

First, take message block 1 and XOR with IV
then take that Cipher and Encrypt with the key
And add that result to the final output

 0c102695 c6d5a02a f39ff2e4 ad34daff

Now, we take the previously generated Cipher and XOR with Plaintext of 2nd part
Then Encrypt with Key and Append to the final output

 1678243f 83ad3468 371702b9 9271dcbd

We repeat this procedure for all Plaintext

 89801e77 e52dc587 59bd4788 365fa2c1

  f02d4d27 38b7552b 374d15e1 a8d4abf8
  df17459e 094dd59d 48db4e0c 7e38f3ff

Encryption:   0c102695 c6d5a02a f39ff2e4 ad34daff b456d318 268261b7 9abd2009 c8240b4f 89801e77 e52dc587 59bd4788 365fa2c1 f02d4d27 38b7552b 374d15e1 a8d4abf8 df17459e 094dd59d 48db4e0c 7e38f3ff
