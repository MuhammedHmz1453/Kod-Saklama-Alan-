# calculator_cli.py
import math

def islemler():
    print("""
Basit Hesap Makinesi
Kullanım:
  +   toplama
  -   çıkarma
  *   çarpma
  /   bölme
  **  üs (ör. 2 ** 3)
  sqrt x  (karekök; ör: sqrt 9)
  q   çıkış
Örnek: 3 + 4
""")

def deger_parsela(expr):
    # "sqrt 9" desteklemek için ayrı kontrol
    expr = expr.strip()
    if expr.startswith("sqrt "):
        _, val = expr.split(maxsplit=1)
        return math.sqrt(float(val))
    # güvenli olmayan eval'i sınırlamak için izin verilen karakter kontrolleri
    allowed = "0123456789.+-*/() **e"
    for ch in expr:
        if ch.isalpha() and ch not in ("e",):
            raise ValueError("Geçersiz ifade veya izin verilmeyen karakter.")
    # Basitçe eval kullanıyoruz ama yalnızca temel aritmetiğe izin verilmeli
    return eval(expr, {"__builtins__": None, "math": math})

def main():
    islemler()
    history = []
    while True:
        try:
            s = input(">>> ").strip()
            if not s:
                continue
            if s.lower() in ("q", "quit", "exit"):
                print("Çıkış. Görüşürüz!")
                break
            if s.lower() == "history":
                for i, (expr, res) in enumerate(history, 1):
                    print(f"{i}: {expr} = {res}")
                continue
            result = deger_parsela(s)
            print("=", result)
            history.append((s, result))
        except Exception as e:
            print("Hata:", e)

if __name__ == "__main__":
    main()
