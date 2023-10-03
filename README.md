# BetaGroup_JC_DS_OL_10_FinalProject
**Model Deployment Streamlit** -> [link]( https://deployment-final-project-b5npck77wodulypkulx8lw.streamlit.app/)

-	Eldwin Surya Kusuma Wardojo
-	Tan William Reinaldo
-	Raden Fadhlan Auffar
  
# Business Understanding & Problem Statement
Bank memiliki 2 jenis income, yaitu fee based income dan spread based income. Bank mengeluarkan produk investasi khusunya deposito untuk menambahkan dana kelolaan yang dapat disalurkan sehingga mendapatkan keuntungan. Telemarketing merupakan salah satu cara yang dapat dilakukan untuk menawarkan produk deposito.
1.	Context  -> Bank Portugal memerlukan tambahan dana kelolaan untuk disalurkan kepada peminjam yang diharapkan dapat meningkatkan pendapatan perusahaan. Bank tersebut memiliki produk deposito. Produk deposito ditawarkan dengan cara melakukan campaign telemarketing.
2.	Problem Statement -> Proses campaign telemarketing tidak selalu mendapatkan nasabah yang ingin membuka deposito, sehingga bank perlu meningkatkan efisiensi dalam proses campaign. Proses perlu dibuat efisien supaya bank dapat memprioritaskan nasabah yang cenderung akan membuka deposito, sehingga dapat meningkatkan dana kelolaan bank serta dapat meminimalisir biaya operasional campaign.
3.	Goals -> Bank ingin bisa memprediksi calon nasabah mana yang cenderung akan membuka akun deposito, sehingga campaign telemarketing lebih efisein. Campaign telemarketing yang efisien dapat lebih memaksimalkan tambahan dana kelolaan serta diharapkan dapat meminimalisir biaya operasional.

# Data Understanding
Dataset berasal dari Kaggle, setiap baris merepresentasikan nasabah yang telah dihubungi untuk ditawarkan produk deposito. Dataset memiliki fitur yang mendeskripsikan data client bank, campaign, dan indeks sosial ekonomi.

# EDA
Berikut beberapa temuan hasil EDA:
-	Terdapat temuan data unknown serta data tidak valid
-	Outlier relatif sedikit
-	Terdapat masalah multikolinearitas 
-	Imbalanced class pada target

# Data Preparation
1.	Data preparation for modelling
2.	Data preparation for analysis

# Methodology (data analysis & modelling)
1.	Data Analysis -> Salah satu insight yang didapat adalah untuk mencari new customer bisa fokus kepada nasabah yang masuk ke kategori elderly.
2.	Modeling ->  Dilakukan beberapa benchmark model. Model terpilh adalah LGBM + ROS + Tuning karena lebih menguntungkan bank serta memiliki metrik evaluasi tertinggi. 

# Kesimpulan & Rekomendasi 
-	Bisnis -> Bank menggunakan model yang telah dibuat sehingga dapat meminimalisir biaya kontak, serta dapat mengevaluasi proses dokumentasi data.
-	Model -> Mencoba memodelkan kembali berdasarkan hasil temuan feature importance serta menganalisis hari error model.

# Deployment
Menyimpan model terpilih untuk digunakan dalam streamlit
