
|    NRP     |      Name      |
| :--------: | :------------: |
| 5025241181 | Muhammad Naufal Hadaya Setiawan |
| 5025241153 | Kamal Zaky Adinata |
| 5025241151 | Adrian Afzal Zaidana |


1. IMPORT LIBRARY
```
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from sympy import symbols
```

Penjelasan :
- numpy → Untuk membuat array x (untuk plotting)
- matplotlib.pyplot → Untuk menampilkan grafik fungsi
- sympy → Untuk memproses ekspresi matematika simbolik (aljabar)
- parse_expr → Mengubah string input seperti 'x**2 - 3' menjadi ekspresi matematika sympy
- symbols → Untuk mendefinisikan simbol variabel x


2. FUNGSI REGULA FALSI
```
def regula_falsi(func_expr, a, b, tol=1e-5, max_iter=100):
```

Penjelasan : 
- func_expr → ekspresi f(x)
- a, b → batas bawah dan atas
- tol → toleransi error (misal |f(c)| < 10⁻⁵)
- max_iter → batas maksimal iterasi

Di dalamnya :
- Ubah f(x) jadi fungsi numerik dengan:
  ```
  f = sp.lambdify(x, func_expr, 'numpy')
  ```
  - Lakukan iterasi hingga menemukan akar atau mencapai iterasi maksimum.
  - Setiap iterasi:
    ```
    c = b - (fb * (b - a)) / (fb - fa)
    ```
    Ini adalah rumus Regula Falsi (false positition)
    - Jika |f(c)| < tol, berarti c adalah akar.
    - Periksa Tanda :
        - Kalau f(a) × f(c) < 0 → akar ada di [a, c] → ubah b = c
        - Kalau f(b) × f(c) < 0 → akar ada di [c, b] → ubah a = c
