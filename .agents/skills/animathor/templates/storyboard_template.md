# [Judul Video / Video Title]

## 1. Mathematical Pre-Flight Audit (Verifikasi Akurasi & Teorema)

Sebelum menulis naskah, pastikan seluruh fakta matematis diverifikasi:
- **Teorema / Konsep Kunci**: [e.g. Teorema Deret Fourier & Syarat Dirichlet untuk gelombang periodik]
- **Persamaan Eksak**:
  $$\text{[Tulis rumus formal lengkap beserta domain dan batasan indeks, e.g. } S_N(x) = \frac{4}{\pi}\sum_{k=1,3,\dots}^N \frac{\sin(kx)}{k} \text{]}$$
- **Konstanta / Batas Kritis**: [e.g. Batas overshoot Gibbs = $\frac{1}{\pi}\int_0^\pi \frac{\sin(t)}{t}dt - \frac{1}{2} \approx 0.08949 \approx 8.95\%$]
- **Tipe Konvergensi**: [e.g. Konvergen titik-demi-titik (pointwise) ke rata-rata lompatan $f(0)=0$, bukan konvergen seragam (uniform)]
- **Pemeriksaan Anti-Mitos**: [e.g. Menambah harmonik tidak menghilangkan lonjakan; frekuensi bertambah hanya memampatkan osilasi mendekati titik patahan]

---

## 2. Parameter Produksi & Narasi

- **Format Video**: [16:9 Widescreen (1920x1080) ATAU 9:16 Portrait Shorts (1080x1920)]
- **Target Durasi Total**: [e.g. 60 detik]
- **Target Kecepatan Tutur**: 130 - 140 kata per menit (~2.1 - 2.3 kata per detik)
- **Anggaran Kata Total (Word Budget)**: Maksimal [Target Durasi x 2.0] kata = [e.g. 120 kata]
- **Palet Warna**:
  - `BG`: `#0B0F19` (Slate Dark Cinema)
  - `PRIMARY`: `#58C4DD` (Cyan-Blue 3B1B)
  - `SECONDARY`: `#83C167` (Sage Green 3B1B)
  - `ACCENT`: `#FACC15` (Vibrant Yellow)
  - `ALERT`: `#FF5964` (Coral Red)
  - `MUTED`: `#64748B` (Structural Slate Grey)

---

## 3. Two-Column Audio/Visual (AV) Script

| Beat & Durasi | Aksi Visual & Mobjects (Manim) | Titik Sinkronisasi [Trigger] | Naskah Narasi / Voiceover (Kata & WPM) | Teks Layar / MathTex |
|---|---|---|---|---|
| **Beat 1: The Hook**<br>00:00 - 00:10<br>*(10 detik)*<br>Anggaran: $\le 20$ kata | - `title = Text(...)` muncul di atas<br>- `axes = Axes(...)` digambar halus (opacity 0.3)<br>- `target = DashedLine(...)` gelombang kotak target muncul (opacity 0.6) | Pada kata: **"sudut"** | *"Bisakah gelombang sinus yang lentur membentuk sudut tegak 90 derajat?"*<br><br>*(10 kata • 1.0 wps • [PASS])* | **Title**: Sudut Patah Fourier<br><br>**Subtitle**: Bisakah gelombang mulus membentuk sudut tegak? |
| **Beat 2: Resep Harmonik**<br>00:10 - 00:25<br>*(15 detik)*<br>Anggaran: $\le 30$ kata | - Formula deret Fourier $S_N(x)$ muncul<br>- Kurva $N=1$ digambar dengan `Create(curve)`<br>- Bertransformasi bertahap ke $N=3$, $N=7$, dan $N=19$<br>- Lereng kurva tampak semakin curam | Pada kata: **"harmonik"** | *"Deret Fourier menjumlahkan harmonik ganjil: semakin tinggi frekuensinya, lereng patahan semakin tegak mendekati kotak."*<br><br>*(16 kata • 1.07 wps • [PASS])* | **Math**: $S_N(x) = \frac{4}{\pi}\sum_{k=1,3,\dots}^N \frac{\sin(kx)}{k}$<br><br>**Badge**: $N = 1 \to 19$ |
| **Beat 3: The Aha Moment**<br>00:25 - 00:42<br>*(17 detik)*<br>Anggaran: $\le 34$ kata | - Harmonik dinaikkan ke $N=51$<br>- `peak_dot = Dot(color=ALERT)` muncul di puncak riak pertama<br>- `brace = Brace(...)` mengukur overshoot $+8.95\%$<br>- Jeda visual 2.5 detik untuk mencerna | Pada kata: **"lonjakan"** | *"Namun tepat di tepi patahan, selalu timbul lonjakan sekitar 8.95 persen. Sebanyak apa pun gelombang ditambah, lonjakan ini tidak pernah hilang."*<br><br>*(23 kata • 1.35 wps • [PASS])* | **Sorotan**: Overshoot Tetap Ada!<br><br>**Math**: $+8.95\%$ dari tinggi lompatan |
| **Beat 4: Resolusi & Penutup**<br>00:42 - 00:55<br>*(13 detik)*<br>Anggaran: $\le 26$ kata | - Sorotan titik tengah konvergensi Dirichlet di $(0,0)$<br>- Fade out seluruh elemen secara elegan (*clean exit*) | Pada kata: **"Gibbs"** | *"Inilah Fenomena Gibbs: batas matematis saat gelombang kontinu dipaksa membentuk diskontinuitas."*<br><br>*(12 kata • 0.92 wps • [PASS])* | **Kesimpulan**: Fenomena Gibbs<br><br>**Math**: $f(0) = \frac{1 + (-1)}{2} = 0$ |

---

## 4. Anti-Slop Quality & Accuracy Checklist

- [ ] **Bebas Tanda Pisah Em-Dash**: Tidak ada karakter tanda pisah em-dash dalam naskah narasi, subtitle, maupun teks layar (Aturan R-02).
- [ ] **Bebas Kata Klise AI**: Naskah bebas dari istilah pemasaran dan meta-komentar klise sesuai panduan 06.
- [ ] **Anggaran Kecepatan Tutur**: Tidak ada beat dengan kecepatan tutur melebihi 2.3 kata per detik.
- [ ] **Akurasi Matematis**: Definisi batas, notasi rumus LaTeX, dan tipe konvergensi sudah diverifikasi secara formal.
- [ ] **Jeda Bernapas (Breathing Room)**: Terdapat jeda hening minimal 1.5 hingga 2.5 detik setelah penyingkapan konsep puncak (Aha Moment).
- [ ] **Titik Sinkronisasi Jelas**: Setiap animasi visual memiliki pemicu kata kunci yang eksplisit.
