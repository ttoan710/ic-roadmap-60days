1. Bài toán

Cộng 2 bit:

A + B

👉 Kết quả gồm 2 phần:

Sum (S) → bit kết quả 
Carry (C) → bit nhớ
⚡ 2. Truth table
A B | S C
0 0 | 0 0
0 1 | 1 0
1 0 | 1 0
1 1 | 0 1
🔥 3. Rút ra công thức
Sum (S)

Nhìn bảng:

S = 1 khi A ≠ B

👉 chính là XOR:

S = A ⊕ B
Carry (C)
C = 1 khi A = 1 và B = 1

👉

C = A · B