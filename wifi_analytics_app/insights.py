import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import psycopg2

def load_data():
    conn = psycopg2.connect(st.secrets["postgresql://postgres:BwkAsWIwvspgfYHDzsQizgwDumIVuZjn@metro.proxy.rlwy.net:54027/railway"], sslmode="require")
    df = pd.read_sql("SELECT * FROM wifi_logs", conn)
    conn.close()
    return df

def analyze_clusters(df):
    le = LabelEncoder()
    df['device_type_encoded'] = le.fit_transform(df['device_type'])
    df['location_encoded'] = le.fit_transform(df['location'])

    X = df[['device_type_encoded', 'location_encoded']]
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['cluster'] = kmeans.fit_predict(X)
    return df
