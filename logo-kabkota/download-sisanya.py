#!/usr/bin/env python3
"""
==========================================================
DOWNLOAD SISA LOGO KABUPATEN/KOTA INDONESIA
==========================================================

Jalankan script ini di komputer kamu untuk mendownload
logo yang belum terdownload dari Wikimedia Commons.

Cara pakai:
  python3 download-sisanya.py

Script ini akan:
- Membaca index.json untuk tahu mana yang sudah ada
- Download sisanya dari Wikimedia Commons
- Update index.json setelah selesai

Requirements: pip install requests beautifulsoup4
==========================================================
"""

import requests
import json
import os
import time
import hashlib
import re
import unicodedata

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_FILE = os.path.join(SCRIPT_DIR, "index.json")

SESSION = requests.Session()
SESSION.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
})


def slugify(text):
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[-\s]+', '-', text).strip('-')
    return text


def download_image(url, filepath, retries=3):
    """Download image with retries and rate-limit handling."""
    for attempt in range(retries):
        try:
            r = SESSION.get(url, timeout=30)
            if r.status_code == 200:
                ct = r.headers.get('content-type', '')
                if 'image' in ct:
                    with open(filepath, 'wb') as f:
                        f.write(r.content)
                    return len(r.content)
            elif r.status_code == 429:
                wait = 10 * (attempt + 1)
                print(f"    Rate limited, waiting {wait}s...")
                time.sleep(wait)
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(3)
    return 0


def main():
    print("=" * 55)
    print("DOWNLOAD SISA LOGO KAB/KOTA INDONESIA")
    print("=" * 55)

    if not os.path.exists(INDEX_FILE):
        print("Error: index.json tidak ditemukan!")
        return

    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        index = json.load(f)

    total = 0
    missing = []

    for category in ['provinsi', 'kabupaten', 'kota']:
        items = index.get(category, [])
        for item in items:
            total += 1
            if not item.get('downloaded'):
                missing.append({**item, 'category': category})

    print(f"Total logo: {total}")
    print(f"Sudah ada: {total - len(missing)}")
    print(f"Perlu download: {len(missing)}")

    if not missing:
        print("\nSemua sudah terdownload!")
        return

    print(f"\nMemulai download...\n")

    success = 0
    failed = 0

    for i, item in enumerate(missing):
        name = item['name']
        slug = item['slug']
        category = item['category']
        wiki_url = item.get('wiki_url', '')

        # Create directory
        if category == 'provinsi':
            dir_path = os.path.join(SCRIPT_DIR, '_provinsi')
        elif category == 'kota':
            dir_path = os.path.join(SCRIPT_DIR, 'kota')
        else:
            dir_path = os.path.join(SCRIPT_DIR, 'kabupaten')

        os.makedirs(dir_path, exist_ok=True)

        # Determine extension from wiki_url
        ext = '.png'
        if wiki_url:
            lower_url = wiki_url.lower()
            if lower_url.endswith('.svg'):
                ext = '.svg'
            elif lower_url.endswith('.jpg') or lower_url.endswith('.jpeg'):
                ext = '.jpg'
            elif lower_url.endswith('.gif'):
                ext = '.gif'

        filepath = os.path.join(dir_path, f"{slug}{ext}")

        # Skip if file already exists and is valid
        if os.path.exists(filepath) and os.path.getsize(filepath) > 1000:
            success += 1
            item['downloaded'] = True
            item['local_file'] = os.path.relpath(filepath, SCRIPT_DIR)
            continue

        # Try wiki_url (direct Wikimedia Commons)
        downloaded = False
        if wiki_url:
            size = download_image(wiki_url, filepath)
            if size > 0:
                downloaded = True

        # Fallback: try API
        if not downloaded:
            api_url = item.get('api_url', '')
            if api_url:
                size = download_image(api_url, filepath)
                if size > 0:
                    downloaded = True

        if downloaded:
            success += 1
            item['downloaded'] = True
            item['local_file'] = os.path.relpath(filepath, SCRIPT_DIR)
            print(f"  [{i+1}/{len(missing)}] ✓ {name}")
        else:
            failed += 1
            if os.path.exists(filepath) and os.path.getsize(filepath) < 500:
                os.remove(filepath)
            print(f"  [{i+1}/{len(missing)}] ✗ {name}")

        time.sleep(0.5)  # Rate limiting

    # Update index
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        index['stats']['downloaded'] = total - failed
        json.dump(index, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*55}")
    print(f"HASIL")
    print(f"{'='*55}")
    print(f"Berhasil: {success}")
    print(f"Gagal:    {failed}")
    print(f"Total tersedia: {total - failed}/{total}")

    if failed > 0:
        print(f"\nJalankan script ini lagi untuk retry yang gagal.")


if __name__ == '__main__':
    main()
