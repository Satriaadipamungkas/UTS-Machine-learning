library(ggplot2)

fakultas <- c("Bisnis", "D3 Perhotelan", "ICT", "Ilmu Komunikasi", "Seni dan Desain")
jumlah_mahasiswa <- c(260, 28, 284, 465, 735)
akreditasi <- c("A", "A", "B", "A", "A")
info_mahasiswa <- data.frame(fakultas, jumlah_mahasiswa, akreditasi)


gambar <- ggplot(info_mahasiswa, aes(x = fakultas, y = jumlah_mahasiswa, fill = fakultas)) +
  geom_bar(stat = "identity", width=1.0) +
  labs(title = "Jumlah Mahasiswa per Fakultas", 
       x = "Nama Fakultas", 
       y = "Jumlah Mahasiswa") +
  theme(
    plot.title = element_text(hjust = 0.5, size = rel(1)),
  )


gambar