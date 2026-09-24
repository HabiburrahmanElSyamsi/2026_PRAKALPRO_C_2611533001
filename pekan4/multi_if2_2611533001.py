# Input dari user
total_belanja_3001 = float(input("Masukkan total belanja (Rp): "))

# Input status member (mengecek apakh user mengetik 'y' atau 'ya')
input_member_3001 = input("Apakah Anda Member? (y/t): ").strip().lower()
is_member_3001 = input_member_3001 in ["y", "ya"]

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_3001 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_3001 = input_promo_3001 in ["y", "ya"]

total_diskon_persen_3001 = 0

if total_belanja_3001 > 1000000:
    total_diskon_persen_3001 += 10 # Diskon belanja besar

if is_member_3001:
    total_diskon_persen_3001 += 5 # Diskon member

if kode_promo_valid_3001:
    total_diskon_persen_3001 += 15 # Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_3001 = total_belanja_3001 * (total_diskon_persen_3001 / 100)
total_bayar_3001 = total_belanja_3001 - nominal_diskon_3001

# Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon : {total_diskon_persen_3001}% (Rp {nominal_diskon_3001 :,.0f})")
print(f"Total Bayar : Rp {total_bayar_3001 :,.0f}")

print(f"Total diskon yang anda dapatkan: {total_diskon_persen_3001}")
