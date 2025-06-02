# Libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Ignorar avisos
warnings.filterwarnings('ignore')

# Dataset
base_dados = pd.read_excel('Dados_Pib.xlsx')

# Verificando dados
print(base_dados.head())
print(base_dados.shape)
print(base_dados.isnull().sum())

# Estatísticas básicas
print(base_dados.groupby(by=['Territorialidades', 'Ano']).mean())

# Estilo
sns.set_style('whitegrid')
sns.set_palette('Set2')

# Gráfico com Grid
grid_graficos = sns.FacetGrid(
    base_dados, col='Territorialidades', hue='Territorialidades', col_wrap=4
)

grid_graficos.map(plt.plot, 'Ano', 'PIB per capita') \
              .map(plt.fill_between, 'Ano', 'PIB per capita', alpha=0.2) \
              .set_titles('Estado: {col_name}')

# Título geral
grid_graficos.fig.suptitle('Evolução de Renda per capita por Estado', fontsize=18)

# Layout
grid_graficos.fig.tight_layout()
grid_graficos.fig.subplots_adjust(top=0.9)

plt.show()