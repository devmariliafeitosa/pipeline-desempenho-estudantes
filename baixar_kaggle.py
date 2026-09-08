import kagglehub

caminho = kagglehub.dataset_download(
    "csafrit2/higher-education-students-performance-evaluation",
    output_dir="data/raw/kaggle"
)

print("Dataset baixado com sucesso!")
print("Local:", caminho)