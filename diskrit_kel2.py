## DISKRIT KELOMPOK 2

import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations

# 1. INISIALISASI DATA
lokasi = {
    0: "Tempat Penampungan",
    1: "Perumahan",
    2: "Pasar",
    3: "Kampus",
    4: "Pertokoan"
}

# Inisial setiap lokasi
inisial = {
    0: "TP",
    1: "PR",
    2: "PS",
    3: "K",
    4: "PT"
}

# Matriks jarak dalam kilometer
jarak = [
    [0, 4, 6, 3, 6],
    [4, 0, 2, 5, 3],
    [6, 2, 0, 4, 6],
    [3, 5, 4, 0, 2],
    [6, 3, 6, 2, 0]
]

jumlah_lokasi = len(lokasi)

# 2. MEMBUAT GRAPH
G = nx.Graph()

# Menambahkan simpul dengan nama lokasi
for nomor, nama in lokasi.items():
    G.add_node(nomor, label=nama, inisial=inisial[nomor])

# Menambahkan sisi dan bobot jarak
for i in range(jumlah_lokasi):
    for j in range(i + 1, jumlah_lokasi):
        G.add_edge(i, j, weight=jarak[i][j])

# 3. MEMBUAT RUTE TERBAIK
titik_tujuan = range(1, jumlah_lokasi)

jarak_minimum = float("inf")
rute_terbaik = None

# Mencoba semua kemungkinan rute
for urutan in permutations(titik_tujuan):

    # Berangkat dan kembali ke titik awal
    rute = (0,) + urutan + (0,)

    total_jarak = 0

    # Menghitung total jarak perjalanan
    for i in range(len(rute) - 1):
        asal = rute[i]
        tujuan = rute[i + 1]

        total_jarak += jarak[asal][tujuan]

    # Memilih rute dengan jarak minimum
    if total_jarak < jarak_minimum:
        jarak_minimum = total_jarak
        rute_terbaik = rute

# 4. MENAMPILKAN HASIL
print("=" * 60)
print("       OPTIMASI RUTE PENGANGKUTAN SAMPAH")
print("          MENGGUNAKAN ALGORITMA TSP")
print("=" * 60)

print("\nDAFTAR LOKASI:")

for nomor, nama in lokasi.items():
    print(f"{inisial[nomor]:<5} = {nama}")

print("\n" + "-" * 60)
print("RUTE PENGANGKUTAN TERBAIK:")
print("-" * 60)

for i, titik in enumerate(rute_terbaik):
    print(inisial[titik], end="")

    if i < len(rute_terbaik) - 1:
        print(" -> ", end="")

print(f"\n\nTOTAL JARAK MINIMUM: {jarak_minimum} km")

print("\nRINCIAN JARAK PERJALANAN:")
print("-" * 60)

for i in range(len(rute_terbaik) - 1):
    asal = rute_terbaik[i]
    tujuan = rute_terbaik[i + 1]

    print(
        f"{inisial[asal]} ({lokasi[asal]})"
        f" -> {inisial[tujuan]} ({lokasi[tujuan]}): "
        f"{jarak[asal][tujuan]} km"
    )

print("\n" + "-" * 60)
print("Semua lokasi berhasil dikunjungi.")
print("Kendaraan kembali ke tempat penampungan.")
print("=" * 60)

# illustrasi
# Posisi simpul
pos = {
    0: (0, 0),   # A: Tempat Penampungan
    1: (4, 0),   # B: Perumahan
    2: (6, 0),   # C: Pasar
    3: (3, 3),   # D: Kampus
    4: (6, 3)    # E: Pertokoan
}

# Membuat dua tampilan graf
fig, axes = plt.subplots(1, 2, figsize=(17, 8))

fig.suptitle(
    "OPTIMASI RUTE PENGANGKUTAN SAMPAH - TSP",
    fontsize=16,
    fontweight="bold"
)

# Label simpul menggunakan inisial lokasi
label_simpul = {
    i: inisial[i] for i in G.nodes()
}

# Label bobot semua sisi
label_jarak = nx.get_edge_attributes(G, "weight")

# GRAF PERTAMA: SELURUH HUBUNGAN
ax = axes[0]

nx.draw_networkx_nodes(
    G, pos,
    node_color="lightblue",
    node_size=2200,
    edgecolors="black",
    linewidths=1.5,
    ax=ax
)

nx.draw_networkx_labels(
    G, pos,
    labels=label_simpul,
    font_size=11,
    font_weight="bold",
    ax=ax
)

nx.draw_networkx_edges(
    G, pos,
    width=1.5,
    edge_color="gray",
    ax=ax
)

nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels=label_jarak,
    font_size=10,
    ax=ax
)

ax.set_title(
    "Graf Berbobot Seluruh Lokasi",
    fontsize=13,
    fontweight="bold"
)

ax.axis("off")

# Rute TSP
ax = axes[1]

# Menampilkan seluruh hubungan sebagai latar
nx.draw_networkx_nodes(
    G, pos,
    node_color="lightblue",
    node_size=2200,
    edgecolors="black",
    linewidths=1.5,
    ax=ax
)

nx.draw_networkx_labels(
    G, pos,
    labels=label_simpul,
    font_size=11,
    font_weight="bold",
    ax=ax
)

nx.draw_networkx_edges(
    G, pos,
    width=1.2,
    edge_color="lightgray",
    ax=ax
)

# Membuat sisi berdasarkan rute terbaik
sisi_rute = [
    (rute_terbaik[i], rute_terbaik[i + 1])
    for i in range(len(rute_terbaik) - 1)
]

# Menampilkan rute optimal
nx.draw_networkx_edges(
    G, pos,
    edgelist=sisi_rute,
    width=4,
    edge_color="red",
    ax=ax
)

# Menampilkan bobot jarak
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels=label_jarak,
    font_size=9,
    ax=ax
)

ax.set_title(
    f"Rute Optimal TSP\nTotal Jarak: {jarak_minimum} km",
    fontsize=13,
    fontweight="bold"
)

ax.axis("off")

# Menimpilkan Visualisasi
plt.tight_layout()
plt.show()
