

def get_eigens(file):
    """
    Get the eigenvalues from a PCA analysis of the given file.
    """
    from sklearn.decomposition import PCA
    import pandas as pd
    
    ipsatized_data = pd.read_csv(file, index_col=0)
    n_samples = ipsatized_data.shape[0]
    n_features = ipsatized_data.shape[1]
    print(f"Result df shape = {ipsatized_data.shape}, n_samples={n_samples}, n_features={n_features}")

    pca = PCA()
    pca.fit(ipsatized_data)

    explained_variance = pca.explained_variance_ratio_ * 100
    eigenvalues = pca.explained_variance_
    
    pp_eigenvalues = ", ".join([f"{e:.2f}" for e in eigenvalues[:12]])
    print(f"Eigenvalues: {pp_eigenvalues}")
    
    pp_variance_explained = ", ".join([f"{v:.2f}" for v in explained_variance[:12]])
    print(f"Explained variance: {pp_variance_explained}")    
    return eigenvalues


def plot(values_a, title_a, values_b, title_b, n_display = 15):
    """
    Plot the eigenvalues for both populations and against those from original paper.
    """
    import matplotlib.pyplot as plt
    
    # first 12 eigenvalues from the original paper
    eigens_original = [88.1, 80.9, 62.9, 52.4, 33.4, 27.2, 25.2, 20.9, 18.7, 17.4, 16.6, 15.7]

    plt.figure(figsize=(6, 5)) 
    plt.plot(values_a[:n_display], '.-', linewidth=1, markersize=8, alpha=0.5, label=title_a)
    plt.plot(values_b[:n_display], '.-', linewidth=1, markersize=8, alpha=0.5, label=title_b) 
    plt.plot(eigens_original, '.-', linewidth=1, markersize=8, alpha=0.5, label="Original paper's values")

    plt.title(f'Scree Plot of Eigenvalues', fontfamily='Times New Roman', fontsize=10) 
    plt.xlabel('Component Number', fontfamily='Times New Roman', fontsize=10) 
    plt.ylabel('Eigenvalue', fontfamily='Times New Roman', fontsize=10) 
    plt.gca().yaxis.set_tick_params(labelsize=10, labelfontfamily='Times New Roman')
    plt.gca().xaxis.set_tick_params(labelsize=10, labelfontfamily='Times New Roman')
    l = plt.legend()
    plt.setp(l.texts, family='Times New Roman', fontsize=10)
    plt.grid(True)  
    plt.show() 

