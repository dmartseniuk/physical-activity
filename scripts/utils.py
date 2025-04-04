import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import seaborn as sns
import pandas as pd

def plot_conf_matrix(y_true, y_pred, encoder, title="Confusion Matrix", figsize=(12, 8)):
    labels = sorted(np.unique(y_true))  # these are integer encoded
    display_labels = encoder.inverse_transform(labels)  # decode labels

    cm = confusion_matrix(y_true, y_pred, labels=labels)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=display_labels)

    fig, ax = plt.subplots(figsize=figsize)
    disp.plot(cmap='Blues', ax=ax, xticks_rotation=45)
    ax.set_title(title)
    plt.show()

def plot_feature_importance(model, feature_names, top_n=20):
    importances = model.feature_importances_
    feature_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": importances
    }).sort_values(by="Importance", ascending=False).head(top_n)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Importance", y="Feature", data=feature_df)
    plt.title("Top Feature Importances")
    plt.tight_layout()
    plt.show()
