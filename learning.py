import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score

df = pd.read_csv('emails.csv')


df = df.drop(columns=["Email No."])


X = df.drop(columns=["Prediction"])  
y = df["Prediction"]                 


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

print("📊 Akurasi Model:", accuracy_score(y_test, y_pred))
print("\n🧾 Laporan Klasifikasi:\n", classification_report(y_test, y_pred))
