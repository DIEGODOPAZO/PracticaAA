import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = [

    #APROX1
    ["ANN [3]", 87.32, 1],
    ["ANN [3]", 82.09, 1],
    ["ANN [3]", 80.64, 1],
    ["ANN [3]", 83.25, 1],
    ["ANN [3]", 84.92, 1],
    ["ANN [3]", 93.05, 1],
    ["ANN [3]", 86.15, 1],
    ["ANN [3]", 88.27, 1],
    ["ANN [3]", 83.86, 1],
    ["ANN [3]", 78.50, 1],

    ["KNN K=9", 95.36, 1],
    ["KNN K=9", 94.64, 1],
    ["KNN K=9", 95.00, 1],
    ["KNN K=9", 93.93, 1],
    ["KNN K=9", 95.71, 1],
    ["KNN K=9", 97.14, 1],
    ["KNN K=9", 97.50, 1],
    ["KNN K=9", 96.43, 1],
    ["KNN K=9", 95.36, 1],
    ["KNN K=9", 95.36, 1],

    ["SVM rbf C=200", 95.71, 1],
    ["SVM rbf C=200", 95.35, 1],
    ["SVM rbf C=200", 95.00, 1],
    ["SVM rbf C=200", 92.86, 1],
    ["SVM rbf C=200", 94.64, 1],
    ["SVM rbf C=200", 95.36, 1],
    ["SVM rbf C=200", 96.07, 1],
    ["SVM rbf C=200", 95.00, 1],
    ["SVM rbf C=200", 95.36, 1],
    ["SVM rbf C=200", 93.93, 1],

    ["DT maxDepth=5", 95.36, 1],
    ["DT maxDepth=5", 93.93, 1],
    ["DT maxDepth=5", 94.64, 1],
    ["DT maxDepth=5", 94.28, 1],
    ["DT maxDepth=5", 95.36, 1],
    ["DT maxDepth=5", 95.00, 1],
    ["DT maxDepth=5", 97.14, 1],
    ["DT maxDepth=5", 96.43, 1],
    ["DT maxDepth=5", 95.71, 1],
    ["DT maxDepth=5", 94.64, 1],

    #APROX2
    ["ANN [2,1]", 62.72, 2],
    ["ANN [2,1]", 63.87, 2],
    ["ANN [2,1]", 64.40, 2],
    ["ANN [2,1]", 63.42, 2],
    ["ANN [2,1]", 63.88, 2],
    ["ANN [2,1]", 64.93, 2],
    ["ANN [2,1]", 64.72, 2],
    ["ANN [2,1]", 64.58, 2],
    ["ANN [2,1]", 64.70, 2],
    ["ANN [2,1]", 64.55, 2],

    ["KNN K=9", 77.33, 2],
    ["KNN K=9", 73.99, 2],
    ["KNN K=9", 75.18, 2],
    ["KNN K=9", 77.80, 2],
    ["KNN K=9", 72.32, 2],
    ["KNN K=9", 75.18, 2],
    ["KNN K=9", 73.44, 2],
    ["KNN K=9", 75.12, 2],
    ["KNN K=9", 78.23, 2],
    ["KNN K=9", 75.84, 2],

    ["SVM rbf C=1", 76.61, 2],
    ["SVM rbf C=1", 72.55, 2],
    ["SVM rbf C=1", 73.75, 2],
    ["SVM rbf C=1", 79.00, 2],
    ["SVM rbf C=1", 77.57, 2],
    ["SVM rbf C=1", 73.99, 2],
    ["SVM rbf C=1", 75.36, 2],
    ["SVM rbf C=1", 75.36, 2],
    ["SVM rbf C=1", 75.36, 2],
    ["SVM rbf C=1", 74.40, 2],
    
    ["DT maxDepth=6", 74.22, 2],
    ["DT maxDepth=6", 72.79, 2],
    ["DT maxDepth=6", 73.27, 2],
    ["DT maxDepth=6", 76.61, 2],
    ["DT maxDepth=6", 75.89, 2],
    ["DT maxDepth=6", 73.03, 2],
    ["DT maxDepth=6", 73.21, 2],
    ["DT maxDepth=6", 73.92, 2],
    ["DT maxDepth=6", 74.88, 2],
    ["DT maxDepth=6", 76.08, 2],
    
    #APROX3
    ["ANN [2,1]", 73.42, 3],
    ["ANN [2,1]", 73.17, 3],
    ["ANN [2,1]", 72.68, 3],
    ["ANN [2,1]", 72.67, 3],
    ["ANN [2,1]", 72.43, 3],
    ["ANN [2,1]", 72.72, 3],
    ["ANN [2,1]", 73.01, 3],
    ["ANN [2,1]", 72.16, 3],
    ["ANN [2,1]", 73.32, 3],
    ["ANN [2,1]", 73.52, 3],

    ["KNN K=4", 82.41, 3],
    ["KNN K=4", 84.56, 3],
    ["KNN K=4", 83.12, 3],
    ["KNN K=4", 83.12, 3],
    ["KNN K=4", 85.28, 3],
    ["KNN K=4", 82.76, 3],
    ["KNN K=4", 82.41, 3],
    ["KNN K=4", 83.48, 3],
    ["KNN K=4", 82.94, 3],
    ["KNN K=4", 85.28, 3],

    ["SVM rbf C=200", 80.61, 3],
    ["SVM rbf C=200", 84.38, 3],
    ["SVM rbf C=200", 83.12, 3],
    ["SVM rbf C=200", 82.23, 3],
    ["SVM rbf C=200", 81.51, 3],
    ["SVM rbf C=200", 79.17, 3],
    ["SVM rbf C=200", 83.12, 3],
    ["SVM rbf C=200", 80.79, 3],
    ["SVM rbf C=200", 80.23, 3],
    ["SVM rbf C=200", 81.15, 3],

    ["DT maxDepth=6", 71.99, 3],
    ["DT maxDepth=6", 80.25, 3],
    ["DT maxDepth=6", 74.69, 3],
    ["DT maxDepth=6", 75.22, 3],
    ["DT maxDepth=6", 73.43, 3],
    ["DT maxDepth=6", 72.71, 3],
    ["DT maxDepth=6", 76.48, 3],
    ["DT maxDepth=6", 76.66, 3],
    ["DT maxDepth=6", 75.76, 3],
    ["DT maxDepth=6", 75.94, 3],

    #APROX4
    ["ANN [2,1]", 82.82, 4],
    ["ANN [2,1]", 82.93, 4],
    ["ANN [2,1]", 83.03, 4],
    ["ANN [2,1]", 82.63, 4],
    ["ANN [2,1]", 82.65, 4],
    ["ANN [2,1]", 82.73, 4],
    ["ANN [2,1]", 82.90, 4],
    ["ANN [2,1]", 82.66, 4],
    ["ANN [2,1]", 82.64, 4],
    ["ANN [2,1]", 82.74, 4],

    ["KNN K=4", 77.90, 4],
    ["KNN K=4", 78.97, 4],
    ["KNN K=4", 79.57, 4],
    ["KNN K=4", 78.97, 4],
    ["KNN K=4", 79.69, 4],
    ["KNN K=4", 78.02, 4],
    ["KNN K=4", 79.69, 4],
    ["KNN K=4", 78.38, 4],
    ["KNN K=4", 80.41, 4],
    ["KNN K=4", 78.38, 4],

    ["SVM rbf C=200", 72.40, 4],
    ["SVM rbf C=200", 76.34, 4],
    ["SVM rbf C=200", 74.67, 4],
    ["SVM rbf C=200", 76.34, 4],
    ["SVM rbf C=200", 73.48, 4],
    ["SVM rbf C=200", 76.94, 4],
    ["SVM rbf C=200", 76.82, 4],
    ["SVM rbf C=200", 72.52, 4],
    ["SVM rbf C=200", 74.91, 4],
    ["SVM rbf C=200", 77.66, 4],
    
    ["DT maxDepth=6", 61.05, 4],
    ["DT maxDepth=6", 61.29, 4],
    ["DT maxDepth=6", 56.51, 4],
    ["DT maxDepth=6", 59.98, 4],
    ["DT maxDepth=6", 59.62, 4],
    ["DT maxDepth=6", 62.60, 4],
    ["DT maxDepth=6", 62.01, 4],
    ["DT maxDepth=6", 56.99, 4],
    ["DT maxDepth=6", 61.05, 4],
    ["DT maxDepth=6", 59.62, 4],
    
    #APROX5
    ["ANN [2,8]", 80.71, 5],
    ["ANN [2,8]", 80.56, 5],
    ["ANN [2,8]", 80.91, 5],
    ["ANN [2,8]", 80.86, 5],
    ["ANN [2,8]", 81.16, 5],
    ["ANN [2,8]", 80.70, 5],
    ["ANN [2,8]", 81.01, 5],
    ["ANN [2,8]", 81.13, 5],
    ["ANN [2,8]", 81.29, 5],
    ["ANN [2,8]", 81.17, 5],

    ["KNN K=1", 86.14, 5],
    ["KNN K=1", 87.10, 5],
    ["KNN K=1", 85.90, 5],
    ["KNN K=1", 85.42, 5],
    ["KNN K=1", 84.59, 5],
    ["KNN K=1", 85.66, 5],
    ["KNN K=1", 85.07, 5],
    ["KNN K=1", 86.74, 5],
    ["KNN K=1", 86.98, 5],
    ["KNN K=1", 85.90, 5],

    ["SVM rbf C=200", 82.32, 5],
    ["SVM rbf C=200", 82.20, 5],
    ["SVM rbf C=200", 82.80, 5],
    ["SVM rbf C=200", 84.47, 5],
    ["SVM rbf C=200", 80.05, 5],
    ["SVM rbf C=200", 82.20, 5],
    ["SVM rbf C=200", 83.27, 5],
    ["SVM rbf C=200", 80.17, 5],
    ["SVM rbf C=200", 83.39, 5],
    ["SVM rbf C=200", 83.99, 5],

    ["DT maxDepth=20", 74.31, 5],
    ["DT maxDepth=20", 73.60, 5],
    ["DT maxDepth=20", 73.72, 5],
    ["DT maxDepth=20", 74.19, 5],
    ["DT maxDepth=20", 73.72, 5],
    ["DT maxDepth=20", 77.90, 5],
    ["DT maxDepth=20", 75.63, 5],
    ["DT maxDepth=20", 73.60, 5],
    ["DT maxDepth=20", 76.11, 5],
    ["DT maxDepth=20", 75.75, 5],
]

df = pd.DataFrame(data, columns=['Modelo de aprendizaje automático', 'Precisión', 'Aproximación'])

for i in range(1,6):
    aprox_data = df[df['Aproximación'] == i]
# Create a combined swarmplot with boxes
    plt.figure(figsize=(10, 6))
    sns.swarmplot(x='Modelo de aprendizaje automático', y='Precisión', data=aprox_data, hue="Modelo de aprendizaje automático", palette='muted', linewidth=1)  # Swarmplot
    sns.boxplot(x='Modelo de aprendizaje automático', y='Precisión', data=aprox_data, width=0.5, fill=False, color='black')  # Boxplot
    plt.title('Precisión de los modelos de aprendizaje automático en la aproximación ' + str(i))
    plt.xlabel('Modelo de aprendizaje automático')
    plt.ylabel('Precisión (%)')
    plt.savefig('graficas/aprox' + str(i) + '.png')
