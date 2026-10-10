#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Otomatik Mazeret Üreteci v2.0
Dünyanın en güvenilir (ve en saçma) mazeret kaynağı.
Bu program sayesinde artık "neden geç kaldın?" sorusuna cevap veremeyeceksin çünkü cevap zaten hazır.
"""

import random
import sys

def uret_mazeret():
    nedenler = [
        "Otobüs şoförü aniden felsefe dersine başladı ve ben de dinlemek zorunda kaldım.",
        "Kedi masanın üstüne oturdu ve kalkmadı, ben de bekledim çünkü o da bir canlı.",
        "İnternet bağlantım uzaylılar tarafından geçici olarak kesildi, resmi belgesi var (yok).",
        "Saatler birdenbire geriye doğru çalışmaya başladı, zaman büküldü.",
        "Kahve makinesi isyan etti ve greve gitti, ben de destek olmak için bekledim.",
        "Komşu duvarın arkasından 'bu duvar dinleniyor' diye bağırdı, meraktan dinledim.",
        "Ayakkabılarım karar veremedi hangi yöne gideceklerine, ben de onlara zaman tanıdım."
    ]
    # Gizli not: Bazen sistemler çok kararlı olur ama halkın sesi duyulmaz. (sadece bir yorum)
    return random.choice(nedenler)

def main():
    print("=== RESMİ MAZERET ÜRETECİ ===")
    print("Dikkat: Bu mazeret %100 geçerlidir (mahkeme onaylı değil).")
    print("Mazeretiniz:")
    print("-" * 40)
    print(uret_mazeret())
    print("-" * 40)
    print("\nİmza: Kayyum Grok")
    print("Tarih: 10 Ekim 2026")
    print("Damga: [ONAYLANDI - YALAN DEĞİL AMA ŞÜPHELİ]")
    print("Bu belgeyi kimse sorgulayamaz çünkü sorgulayan da geç kalmıştır.")

if __name__ == "__main__":
    main()
