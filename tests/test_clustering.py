from src.clustering import load_runs, kmeans
X=load_runs('data/ipl_matches.csv'); c,l=kmeans(X,3); assert len(c)==3 and len(l)==len(X)