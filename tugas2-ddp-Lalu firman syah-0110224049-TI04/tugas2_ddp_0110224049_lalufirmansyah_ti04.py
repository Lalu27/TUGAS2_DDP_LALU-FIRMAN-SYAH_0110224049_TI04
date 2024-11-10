# TUGAS 2 DDP | BUKAN TUGAS PROJECT
# ==========
# Buat Dictionary (Bobot Penilaian 15 Point):
# p1 : nama=>Budi, jabatan=> Manager, agama=>Islam, status=>Menikah
# p2 : nama=>Siti, jabatan=> Asisten Manager, agama=>Islam, status=>Menikah
# p3 : nama=>I Gede, jabatan=> Supervisor, agama=>Hindu, status=>Menikah
# p4 : nama=>Joko, jabatan=> Staff, agama=>Islam, status=>Belum Menikah
# p5 : nama=>Alex, jabatan=> Staff, agama=>Kristen Protestan, status=>Belum Menikah

# Cetaklah Slip Gaji Pegawai Menggunakan Nested Loop Dengan Data:
# - Nama (Bobot Penilaian 5 Point)
# - Jabatan (Bobot Penilaian  5 Point)
# - Agama (Bobot Penilaian  5 Point)
# - Status (Bobot Penilaian  5 Point)
# - Gaji Pokok: (Bobot Penilaian 10 Point)
#   Gunakan kondisional if:
#   (Manager=>15 jt, Asmen=>10 jt, Supervisor=>7 jt, Staff=> 4jt)
# - Tunjangan jabatan => 30% dari gapok (Bobot Penilaian  5 Point)
# - BPJS = 10 % dari gapok (Bobot 5 Penilaian Point)
# - Tunjangan keluarga: (Bobot Penilaian 10 Point)
#   Gunakan Tuple & List 
#   10% dari gapok untuk yg sudah menikah
# - Gaji Kotor (Jumlahkan semua element gaji) (Bobot Penilaian 5 Point)
# - Zakat Profesi 2,5% (Bobot Penilaian 10 Point)
#   (gunakan tuple list: untuk pegawai muslim dan minimal gaji kotor 7 jt )
# - Gaji Bersih => Gaji Kotor - Zakat Profesi (Bobot Penilaian 5 Point)
# Pengumpulan Tugas2:
# ===================
# nama_file: tugas2_ddp_nim_nama_lengkap_kelas.py
# dead_line: Selasa, 12 November 2024 pukul 23:59
# Dikumpulkan ke gform yang ada di deskripsi
 

pegawai = {
    "p1": {"nama": "Budi", "jabatan": "Manager", "agama": "Islam", "status": "Menikah"},
    "p2": {"nama": "Siti", "jabatan": "Asisten Manager", "agama": "Islam", "status": "Menikah"},
    "p3": {"nama": "I Gede", "jabatan": "Supervisor", "agama": "Hindu", "status": "Menikah"},
    "p4": {"nama": "Joko", "jabatan": "Staff", "agama": "Islam", "status": "Belum Menikah"},
    "p5": {"nama": "Alex", "jabatan": "Staff", "agama": "Kristen Protestan", "status": "Belum Menikah"}
}

for i,j in pegawai.items():
    nama = j["nama"]
    jabatan = j["jabatan"]
    agama = j["agama"]
    status = j["status"]

    if jabatan == "Manager":
        gapok = 15000000
    elif jabatan == "Asisten Manager":
        gapok = 10000000
    elif jabatan == "Supervisor":
        gapok = 7000000
    elif jabatan == "Staff":
        gapok = 4000000
    else:
        0
        
    tunjab = 30/100 * gapok

    bpjs = 10/100 * gapok
    tunkel = []
    if status == "Menikah":
        tunkel = [10/100 * gapok]
    else:
        0
        
    gakor = gapok + tunjab + bpjs + sum(tunkel)
    zakat_prof = []
    if agama == "Islam" and gakor >= 7000000:
        zakat_prof = [2.5/100 * gakor]
    else:
        0

    gaber = gakor - sum(zakat_prof)

    print(f"\nSlip Gaji para Pegawai",
        f"\n----------------------",
        f"\nNama       : {nama}",
        f"\nJabatan    : {jabatan}",
        f"\nAgama      : {agama}",
        f"\nStatus     : {status}",
        f"\nGaji Pokok : Rp{gapok}",
        f"\nTunjangan Jabatan : Rp{tunjab}",
        f"\nBPJS       : Rp{bpjs}",
        f"\nTunjangan Keluarga: Rp{tunkel}",
        f"\nGaji Kotor : Rp{gakor}",
        f"\nZakat Profesi : Rp{zakat_prof}",
        f"\nGaji Bersih: Rp{gaber}",
        "\n================================"
        )

