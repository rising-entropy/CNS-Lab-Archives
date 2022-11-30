from aes import aes

mk = 0x000102030405060708090a0b0c0d0e0f
pt = 0x00112233445566778899aabbccddeeff

cipher = aes.aes(mk, 128)
ct = cipher.enc_once(pt)
print(ct)
print("0x"+hex(aes.utils.arr8bit2int(ct))[2:].zfill(32))

pr = cipher.dec_once(ct)
print(pr)
print("0x"+hex(aes.utils.arr8bit2int(pr))[2:].zfill(32))