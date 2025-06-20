rules = [
    ({"demam", "batuk"}, "flu", 0.8),
    ({"flu", "tenggorokan_sakit"}, "radang_tenggorokan", 0.6),
    ({"flu", "pilek"}, "infeksi_saluran_pernapasan_atas", 0.7),
    ({"flu"}, "istirahat_dan_minum_air_putih", 0.9),
    ({"radang_tenggorokan"}, "periksa_ke_dokter", 0.95)
]

print("Masukkan gejala yang kamu alami (pisahkan dengan koma):")
user_input = input(">> ").lower().replace(" ", "").split(",")
facts = set(user_input)

def forward_chaining_with_prob(facts, rules):
    inferred = set(facts)
    hasil_diagnosa = {}
    added = True
    while added:
        added = False
        for kondisi, hasil, prob in rules:
            if kondisi.issubset(inferred) and hasil not in inferred:
                inferred.add(hasil)
                added = True
                if hasil in hasil_diagnosa:
                    hasil_diagnosa[hasil] += prob  
                else:
                    hasil_diagnosa[hasil] = prob
                print(f"[RULE FIRED] {kondisi} => {hasil} (+{prob*100:.0f}%)")
    return hasil_diagnosa

hasil = forward_chaining_with_prob(facts, rules)

print("\n📋 Rekomendasi Diagnosa:")
if hasil:
    for penyakit, skor in sorted(hasil.items(), key=lambda x: x[1], reverse=True):
        print(f"- {penyakit.replace('_', ' ').capitalize()}: keyakinan {skor*100:.1f}%")
else:
    print("❌ Tidak ada penyakit yang cocok dengan gejala tersebut.")
